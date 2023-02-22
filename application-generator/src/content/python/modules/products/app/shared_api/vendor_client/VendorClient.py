# app/order_api/api/UserClient.py
import os
import requests


class VendorClient:
	@staticmethod
	def get_user(_id):
		
		environment_configuration = os.environ['CONFIGURATION_SETUP']
		user_prod_api_uri = os.environ['USER_PROD_API_URL']
		user_dev_api_uri = os.environ['USER_DEV_API_URL']

		if environment_configuration == 'config.ProductionConfig':
			_url = f'{user_prod_api_uri}/api/user/vendors/{_id}/vendor'
		if environment_configuration == 'config.DevelopmentConfig':
			_url = f'{user_dev_api_uri}/api/user/vendors/{_id}/vendor'

		# TODO: reduce response time => Python async
		response = requests.request(method="GET", url=_url)
		if response.status_code == 401:
			return False
		vendors = response.json()
		return vendors

	@staticmethod
	def get_vendor_by_id(vendor_id):
		
		environment_configuration = os.environ['CONFIGURATION_SETUP']
		user_prod_api_uri = os.environ['USER_PROD_API_URL']
		user_dev_api_uri = os.environ['USER_DEV_API_URL']
		
		if environment_configuration == 'config.ProductionConfig':
			_url = f'{user_prod_api_uri}/api/user/vendor?id={vendor_id}'

		if environment_configuration == 'config.DevelopmentConfig':
			_url = f'{user_dev_api_uri}/api/user/vendor?id={vendor_id}'

		# TODO: reduce response time => Python async
		response = requests.request(method="GET", url=_url)
		if response.status_code == 401:
			return False

		vendors = response.json()
		return vendors

	@staticmethod
	def get_vendor_details_by_user_id(user_id):
		
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


class VendorAddressClient:
	@staticmethod
	def get_user_address(_id):
		
		environment_configuration = os.environ['CONFIGURATION_SETUP']
		user_prod_api_uri = os.environ['USER_PROD_API_URL']
		user_dev_api_uri = os.environ['USER_DEV_API_URL']

		if environment_configuration == 'config.ProductionConfig':
			_url = f'{user_prod_api_uri}/api/user/deliveryaddress/{_id}'
		if environment_configuration == 'config.DevelopmentConfig':
			_url = f'{user_dev_api_uri}/api/user/deliveryaddress/{_id}'

		# TODO: reduce response time => Python async
		response = requests.request(method="GET", url=_url)
		if response.status_code == 401:
			return False
		delivery_address = response.json()
		return delivery_address