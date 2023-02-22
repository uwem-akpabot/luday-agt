# app/constants.py
from enum import Enum

class OrderStatus(Enum):
	NEW = "New"
	PAYMENT_PENDING = "Pending"
	PAYMENT_FAILED = "Failed"
	SUCCESS = "Successful"

	def __str__(self):
		return self.value
class DeliveryStatus(Enum):
	PENDING = "Pending"
	SHIPPED = "Shipped"
	DELIVERED = "Delivered"

	def __str__(self):
		return self.value
