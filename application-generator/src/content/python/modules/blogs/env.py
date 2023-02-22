class BlogsEnv:
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

# mail config
MAIL_PORT=2525
MAIL_SERVER='smtp.mailtrap.io'
MAIL_USERNAME=''
MAIL_PASSWORD=''
MAIL_FROM_ADDRESS=NOREPLY@bestdealnaija.com
MAIL_FROM_NAME="${APP_NAME}"

USER_PROD_API_URL=""
USER_DEV_API_URL="http://localhost:5002"
PASSWORD_RESET_URL="http://localhost:3000/reset"
	"""

 env["default"] = default