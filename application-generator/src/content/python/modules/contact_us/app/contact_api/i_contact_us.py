# app/contact_api/i_contact_us.py
from abc import ABC, abstractmethod

class IConactUs(ABC):
	@abstractmethod
	def add_contact_us_details(self, _db):
		pass

	@abstractmethod
	def get_contacts(self):
		pass

	def send_async_email(self, app, msg):
		pass

	def send_email(self, subject, message_body, message_sender, email_recipient):
		pass