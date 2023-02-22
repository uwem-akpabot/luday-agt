# app/contact_api/contact_us.py
import os, sys
import smtplib

from flask import request, jsonify, current_app

from sqlalchemy import false
from app import mail

from ..models import ContactUsModel
from .i_contact_us import IConactUs
from .email_users.email import Emails

_email = Emails()

class ContactUs(IConactUs):

	def add_contact_us_details(self, _db):
		name = request.json['name']
		subject = request.json['subject']
		email = request.json['email']
		mobile = request.json['mobile']
		mssg = request.json['mssg']
		admin_email = os.environ.get('ADMIN_EMAIL')
		error = False

		try:	
			contact = ContactUsModel()
			contact.email = email
			contact.name = name
			contact.subject = subject
			contact.mobile = mobile
			contact.mssg = mssg

			subject = 'Bestdealnaija contact request'
			message_body = 'New contact request visit bestdeal admin dashboard to see details'
			_db.session.add(contact)
			_db.session.commit()	

			_email.send_contact_email(subject, message_body, email, admin_email)
		
		except:
			error = True
			_db.session.rollback()
			print(sys.exc_info())

		if error:
			response = jsonify({
				'message': 'Error!', 
				'result': contact.to_json()
			})
		if not error:
			response = jsonify({
				'message': 'Contact added', 
				'result': contact.to_json()
			})
		return response


	def get_contacts(self):
		items = []
		for row in ContactUsModel.query.all():
			items.append(row.to_json())

		response = jsonify({'results': items})
		return response