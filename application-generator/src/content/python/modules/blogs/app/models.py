from . import db
from datetime import datetime
from sqlalchemy import event
from slugify import slugify
# import base64


class BlogsModel(db.Model):
	__tablename__ = 'blogs'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Text, nullable=False)
	summary = db.Column(db.Text, nullable=False)
	slug = db.Column(db.Text, nullable=False)
	content = db.Column(db.Text, unique=False, nullable=False)
	image_name = db.Column(db.Text, unique=False, nullable=True)
	image_path = db.Column(db.Text, unique=False, nullable=True)
	created_at = db.Column(db.DateTime, default=datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
	

	@staticmethod
	def generate_slug(target, value, oldvalue, initiator):
		if value and (not target.slug or value != oldvalue):
			target.slug = slugify(value)
	
	def __repr__(self):
		return '<BlogsModel {}-{}-{}-{}-{}-{}-{}-{}>'.format(self.id, self.title, self.summary, self.slug, self.content, self.image_name, self.image_path, self.created_at)

	def to_json(self):
		return {
			'id': self.id,
			'title': self.title, 
			'summary': self.summary, 
			'slug': self.slug,
			'content': self.content,
			'image_name': self.image_name,
			'image_path': self.image_path,
			'created_at': self.created_at
		}

event.listen(BlogsModel.title, 'set', BlogsModel.generate_slug, retval=False)