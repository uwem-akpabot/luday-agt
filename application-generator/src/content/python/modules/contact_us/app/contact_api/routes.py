# app/contact_api/routes.py
from flask import request
import os
from apifairy import body, response
from flask_restful import reqparse

from app import db, moment
from app.contact_api import contact_api_blueprint
from app.contact_api.contact_us import ContactUs
from app.contact_api.email_users.email import Emails
from app.contact_api.email_users.custom_mail import CustomMail
from app.schemas import EmptySchema, CustomMailSchema

parser = reqparse.RequestParser(bundle_errors=True)
_email = Emails()

custom_mail = CustomMail()
empty_schema = EmptySchema()
custom_mail_schema = CustomMailSchema()


@contact_api_blueprint.route('/api/contact/add', methods=['POST'])
def add_contact_us_details():
    try:
        parser.add_argument('name',
                            type=str,
                            required=True,
                            help="Name field cannot be left blank!"
                            )
        parser.add_argument('subject',
                            type=str,
                            required=True,
                            help="Subject field cannot be left blank!"
                            )
        parser.add_argument('email',
                            type=str,
                            required=True,
                            help="Email field cannot be left blank!"
                            )
        parser.add_argument('mobile',
                            type=str,
                            required=True,
                            help="Mobile field cannot be left blank!"
                            )
        parser.add_argument('mssg',
                            type=str,
                            required=True,
                            help="Message field cannot be left blank!"
                            )
        args = parser.parse_args(strict=True)

        contact_us = ContactUs()
        response = contact_us.add_contact_us_details(db)
        return response

    except Exception as e:
            return {
                'message' : str(e)
            }, 400

@contact_api_blueprint.route('/api/contact', methods=['GET'])
def get_contacts():
    contact_us = ContactUs()
    response = contact_us.get_contacts()
    return response


# To be used to send mail inplace of route:/api/contact/sendemail
@contact_api_blueprint.route('/api/contact/send-email', methods=['POST'])
@body(custom_mail_schema)
@response(custom_mail_schema, description='Email sent')
def custom_send_email(args):
    to = args['to']
    subject = args['subject']
    template = args['template']

    response = custom_mail.send_email(
            to, subject, template, 
            token=args['kwargs']['token'], 
            url=args['kwargs']['url'], 
            first_name=args['kwargs']['first_name']
        )
    return response


@contact_api_blueprint.route('/api/contact/sendemail', methods=['POST'])
def Send_email():
  
    # response = _email.index_mail()
    # return response
    subject = request.json['subject']
    message_body = request.json['msg']
    email = request.json['email']
    admin_email = os.environ.get('ADMIN_EMAIL')
    response = _email.request_email_sending(subject, message_body, email, admin_email)
    return response
