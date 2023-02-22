# app/user_api/api/PaystackClient.py
import os
import requests


class PaystackClient:
	@staticmethod
	def create_subaccount(_data):
		paystack_secret_key = os.environ['PAYSTACK_SECRET_KEY']
		_url = 'https://api.paystack.co/subaccount'
		headers = {
			'Authorization': 'Bearer '+paystack_secret_key
		}

		try:
			response =  requests.request(
								method="POST", url=_url, 
								headers=headers, data=_data)
			user = response.json()
			if not user['status']:
				return False		
			return user['data']
		except requests.exceptions.ConnectionError:
			print("Site not reachable")