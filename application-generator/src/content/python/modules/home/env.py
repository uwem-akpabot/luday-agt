class HomeEnv:
 env = {}

 default = """
# .env
APP_NAME="@@AppName@@"
CONFIGURATION_SETUP="@@Config@@"
SECRET_KEY="@@secret_key@@"
	"""

 env["default"] = default