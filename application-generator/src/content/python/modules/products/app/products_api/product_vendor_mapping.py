import sys
from flask import abort,jsonify

from app import db
from ..models import (
	ProductVendorMappingModel
) 

class ProductVendorMapping():

	def get_product_vendor_mapping_by_id_or_404(self, id):
		return db.session.get(ProductVendorMappingModel, id) or abort(404)

	
	def get_product_vendor_mapping_by_product_id_or_404(self, product_id):
		return  ProductVendorMappingModel.query\
					.filter(ProductVendorMappingModel.product_id==product_id)\
						.first_or_404()


	def add_product_vendor_mapping(self, product_id, vendor_id):
		error = False

		try:	
			product_vendor_mapping = ProductVendorMappingModel()
			product_vendor_mapping.product_id = product_id
			product_vendor_mapping.vendor_id = vendor_id

			db.session.add(product_vendor_mapping)
			db.session.commit()
			message = 'Product vendor mapping created'

		except:
			error = True
			db.session.rollback()
			print(sys.exc_info())
			message = 'Error creating product vendor mapping'

		if error:
			response = jsonify({
				'message': message
			})
		if not error:
			response = jsonify({
				'message': message, 
				'result': product_vendor_mapping.to_json()
			})
		return response
	