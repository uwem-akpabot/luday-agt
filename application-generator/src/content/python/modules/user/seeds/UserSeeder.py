import os
from flask_seeder import Seeder
from werkzeug.security import generate_password_hash

from app.models import User
import app.constants as k

class UserSeeder(Seeder):

	def run(self):
		args = {
			"first_name": "Super",
			"last_name": "Admin",
			"email": os.environ.get('SUPER_ADMIN_EMAIL'),
			"user_type": k.UserType.SUPER_ADMIN.value,
			"password_harsh": generate_password_hash(os.environ.get('SUPER_ADMIN_PASSWORD')),
			"is_active": True,
			"email_verified": True
		}
		user = User(**args)
		print("Adding user: %s" % user)
		self.db.session.add(user)
		try:
			self.db.session.commit()
		except:
			self.db.session.rollback()
