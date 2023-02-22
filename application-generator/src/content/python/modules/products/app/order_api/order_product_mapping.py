# app/order_api/order_product_mapping.py
import os, sys
from flask import jsonify, current_app, abort, request, escape
from sqlalchemy import func

from app import db
from app.models import OrderProductMapping as OrderProductMappingModel, \
	ProductsModel

class OrderProductMapping():

	def _get_price(self, args):
		if 'sale_price' in args and args['sale_price'] >= 1:
			return args['sale_price']
		else:
			return args['price']


	def add_order_product_mapping(self, order_product, args):
		product_id = args['id']
		order_id = order_product.id
		quantity = args['cart_quantity']
		price = self._get_price(args)

		user_id = order_product.user_id
		vendor_id = args['vendor_id']
		error = False

		try:	
			order_product_mapping = OrderProductMappingModel()
			order_product_mapping.product_id = product_id
			order_product_mapping.order_id = order_id
			order_product_mapping.quantity = quantity
			order_product_mapping.price = price
			order_product_mapping.user_id = user_id
			order_product_mapping.vendor_id = vendor_id

			db.session.add(order_product_mapping)
			db.session.commit()
			message = 'Order Product created'

		except:
			error = True
			db.session.rollback()
			print(sys.exc_info())
			message = 'Error creating Order Product mapping'

		if error:
			response = jsonify({
				'message': message
			})
		if not error:
			response = jsonify({
				'message': message, 
				'result': order_product_mapping.to_dict()
			})
		return response


	def add_guest_order_product_mapping(self, order_product, args):
		product_id = args['id']
		order_id = order_product.id
		quantity = args['cart_quantity']
		price = self._get_price(args)		

		email = order_product.email
		vendor_id = args['vendor_id']
		error = False
		try:	
			order_product_mapping = OrderProductMappingModel()
			order_product_mapping.product_id = product_id
			order_product_mapping.order_id = order_id
			order_product_mapping.quantity = quantity
			order_product_mapping.price = price
			order_product_mapping.email = email
			order_product_mapping.vendor_id = vendor_id

			db.session.add(order_product_mapping)
			db.session.commit()
			message = 'Order Product created'

		except:
			error = True
			db.session.rollback()
			print(sys.exc_info())
			message = 'Error creating Order Product mapping'

		if error:
			response = jsonify({
				'message': message
			})
		if not error:
			response = jsonify({
				'message': message, 
				'result': order_product_mapping.to_dict()
			})
		return response

	def get_order_by_id_or_404(self, id):
		return db.session.get(OrderProductMappingModel, id) or abort(404)


	def get_order_mapping_by_order_id(self, order_id):
		return  OrderProductMappingModel.query\
			.filter(OrderProductMappingModel.order_id==order_id)\
				.filter(ProductsModel.id == OrderProductMappingModel.product_id)\
					.all()

	def get_order_product_item_sum_by_order_id_and_product_id(self, order_id, product_id):
		return db.session.query(db.func.sum(
					OrderProductMappingModel.price
				).label('amount'))\
				.filter(
					OrderProductMappingModel.order_id == order_id, 
					OrderProductMappingModel.product_id == product_id
				)\
				.all()
		
