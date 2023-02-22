# app/user_api/i_user.py
from abc import ABC, abstractmethod

class IUser(ABC):
	@abstractmethod
	def get_users(self):
		pass


	@abstractmethod
	def add_user(self):
		pass


	@abstractmethod
	def get_user_by_id_or_404(self):
		pass


	def get_user_by_email_or_404(self):
		pass