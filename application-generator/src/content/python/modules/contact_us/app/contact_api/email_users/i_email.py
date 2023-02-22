# app/contact_api/email/i_email.py
from abc import ABC, abstractmethod

class IEmail(ABC):
	@abstractmethod
	def send_async_email(self):
		pass

	@abstractmethod
	def send_contact_email(self, subject, message_body, message_sender, email_recipient):
		pass


	