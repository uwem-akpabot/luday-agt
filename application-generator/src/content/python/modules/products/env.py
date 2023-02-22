class ProductsEnv:
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

USER_PROD_API_URL=""
USER_DEV_API_URL="http://localhost:5002"

CONTACT_US_PROD_API_URL=""
CONTACT_US_DEV_API_URL="http://localhost:5001"

PASSWORD_RESET_URL="http://localhost:3000/reset"
USE_CORS='true'

PAYSTACK_SECRET_KEY=""
PAYSTACK_PUBLIC_KEY=""
PAYSTACK_SUBACCOUNT_PERCENTAGE_CHARGE=10

POSTS_PER_PAGE=10
	"""

 env["default"] = default
