from . import db
from datetime import datetime

class ContactUsModel(db.Model):
	__tablename__ = 'contact_us'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=False, nullable=False)
	subject = db.Column(db.String(100), unique=False, nullable=False)
	email = db.Column(db.String(255), unique=False, nullable=False)
	mobile = db.Column(db.String(15), unique=False, nullable=False)
	mssg = db.Column(db.String(255), unique=False, nullable=False)
	created_at = db.Column(db.DateTime, default=datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

	def to_json(self):
		return {
			'id': self.id,
			'name': self.name, 
			'subject': self.subject,
			'email': self.email,
			'mobile': self.mobile,
			'mssg': self.mssg
		}