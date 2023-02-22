# app/user_api/user.py
from flask import jsonify, current_app, abort, request
from werkzeug.utils import secure_filename
import sys, os
import re

from config import ROOT_DIR, vendor_upload_folder
from app import db
from app.models import User as UserModel
from app.models import Vendors as VendorModel
import app.user_api.routes as helper
from app.user_api.i_user import IUser
from app.constants import UserType
from .api.CustomMailClient import CustomMailClient

_custom_mail = CustomMailClient()
class User(IUser):

	def get_user_by_id_or_404(self, id):
		return db.session.get(UserModel, id) or abort(404)


	def get_user_by_email_or_404(self, email):
		return db.session.scalar(UserModel.query
			.filter(UserModel.email==email)) or \
        	abort(404)
	

	def get_users(self):
		data = []
		for row in UserModel.query\
			.filter_by(user_type=UserType.USER.value)\
					.all():
			data.append(row.to_dict(True))

		response = jsonify(data)
		return response

	
	def get_sub_admin(self):
		data = []
		for row in UserModel.query\
			.filter_by(user_type=UserType.SUB_ADMIN.value)\
				.all():
			data.append(row.to_dict(True))

		response = jsonify(data)
		return response


	def add_user(self, args):
		user = UserModel(**args)
		db.session.add(user)
		db.session.commit()

		if args['user_type'] == UserType.SUB_ADMIN.value:
			#send a mail to the created sub admin
			message = {
				"subject":"You have been added as Admin on BestDealNaija",
				"user_name": f"{args['email']}",
				"password": f"{args['password']}",
				"first_name": f"{args['first_name']}",
				"email": args['email'],
				"template": "subAccountCreated"
			}
		else:
			message = {
				"subject":"Welcome to BestDealNaija",
				"first_name": f"{args['first_name']}",
				"email": args['email'],
				"template": "accountCreated"
			}
		_custom_mail.send_email_to_users(message)

		return user


	def update_authenticated_user(self, user, data):
		user.update(data)
		db.session.commit()
		return user
	

	def allowed_file(self, filename, allowed_extensions):
		return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

	def add_vendors(self, _db):
		v_first_name = request.form.get('vendor_first_name')
		v_last_name = request.form.get('vendor_last_name')
		v_gender = request.form.get('vendor_gender')
		v_email = request.form.get('vendor_email')
		v_mobile_number = request.form.get('vendor_phone')
		v_password = 'V_password'
		v_user_type = UserType.VENDOR.value
		v_is_active = True
		vendor_img = request.files.get('vendor_image')
		business_name = request.form.get('vendor_business_name').strip()
		business_description = request.form.get('vendor_Description')
		slugify = re.sub('\s+', '-', business_name)
		v_business_bank = request.form.get('vendor_Bank')
		v_business_bank_value = request.form.get('vendor_Bank_value')
		v_business_account_no = request.form.get('vendor_account_number')
		v_business_account_name = request.form.get('vendor_account_name')
		v_business_address = request.form.get('vendor_address')
		v_business_state = request.form.get('vendor_state')
		v_business_state_value = request.form.get('vendor_state_value')
		v_business_city = request.form.get('vendor_city')
		allowed_extensions = {'webp', 'png', 'jpg', 'jpeg'}

		check_businessname = VendorModel.query.with_entities(VendorModel.name).filter(VendorModel.name == business_name).first()
		error = False
		if not vendor_img:
			error = True
			message = 'At least one image is required for Vendor'
		else:
			if check_businessname:
				message = 'bussiness name already exist'
				error = True
			else:	
				if self.allowed_file(vendor_img.filename, allowed_extensions):
					filename = secure_filename(business_name + '.' + vendor_img.filename.rsplit('.',1)[1])
					vendor_img.save(os.path.join(vendor_upload_folder, filename))
					try:
						user = UserModel()
						user.first_name = v_first_name
						user.last_name = v_last_name
						user.gender = v_gender
						user.email = v_email
						user.mobile_number = v_mobile_number
						user.password = v_password
						user.user_type = v_user_type
						user.is_active = v_is_active
						_db.session.add(user)
						_db.session.flush()
						v_user_id = user.id
						vendor_mapping = VendorModel()
						vendor_mapping.user_id = v_user_id
						vendor_mapping.name = business_name
						vendor_mapping.business_description = business_description
						vendor_mapping.slug = slugify
						vendor_mapping.business_bank_name = v_business_bank
						vendor_mapping.business_bank_name_value = v_business_bank_value
						vendor_mapping.business_account_no = v_business_account_no
						vendor_mapping.business_account_name = v_business_account_name
						vendor_mapping.business_address = v_business_address
						vendor_mapping.business_city = v_business_city
						vendor_mapping.business_state = v_business_state
						vendor_mapping.business_state_value = v_business_state_value
						vendor_mapping.business_image_path = 'images/vendors/'+filename
						#vendor_mapping.slug = business_name.replace(" ", "-")
						_db.session.add(vendor_mapping)
						_db.session.commit()

						# Create vendor subaccount code
						helper.update_vendor_subaccount_details(vendor_mapping)
						
						#send mail to vendor
						mailmessage = {
							"subject" : "Vendor account created",
							"business_name": f"{business_name}",
							"first_name" : f"{v_first_name}",
							"email" : f"{v_email}",
							"template" : "vendorCreated"
						}
						_custom_mail.send_email_to_users(mailmessage)
						
						
						message = 'Vendor added successfully'

					except:
						error = True
						_db.session.rollback()
						print(sys.exc_info())
						message = 'An error occured'
				else:
					error = True
					message = 'Image filetype not valid'
		if error:
			return jsonify({
				'message': message, 
				'result': ''
			})
		if not error:
			return jsonify({
				'message': message, 
				'result': user.to_dict()
			})
		return False

	def get_vendors(self, _db):
		vendors = []
		query = db.session.query(
						VendorModel.id, 
						UserModel.first_name, UserModel.last_name, 
						UserModel.email, UserModel.mobile_number, 
						VendorModel.slug, VendorModel.business_image_path, 
						VendorModel.name, VendorModel.created_at, 
						VendorModel.business_description, VendorModel.business_address, 
						VendorModel.business_state, VendorModel.business_city, 
						VendorModel.user_id, UserModel.is_active
					)\
					.filter(VendorModel.user_id == UserModel.id)\
					.order_by(VendorModel.id.desc())\
					.all()
		
		for vendor in query:
			vendors.append({
			"vendor_id": vendor[0],
			"first_name":vendor[1],
			"last_name": vendor[2],
			"email": vendor[3],
			"phone": vendor[4],
			"slug": vendor[5],
			"image": vendor[6],
			"business_name": vendor[7],
			"join": vendor[8],
			"business_description": vendor[9],
			"business_address": vendor[10],
			"business_state": vendor[11],
			"business_city": vendor[12],
			"user_id": vendor[13],
			"status": vendor[14]
		})
		response = jsonify({'results': vendors})
		return response

	def edit_vendor(self, _db, vendor_id, slug):
		vendor = VendorModel.query.filter_by(id=vendor_id).first()
		business_image_path = vendor.business_image_path
		
		error = False
		if vendor:
			vendor_img = request.files.get('vendor_image')
			business_name = request.form.get('vendor_business_name').strip()
			business_description = request.form.get('vendor_Description')
			business_address = request.form.get('vendor_address')
			business_state = request.form.get('vendor_state')
			business_state_code = request.form.get('vendor_state_code')
			business_city = request.form.get('vendor_city')
			business_bank = request.form.get('vendor_Bank')
			business_account_nunber = request.form.get('vendor_account_number')
			business_account_name = request.form.get('vendor_account_name')
			slugify = re.sub('\s+', '-', business_name)
			allowed_extensions = {'webp', 'png', 'jpg', 'jpeg'}

			if vendor_img:
				if self.allowed_file(vendor_img.filename, allowed_extensions):
					filename = secure_filename(secure_filename(business_name + '.' + vendor_img.filename.rsplit('.',1)[1]))
					vendor_img.save(os.path.join(vendor_upload_folder, filename))
					
					business_image_path = 'images/vendors/'+filename
				else:
					error = True
					message = 'Invalid image file type'
			try:
				vendor.name = business_name
				vendor.business_description = business_description
				vendor.business_address = business_address
				vendor.business_state = business_state
				vendor.business_state_value = business_state_code
				vendor.business_city = business_city
				vendor.business_bank_name = business_bank
				vendor.business_account_name = business_account_name
				vendor.business_account_no = business_account_nunber
				vendor.business_image_path = business_image_path
				vendor.slug = slugify
				_db.session.add(vendor)
				_db.session.commit()

				message = 'Vendor updated successfully'
			except:
				error = True
				_db.session.rollback()
				print(sys.exc_info())
				message = 'An error occured please try again'
		if error:
			response = jsonify({
				'message': message,
				'result': ''
			})
		if not error:
			response = jsonify({
				'message': message,
				'result': vendor.to_json()
			})
		return response

	def get_single_vendors(self, vendor_id, slug):
		vendor = []
		query = db.session.query(
				VendorModel.id, UserModel.first_name, UserModel.last_name, UserModel.email, 
				UserModel.mobile_number, VendorModel.slug, VendorModel.business_image_path,
				VendorModel.name, VendorModel.created_at, VendorModel.business_description, 
				VendorModel.business_address, VendorModel.business_state, VendorModel.business_city, 
				VendorModel.business_bank_name, VendorModel.business_account_name, 
				VendorModel.business_account_no, VendorModel.business_bank_name_value, 
				VendorModel.business_state_value, VendorModel.user_id, UserModel.is_active
			)\
				.filter(
					VendorModel.user_id == UserModel.id,
					VendorModel.id == vendor_id, 
					UserModel.user_type == UserType.VENDOR.value
				)	

		if not query:
			message = 'Vendor does not exist'
			vendor = ''
		else:
			for the_vendor in query:
				vendor.append({
				"vendo_id": the_vendor[0],
				"first_name":the_vendor[1],
				"last_name": the_vendor[2],
				"email": the_vendor[3],
				"phone": the_vendor[4],
				"slug": the_vendor[5],
				"image": the_vendor[6],
				"business_name": the_vendor[7],
				"join": the_vendor[8],
				"business_description": the_vendor[9],
				"business_address": the_vendor[10],
				"business_state": the_vendor[11],
				"business_city": the_vendor[12],
				"business_bank": the_vendor[13],
				"business_account_name": the_vendor[14],
				"business_account_no": the_vendor[15],
				"business_bank_value": the_vendor[16],
				"business_state_value": the_vendor[17],
				"user_id": the_vendor[18],
				"status": the_vendor[19]
			})
			message = 'Success'
		response = jsonify({'vendor': vendor, 'message': message })
		return response

	def get_single_vendor_by_slug(self, _db, slug):
		vendor = []
		query = db.session.query(
				VendorModel.id, UserModel.first_name, UserModel.last_name, UserModel.email, 
				UserModel.mobile_number, VendorModel.slug, VendorModel.business_image_path, 
				VendorModel.name, VendorModel.created_at, VendorModel.business_description, 
				VendorModel.business_address, VendorModel.business_state, VendorModel.business_city, 
				VendorModel.business_bank_name, VendorModel.business_account_name, 
				VendorModel.business_account_no, VendorModel.user_id
			)\
				.filter(VendorModel.user_id == UserModel.id, VendorModel.slug == slug)
		print(query)
		
		if not query:
			message = 'Vendor does not exist'
			vendor = ''
		else:
			for the_vendor in query:
				vendor.append({
				"id": the_vendor[0],
				"first_name":the_vendor[1],
				"last_name": the_vendor[2],
				"email": the_vendor[3],
				"phone": the_vendor[4],
				"slug": the_vendor[5],
				"image": the_vendor[6],
				"business_name": the_vendor[7],
				"join": the_vendor[8],
				"business_description": the_vendor[9],
				"business_address": the_vendor[10],
				"business_state": the_vendor[11],
				"business_city": the_vendor[12],
				"business_bank": the_vendor[13],
				"business_account_no": the_vendor[14],
				"business_account_name": the_vendor[15],
				"vendor_id": the_vendor[16]
			})
			message = 'Success'
		response = jsonify({'vendor': vendor, 'message': message })
		return response
	
	def delete_vendor(self, _db, vendor_id, slug):
		#this only deletes the vendors business details. the vendor is not deleted from the user table.
		vendor = VendorModel.query.get(vendor_id)
		error = False
		if vendor:
			_db.session.delete(vendor)
			_db.session.commit()
			message = 'Vendor successfully deleted'	
		else:
			error = True
			message = 'Vendor does not exist'			
		response = jsonify({
			'message': message, 
			'result': vendor_id
		})
		return response

	def verify_vendor(self, _db, user_id):
		vendor = UserModel.query.filter_by(id=user_id).first()
		vendor_details = VendorModel.query.filter_by(user_id = user_id).first()
		error = False
		if not vendor:
			message = 'Vendor does not exist'
		if vendor:
			try:
				vendor.is_active = True
				_db.session.add(vendor)
				_db.session.commit()

				_mail = {
					"subject":"Vendor account approved",
					"first_name" : f"{vendor.first_name}",
					"template" : "vendorApproved",
					"email": f"{vendor.email}",
					"business_name": f"{vendor_details.name}",
					"business_slug": f"{vendor_details.slug}"
				}
				_custom_mail.send_email_to_users(_mail)

				message = 'Vendor verified'
			except:
				error = True
				_db.session.rollback()
				print(sys.exc_info())
				message = 'An error occurred please try again'
			
		if error:
			response = jsonify({
				'message': message,
				'result': ''
			})
		if not error:
			response = jsonify({
				'message': message
			})
		return response

	def unverify_vendor(self, _db, user_id):
		vendor = UserModel.query.get(user_id)
		vendor_details = VendorModel.query.filter_by(user_id = user_id).first()
		error = False
		if not vendor:
			message = 'Vendor does not exist'
		if vendor:
			try:
				vendor.is_active = 0
				_db.session.add(vendor)
				_db.session.commit()
				_mail = {
					"subject":"Vendor account suspended",
					"first_name" : f"{vendor.first_name}",
					"template" : "unListVendor",
					"business_name": f"{vendor_details.name}",
					"email": f"{vendor.email}"
				}
				_custom_mail.send_email_to_users(_mail)

				message = 'Vendor unverified'
			except:
				error = True
				_db.session.rollback()
				print(sys.exc_info())
				message = 'An error occurred please try again'
		if error:
			response = jsonify({
				'message': message,
				'result': ''
			})
		if not error:
			response = jsonify({
				'message': message
			})
		return response


	def get_unverified_vendors(self):
		return UserModel.query\
					.filter_by(user_type=UserType.VENDOR.value)\
					.filter_by(is_active=0)\
					.filter(VendorModel.user_id == UserModel.id)\
					.all()


	def verify_all_vendors(self, _db):
		vendors = self.get_unverified_vendors()
		error = False
		if not vendors:
			message = 'No unverified vendor found'
		if vendors:
			for vendor in vendors:
				try:
					vendor.is_active = True
					_db.session.add(vendor)
					_db.session.commit()
					message = 'All vendors verified'
				except:
					error = True
					_db.session.rollback()
					print(sys.exc_info())
					message = 'An error occurred please try again'
		if error:
			response = jsonify({
				'message': message,
			})
		if not error:
			response = jsonify({
				'message': message,
			})
		return response

	def delete_admin(self, _db, id):
		user = UserModel.query.get(id)
		if user:
			_db.session.delete(user)
			_db.session.commit()
			message = 'Admin successfully deleted'	
		else:
			message = 'Admin does not exist'			
		response = jsonify({
			'message': message, 
			'result': id
		})
		return response

	def edit_admin(self, _db, _id):
		admin = UserModel.query.filter(UserModel.id==_id, UserModel.user_type == request.json.get('user_type')).first()
		first_name = request.json.get('first_name')
		last_name = request.json.get('last_name')
		mobile_number = request.json.get('mobile_number')
		email = request.json.get('email')
		user_type = request.json.get('user_type')
		error = False
		message = "Admin doesnt exist"

		if admin:	
			
			try:
				admin.first_name = first_name
				admin.last_name = last_name
				admin.mobile_number = mobile_number
				admin.email = email
				admin.user_type = user_type
				
				_db.session.add(admin)
				_db.session.commit()

				message = 'Admin updated successfully'
			except Exception as e:
				error = True
				# _db.session.rollback()
				# print(sys.exc_info())
				message = f'<p>{e} </p>'

		if error:
			response = jsonify({
				'message': message,
				'result': ''
			})
		if not error:
			response = jsonify({
				'message': message
			})
		return response