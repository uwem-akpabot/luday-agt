# app/order_api/api/PaystackClient.py
import os
import requests


class PaystackClient:
	@staticmethod
	def create_transaction_split(_data):
		paystack_secret_key = os.environ['PAYSTACK_SECRET_KEY']
		_url = 'https://api.paystack.co/split'
		headers = {
			'Authorization': 'Bearer '+paystack_secret_key,
			'Content-Type': 'application/json',
			'Accept': '*/*',
		}

		response =  requests.request(
							method="POST", url=_url, 
							headers=headers, json=_data)
		split = response.json()
		if not split['status']:
			return False		
		return split['data']