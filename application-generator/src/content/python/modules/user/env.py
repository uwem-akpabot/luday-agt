class UserEnv:
 env = {}

 default = """
# .env
APP_NAME="@@AppName@@"
CONFIGURATION_SETUP="@@Config@@"
SECRET_KEY="@@secret_key@@"
ADMIN_EMAIL="@@admin_email@@"
SUPER_ADMIN_EMAIL="@@super_admin_email@@"
SUPER_ADMIN_PASSWORD="@@super_admin_password@@"

DB_SERVER=127.0.0.1
DB_PORT=3306
DB_DATABASE="@@db_name@@"
DB_USERNAME="@@db_user@@"
DB_PASSWORD="@@db_password@@"

CONTACT_US_PROD_API_URL=""
CONTACT_US_DEV_API_URL="http://localhost:5001"

CCESS_TOKEN_MINUTES='15'
REFRESH_TOKEN_DAYS='7'
RESET_TOKEN_MINUTES='15'
REFRESH_TOKEN_IN_COOKIE='no'
REFRESH_TOKEN_IN_BODY='true'
MAIL_USE_TLS='true'
USE_CORS='true'
PASSWORD_RESET_URL="http://localhost:3000/reset_password"

PAYSTACK_SECRET_KEY=""
PAYSTACK_PUBLIC_KEY=""
PAYSTACK_SUBACCOUNT_PERCENTAGE_CHARGE=10
	"""

 env["default"] = default