# app/product_api/api/VendorClient.py
import os
import requests


class VendorClient:
	@staticmethod
	def get_vendor_by_user_id(user_id):
		
		environment_configuration = os.environ['CONFIGURATION_SETUP']
		user_prod_api_uri = os.environ['USER_PROD_API_URL']
		user_dev_api_uri = os.environ['USER_DEV_API_URL']
		
		if environment_configuration == 'config.ProductionConfig':
			_url = f'{user_prod_api_uri}/api/user/vendor?user_id={user_id}'

		if environment_configuration == 'config.DevelopmentConfig':
			_url = f'{user_dev_api_uri}/api/user/vendor?user_id={user_id}'

		# TODO: reduce response time => Python async
		response = requests.request(method="GET", url=_url)
		if response.status_code == 401:
			return False

		vendors = response.json()
		return vendors
