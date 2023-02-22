class ContactUsEnv:
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
MAIL_SERVER='@@MailServer@@'
MAIL_USERNAME='@@MailUsername@@'
MAIL_PASSWORD='@@MailPassword@@'
MAIL_USE_TLS='true'
MAIL_DEFAULT_SENDER='@@MailDefaultSender@@'
	"""

 env["default"] = default