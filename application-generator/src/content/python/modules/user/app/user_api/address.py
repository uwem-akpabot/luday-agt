# app/user_api/address.py
from app.models import Address as AddressModel
from app import db
from app.user_api.i_address import IAddress
from flask import jsonify

class Address(IAddress):
	def add_user_address(self, args):
		address = AddressModel(**args)
		db.session.add(address)
		db.session.commit()

		address.ref_address_id = address.id
		db.session.add(address)
		db.session.commit()
		return address

	
	def get_address_by_user_id(self, user_id):
		return db.session.scalar(AddressModel.query
			.filter(AddressModel.user_id==user_id))

	def get_address_by_address_id(self, _id):
		
		query = AddressModel.query.filter_by(id=_id).first()
		data = jsonify({
			"street": query.address,
			"lga": query.ref_local_govt,
			"postal_code": query.postal_code,
			"ref_state": query.ref_state
			})
		return  data

	
	def get_address_by_email(self, email):
		return db.session.scalar(AddressModel.query
			.filter(AddressModel.email==email))


	def update_address_by_guest(self, guest, args):
		addressModel = AddressModel.query.get(guest.id)
		addressModel.address = args['address']
		addressModel.ref_local_govt = args['ref_local_govt']
		addressModel.ref_state = args['ref_state']
		addressModel.email = args['email']

		db.session.add(addressModel)
		db.session.commit()
		return addressModel

	
	def update_address_by_user(self, user, args):
		addressModel = AddressModel.query.get(user.id)
		addressModel.address = args['address']
		addressModel.ref_local_govt = args['ref_local_govt']
		addressModel.ref_state = args['ref_state']
		addressModel.email = args['email']

		db.session.add(addressModel)
		db.session.commit()
		return addressModel
