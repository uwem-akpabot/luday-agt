# app/auth_api/auth.py
from flask_mail import Message
from flask import request, jsonify, current_app
from threading import Thread

from flask import current_app
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from werkzeug.exceptions import Unauthorized, Forbidden

from app import db, constants as k
from app.auth_api.i_auth import IAuthentication
from app.models import User

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()
class Authentication(IAuthentication):

	@basic_auth.verify_password
	def verify_password(email, password):
		if email and password:
			user = db.session.scalar(User.query.filter_by(email=email))
			if user and user.verify_password(password):
				return user


	@basic_auth.error_handler
	def basic_auth_error(status=401):
		error = (Forbidden if status == 403 else Unauthorized)()
		return {
			'code': error.code,
			'message': error.name,	
			'description': error.description,
		}, error.code, {'WWW-Authenticate': 'Form'}


	@token_auth.verify_token
	def verify_token(access_token):
		if current_app.config['DISABLE_AUTH']:
			user = db.session.get(User, 1)
			user.ping()
			return user
		if access_token:
			return User.verify_access_token(access_token)


	@token_auth.error_handler
	def token_auth_error(status=401):
		error = (Forbidden if status == 403 else Unauthorized)()
		return {
			'code': error.code,
			'message': error.name,
			'description': error.description,
		}, error.code
