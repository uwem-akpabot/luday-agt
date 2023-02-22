# app/user_api/vendor.py
from pickle import TRUE
from flask import jsonify, abort, request

from app.models import Vendors as VendorModel
from app.models import User as UserModel
from app import db
from app.user_api.i_user import IUser
from config import ROOT_DIR, vendor_upload_folder
from werkzeug.utils import secure_filename
import os
import re
from .api.CustomMailClient import CustomMailClient

_custom_mail = CustomMailClient()

class Vendor(IUser):

	def get_user_by_id_or_404(self, id):
		return db.session.get(VendorModel, id) or abort(404)


	def get_user_by_email_or_404(self, id):
		return self.get_user_by_id_or_404(id)


	def get_user_by_user_id(self, user_id):
		return VendorModel.query.filter_by(user_id=user_id).first()

	def get_vendors_uset_details_by_user_id(self, user_id):
		return UserModel.query.filter_by(id=user_id).first()
	

	def get_users(self):
		data = []
		for row in VendorModel.query\
			.all():
			data.append(row.to_dict(True))

		response = jsonify(data)
		return response


	def allowed_file(self, filename, allowed_extensions):
		return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions


	def get_business_image_path(self):
		image_file = request.files.get('image_file')
		name = request.form.get('name')
		allowed_extensions = {'webp', 'png', 'jpg', 'jpeg'}
		if image_file:
			if self.allowed_file(image_file.filename, allowed_extensions):
				filename = secure_filename(name + '.' + image_file.filename.rsplit('.',1)[1])
				image_file.save(os.path.join(vendor_upload_folder, filename))

				business_image_path = 'images/vendors/'+filename
				return business_image_path
		abort(400)


	def add_or_update_vendor(self, args):
		user_id = args['user_id']
		user = self.get_user_by_user_id(user_id)
		vendor_user_details = self.get_vendors_uset_details_by_user_id(user_id)
		business_image_path = self.get_business_image_path()
		slug = args['name'].strip()

		if user:
			vendor = user
		else:
			vendor = VendorModel()
			mailmessage = {
				"subject" : "Vendor account created",
				"business_name": args['name'],
				"first_name" : vendor_user_details.first_name,
				"email" : vendor_user_details.email,
				"template" : "vendorCreated"
			}
			_custom_mail.send_email_to_users(mailmessage)
		
		vendor.user_id = args['user_id']
		vendor.name = args['name']
		vendor.business_description = args['business_description']
		vendor.slug = re.sub('\s+', '-', slug)
		vendor.business_bank_name = args['business_bank_name']
		vendor.business_bank_name_value = args['business_bank_name_value']
		vendor.business_account_no = args['business_account_no']
		vendor.business_account_name = args['business_account_name']
		vendor.business_address = args['business_address']
		vendor.business_city = args['business_city']
		vendor.business_state = args['business_state']
		vendor.business_state_value = args['business_state_value']
		vendor.business_image_path = business_image_path

		if not user:
			db.session.add(vendor)
		db.session.commit()
		return vendor


	def add_user(self, args):
		self.add_or_update_vendor(args)

	
	def update_vendor_subaccount_details(self, vendor_id, args):
		vendor = self.get_user_by_id_or_404(vendor_id)
		vendor.business_subaccount_code = args['subaccount_code']
		vendor.business_percentage_charge = args['percentage_charge']
		db.session.commit()

		return vendor
