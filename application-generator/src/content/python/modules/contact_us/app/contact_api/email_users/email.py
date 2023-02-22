# app/contact_api/contact_us.py
import sys
import smtplib

from flask_mail import Message
from flask import jsonify, current_app
from threading import Thread

from sqlalchemy import false
from app import mail
from .i_email import IEmail

class Emails(IEmail):
	
	def send_async_email(self, app, msg):
		with app.app_context():
			mail.send(msg)


	def send_contact_email(self, subject, message_body, email_recipient, message_sender):
		msg = Message(subject, sender=message_sender, recipients=[email_recipient])
		msg.body = message_body
		Thread(target=self.send_async_email,
			args=(current_app._get_current_object(), msg)).start()


	def request_email_sending(self, subject, message_body, email, admin_email):
		error = False
		mail_subject = subject
		message = message_body
		receiver = email
		sender = admin_email
		
		try:
			self.send_contact_email(mail_subject, message, receiver, sender)
		except:
			error = True
			print(sys.exc_info())

		if error:
			response = jsonify({
				'message': 'Error!'
				
			})
		if not error:
			response = jsonify({
				'message': 'Email sent'
			})
		return response

	def index_mail(self):
		msg = Message('Hello from the other side!', sender =   'alexandra@mailtrap.io', recipients = ['paul@mailtrap.io'])
		msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
		mail.send(msg)
		return "Message sent!"