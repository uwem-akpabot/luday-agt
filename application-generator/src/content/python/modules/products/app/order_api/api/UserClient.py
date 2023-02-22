# app/order_api/api/UserClient.py
import os
import requests


class UserClient:
	@staticmethod
	def get_user(api_key):
		headers = {
			'Authorization': api_key
		}
		environment_configuration = os.environ['CONFIGURATION_SETUP']
		user_prod_api_uri = os.environ['USER_PROD_API_URL']
		user_dev_api_uri = os.environ['USER_DEV_API_URL']
		
		if environment_configuration == 'config.ProductionConfig':
			_url = f'{user_prod_api_uri}/api/user/auth'
		if environment_configuration == 'config.DevelopmentConfig':
			_url = f'{user_dev_api_uri}/api/user/auth'

		# TODO: reduce response time => Python async
		response = requests.request(method="GET", url=_url, headers=headers)
		if response.status_code == 401:
			return False
		user = response.json()
		return user


	@staticmethod
	def get_unauthenticated_user_by_id(user_id):
		environment_configuration = os.environ['CONFIGURATION_SETUP']
		user_prod_api_uri = os.environ['USER_PROD_API_URL']
		user_dev_api_uri = os.environ['USER_DEV_API_URL']
		
		if environment_configuration == 'config.ProductionConfig':
			_url = f'{user_prod_api_uri}/api/unauth/user?id={user_id}'
		if environment_configuration == 'config.DevelopmentConfig':
			_url = f'{user_dev_api_uri}/api/unauth/user?id={user_id}'

		# TODO: reduce response time => Python async
		response = requests.request(method="GET", url=_url)
		if response.status_code == 401:
			return False
		user = response.json()
		return user

	
	@staticmethod
	def get_vendor_by_id(vendor_id):
		headers = {
			'Accept': '*/*'
		}
		environment_configuration = os.environ['CONFIGURATION_SETUP']
		user_prod_api_uri = os.environ['USER_PROD_API_URL']
		user_dev_api_uri = os.environ['USER_DEV_API_URL']

		if environment_configuration == 'config.ProductionConfig':
			_url = f'{user_prod_api_uri}/api/user/vendor?id={vendor_id}'
		if environment_configuration == 'config.DevelopmentConfig':
			_url = f'{user_dev_api_uri}/api/user/vendor?id={vendor_id}'

		# TODO: reduce response time => Python async
		response = requests.request(method="GET", url=_url, headers=headers)
		if response.status_code == 401 or response.status_code == 404:
			return False
		user = response.json()
		return user