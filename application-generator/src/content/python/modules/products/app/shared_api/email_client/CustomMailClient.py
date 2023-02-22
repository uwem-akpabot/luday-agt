
import os
import requests
import json


class CustomMailClient:
    @staticmethod
    def send_email_to_users(body):
        headers = {
            'content-type': 'application/json'
        }
        body = body

        environment_configuration = os.environ['CONFIGURATION_SETUP']
        contact_us_prod_api_uri = os.environ['EMAIL_PROD_API_URL']
        contact_us_dev_api_uri = os.environ['EMAIL_DEV_API_URL']

        if environment_configuration == 'config.ProductionConfig':
            _url = F'{contact_us_prod_api_uri}/api/email/send'
        if environment_configuration == 'config.DevelopmentConfig':
            _url = F'{contact_us_dev_api_uri}/api/email/send'

        # TODO: reduce response time => Python async
        response = requests.post(url=_url, headers=headers, json=body)
        if response.status_code == 401:
            return False
        messsage = response.json()
        return messsage
