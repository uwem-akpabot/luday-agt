# app/order_api/i_order.py
from abc import ABC, abstractmethod

class IOrder(ABC):
	@abstractmethod
	def add_order(self, _db):
		pass

	@abstractmethod
	def add_guest_order(self, _db):
		pass

	@abstractmethod
	def get_order_by_id_or_404(self, _db):
		pass
	