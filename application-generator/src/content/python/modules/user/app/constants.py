# app/constants.py
from enum import Enum

class UserType(Enum):
	USER = "user"
	VENDOR = "vendor"
	SUPER_ADMIN = "super-admin"
	SUB_ADMIN = "sub-admin"

	def __str__(self):
		return self.value

class Gender(Enum):
	MALE = "male"
	FEMALE = "female"
	NOT_SPECIFIED = "not-specified"

	def __str__(self):
		return self.value
