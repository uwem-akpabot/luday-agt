# app/user_api/i_user.py
from abc import ABC, abstractmethod

class IAddress(ABC):
	@abstractmethod
	def add_user_address(self):
		pass

	@abstractmethod
	def update_address_by_guest(self):
		pass


	@abstractmethod
	def update_address_by_user(self):
		pass