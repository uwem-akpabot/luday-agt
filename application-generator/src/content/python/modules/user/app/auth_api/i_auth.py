# app/auth_api/i_auth.py
from abc import ABC, abstractmethod

class IAuthentication(ABC):
	@abstractmethod
	def verify_password(self):
		""" Verify password.
		Must be implemented.
		"""
		raise NotImplementedError()

	@abstractmethod
	def basic_auth_error(self):
		""" Basic authentication error.
		Must be implemented.
		"""
		raise NotImplementedError()

	@abstractmethod
	def verify_token(self):
		""" Verify token.
		Must be implemented.
		"""
		raise NotImplementedError()

	@abstractmethod
	def token_auth_error(self):
		""" Token authentication error.
		Must be implemented.
		"""
		raise NotImplementedError()