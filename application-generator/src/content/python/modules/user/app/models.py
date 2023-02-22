# app/models.py
import secrets, jwt, re, os
from flask import current_app, jsonify
from datetime import datetime, timedelta
from time import time
from sqlalchemy import select, delete, orm as db_orm
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from app.constants import Gender, UserType
from sqlalchemy import event

class Updateable:
    def update(self, data):
        for attr, value in data.items():
            setattr(self, attr, value)


class Token(db.Model):
	__tablename__ = 'tokens'

	id = db.Column(db.Integer, primary_key=True)
	access_token = db.Column(db.String(64), nullable=False, index=True)
	access_expiration = db.Column(db.DateTime, nullable=False)
	refresh_token = db.Column(db.String(64), nullable=False, index=True)
	refresh_expiration = db.Column(db.DateTime, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), index=True)
	created_at = db.Column(db.DateTime, index=True, default=datetime.now)
	updated_at = db.Column(db.DateTime, index=True, default=datetime.now, 
							onupdate=datetime.now)


	def generate(self):
		self.access_token = secrets.token_urlsafe()
		self.access_expiration = datetime.now() + \
			timedelta(minutes=current_app.config['ACCESS_TOKEN_MINUTES'])
		self.refresh_token = secrets.token_urlsafe()
		self.refresh_expiration = datetime.now() + \
			timedelta(days=current_app.config['REFRESH_TOKEN_DAYS'])

	def expire(self):
		self.access_expiration = datetime.now()
		self.refresh_expiration = datetime.now()

	@staticmethod
	def clean():
		"""Remove any tokens that have been expired for more than a day."""
		yesterday = datetime.now() - timedelta(days=1)
		tokens = Token.query.filter(Token.refresh_expiration < yesterday)\
			.all()
		if tokens:
			for token in tokens:
				db.session.delete(token)
				db.session.commit()


class User(UserMixin, Updateable, db.Model):
	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(30), index=True, nullable=False)
	last_name = db.Column(db.String(30), index=True, nullable=False)
	email = db.Column(db.String(120), index=True, unique=True, nullable=False)
	user_type = db.Column('user_type', db.Enum('user', 'vendor', 'super-admin', 'sub-admin'), default='user')
	gender = db.Column('gender', db.Enum('male', 'female', 'not-specified'), default='not-specified')
	dob = db.Column(db.Date, index=True, nullable=True)
	username = db.Column(db.String(30), index=True, nullable=True)
	password_harsh = db.Column(db.String(128))
	is_active = db.Column(db.Boolean, default=False)
	email_verified = db.Column(db.Boolean, default=False)
	mobile_number = db.Column(db.String(15), index=True, unique=True, nullable=True)
	provider = db.Column(db.String(20), index=True, nullable=True)
	provider_id = db.Column(db.Text, nullable=True)
	first_seen = db.Column(db.DateTime, default=datetime.utcnow)
	last_seen = db.Column(db.DateTime, default=datetime.utcnow)
	remember_token = db.Column(db.Text, nullable=True)	
	created_at = db.Column(db.DateTime, index=True, default=datetime.now)
	updated_at = db.Column(db.DateTime, index=True, default=datetime.now, onupdate=datetime.now)

	tokens = db_orm.relationship('Token', 
									backref="user",
									passive_deletes=True
								)
	attachment = db_orm.relationship('Attachment', 
									backref="user",
									passive_deletes=True
								)
	address = db_orm.relationship('Address', 
									backref="user",
									passive_deletes=True
								)
	vendors = db_orm.relationship('Vendors', 
									backref="user",
									passive_deletes=True
								)
	

	def attachment_select(self):
		attachment = Attachment.query.filter(db_orm.with_parent(self, User.attachment))\
			.all()
		response = jsonify(attachment)
		return response
	
	def address_select(self):
		address = Address.query.filter(db_orm.with_parent(self, User.address))\
			.all()
		response = jsonify(address)
		return response

	def __repr__(self):
		return '<User %r>' % self.first_name

	
	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_harsh = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_harsh, password)

	def ping(self):
		self.last_seen = datetime.utcnow()

	def to_dict(self, include_email=False):
		data = {
			'id': self.id,
			'first_name': self.first_name,
			'last_name': self.last_name,
			'dob': self.dob,
			'gender': self.gender,
			'user_type': self.user_type,
			'mobile_number': self.mobile_number,
			'provider': self.provider,
			'is_active': self.is_active,
			'created_at': self.created_at,
			'updated_at': self.updated_at
		}
		if include_email:
			data['email'] = self.email
		return data

	def get_roles(self):
		return self.user_type

	def generate_auth_token(self):
		token = Token(user=self)
		token.generate()
		self.token = token
		return self.token

	@staticmethod
	def verify_access_token(access_token, refresh_token=None):
		token = db.session.scalar(Token.query.filter_by(
			access_token=access_token))
		if token:
			if token.access_expiration > datetime.now():
				token.user.ping()
				db.session.commit()
				return token.user

	@staticmethod
	def verify_refresh_token(refresh_token, access_token):
		token = db.session.scalar(Token.query.filter_by(
			refresh_token=refresh_token, access_token=access_token))
		if token:
			if token.refresh_expiration > datetime.now():
				return token

			# someone tried to refresh with an expired token
			# revoke all tokens from this user as a precaution
			token.user.revoke_all()
			db.session.commit()

	def revoke_all(self):
		tokens = Token.query.filter(Token.user == self)\
			.all()
		for token in tokens:
			db.session.delete(token)
			db.session.commit()
		

	def generate_reset_token(self):
		return jwt.encode(
			{
				'exp': time() + int(os.environ.get('RESET_TOKEN_MINUTES')) * 60,
				'reset_email': self.email,
			},
			os.environ.get('SECRET_KEY'),
			algorithm='HS256'
		)
		
	@staticmethod
	def verify_reset_token(reset_token):
		try:
			data = jwt.decode(reset_token, os.environ.get('SECRET_KEY'),
								algorithms=['HS256'])
		except jwt.PyJWTError:
			return
		return db.session.scalar(User.query.filter_by(
			email=data['reset_email']))


class Address(db.Model):
	__tablename__ = 'address'

	id = db.Column(db.Integer, primary_key=True)
	ref_address_id = db.Column(db.Integer, nullable=True)
	address = db.Column(db.String(255), index=True, nullable=True)
	ref_local_govt = db.Column(db.Text, nullable=False)
	ref_state = db.Column(db.Text, nullable=False)
	postal_code = db.Column(db.String(10), nullable=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=True)
	email = db.Column(db.Text, nullable=True)
	created_at = db.Column(db.DateTime, index=True, default=datetime.now)
	updated_at = db.Column(db.DateTime, index=True, default=datetime.now, onupdate=datetime.now)


	def __repr__(self):
		return '<Address {}>'.format(self.id)

class Vendors(db.Model):
	__tablename__ = 'vendors'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text, nullable=False)
	slug = db.Column(db.Text, nullable=True)
	business_description = db.Column(db.Text, nullable=True)
	business_bank_name = db.Column(db.Text, nullable=True)
	business_bank_name_value = db.Column(db.Text, nullable=True)
	business_account_no = db.Column(db.Text, nullable=True)
	business_account_name = db.Column(db.Text, nullable=True)
	business_address = db.Column(db.Text, nullable=True)
	business_city = db.Column(db.Text, nullable=True)
	business_state = db.Column(db.Text, nullable=True)
	business_state_value = db.Column(db.Text, nullable=True)
	business_image_path = db.Column(db.Text, nullable=True)
	business_subaccount_code = db.Column(db.Text, nullable=True)
	business_percentage_charge = db.Column(db.Integer, nullable=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
	created_at = db.Column(db.DateTime, index=True, default=datetime.now)
	updated_at = db.Column(db.DateTime, index=True, default=datetime.now, onupdate=datetime.now)
	

	def __repr__(self):
		return '<Vendors {}-{}-{}-{}-{}-{}-{}-{}-{}-{}>'.format(
			self.name, 
			self.slug, 
			self.business_description, 
			self.business_image_path, 
			self.business_bank_name,
			self.business_account_no,
			self.business_account_name,
			self.business_address,
			self.business_city,
			self.business_state
			)


	@property
	def slugify(self):
		return self.slug

	@slugify.setter
	def slugify(self, slug):
		self.slug = re.sub('\s+', '-', slug)

	def to_json(self):
		return {
			'id': self.id,
			'name': self.name, 
			'slug': self.slug,
			'business_description': self.business_description,
			'business_image_path': self.business_image_path,
			"user_id":self.user_id,
			"business_bank_name": self.business_bank_name,
			"business_account_no": self.business_account_no,
			"business_account_name": self.business_account_name,
			"business_address": self.business_address,
			"business_city": self.business_city,
			"business_state": self.business_state,
			"business_subaccount_code": self.business_subaccount_code,
			"business_percentage_charge": self.business_percentage_charge
		}

class Attachment(db.Model):
	__tablename__ = 'attachment'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), index=True, nullable=False)
	path = db.Column(db.String(255), index=True, nullable=False)
	entity_id = db.Column(db.Integer)
	entity_type = db.Column(db.String(100), index=True, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
	created_at = db.Column(db.DateTime, index=True, default=datetime.now)
	updated_at = db.Column(db.DateTime, index=True, default=datetime.now, onupdate=datetime.now)


	def __repr__(self):
		return '<Attachment {}>'.format(self.path)