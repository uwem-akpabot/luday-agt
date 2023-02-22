from flask import jsonify, Blueprint, abort

from flask_restful import (Resource, Api, reqparse,
                               fields, marshal_with)

from ..contact_api.contact_us import ContactUs
from .. import db


contact_us_fields = {
    'name': fields.String,
    'subject': fields.String,
    'email': fields.String,
    'mobile': fields.Integer,
	'mssg': fields.String
}

class Contact(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument(
			'name',
			required=True,
			help='No name title provided',
			location=['form', 'json']
		)
		self.reqparse.add_argument(
			'email',
			required=True,
			help='No email provided',
			location=['form', 'json']
		)
		self.reqparse.add_argument(
			'subject',
			required=True,
			help='No subject provided',
			location=['form', 'json']
		)
		self.reqparse.add_argument(
			'mobile',
			required=True,
			help='No mobile provided',
			location=['form', 'json']
		)
		self.reqparse.add_argument(
			'mssg',
			required=True,
			help='No message provided',
			location=['form', 'json']
		)
		super().__init__()

	def get(self):
		contact_us = ContactUs()
		response = contact_us.get_contacts()
		return response

	@marshal_with(contact_us_fields)
	def post(self):
		args = self.reqparse.parse_args()
		contact_us = ContactUs()
		response = contact_us.add_contact_us_details(db, args)
		return response

		# course = models.Course.create(**args)
		# return (add_reviews(course), 201, {
		# 		'Location': url_for('resources.courses.course', id=course.id)}
		# 		)

contact_us_api = Blueprint('contact', __name__)
api = Api(contact_us_api)
api.add_resource(
    Contact,
    '/api/v1/contact_us',
    endpoint='contact'
)