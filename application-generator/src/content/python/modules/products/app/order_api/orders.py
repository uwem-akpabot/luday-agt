# app/order_api/orders.py
import sys, uuid, time, calendar
from flask import jsonify, abort

from app import db
from app import constants as k
from app.models import Orders as OrderModel, \
	OrderProductMapping as OrderProductMappingModel, \
	ProductsModel
from app.order_api.i_order import IOrder
from app.order_api.order_product_mapping import OrderProductMapping
from ..shared_api.vendor_client.VendorClient import VendorClient, VendorAddressClient
from sqlalchemy import func
import dateparser
from ..shared_api.email_client.CustomMailClient import CustomMailClient

_custom_mail = CustomMailClient()
_order_product_mapping = OrderProductMapping()
class Orders(IOrder):
	def __init__(self) -> None:
		super().__init__()
		self.time_stamp = calendar.timegm(time.gmtime())

	def add_order(self, args, is_array=False):
		first_name = args['first_name']
		last_name = args['last_name']
		mobile_number = args['mobile_number']
		ref_transaction_id = args['ref_transaction_id']
		ref_id = f"{uuid.uuid4().hex}{self.time_stamp}"
		user_id = args['user_id']
		email = args['email']
		amount = args['amount']
		currency = args['currency']
		tax = args['tax']
		status = args['status']
		email = args['email']
		error = False

		try:	
			order = OrderModel()
			order.first_name = first_name
			order.last_name = last_name
			order.mobile_number = mobile_number
			order.ref_transaction_id = ref_transaction_id
			order.ref_id = ref_id
			order.user_id = user_id
			order.email = email
			order.amount = amount
			order.currency = currency
			order.tax = tax
			order.status = status
			order.email = email

			db.session.add(order)
			db.session.commit()

			order.ref_order_id = order.id
			db.session.add(order)
			db.session.commit()

			message = 'Order created'
		except:
			error = True
			db.session.rollback()
			print(sys.exc_info())
			message = 'Error creating an order'

		if error:
			response = jsonify({
				'message': message
			})
		if not error and is_array:
			response = jsonify({
				'message': message, 
				'result': order.to_dict()
			})
		if not error:
			response = order
		return response


	def add_guest_order(self, args, is_array=False):
		first_name = args['first_name']
		last_name = args['last_name']
		mobile_number = args['mobile_number']
		ref_transaction_id = args['ref_transaction_id']
		ref_id = f"{uuid.uuid4().hex}{self.time_stamp}"
		email = args['email']
		amount = args['amount']
		currency = args['currency']
		tax = args['tax']
		status = args['status']
		error = False

		try:	
			order = OrderModel()
			order.first_name = first_name
			order.last_name = last_name
			order.mobile_number = mobile_number
			order.ref_transaction_id = ref_transaction_id
			order.ref_id = ref_id
			order.email = email
			order.amount = amount
			order.currency = currency
			order.tax = tax
			order.status = status
			
			db.session.add(order)
			db.session.commit()

			order.ref_order_id = order.id
			db.session.add(order)
			db.session.commit()

			message = 'Order created'
		except Exception as e:
			error = True
			db.session.rollback()
			print(f"{e}")
			#print(sys.exc_info())
			message = 'Error creating an order'

		if error:
			response = jsonify({
				'message': message
			})
		if not error and is_array:
			response = jsonify({
				'message': message, 
				'result': order.to_dict()
			})
		if not error:
			response = order
		return response


	def find_order(self, id):
		return db.session.get(OrderModel, id) or abort(404)


	def get_all_order_or_404(self):
		orders = OrderModel.query\
				.order_by(OrderModel.id.desc())\
				.all()
				
		result = []
		if orders:
			for row in orders:
				result.append({
						'id': row.id,
						'ref_transaction_id': row.ref_transaction_id,
						'email': row.email,
						'ref_id': row.ref_id,
						'ref_order_id': row.ref_order_id,
						'first_name': row.first_name,
						'last_name': row.last_name,
						'mobile_number': row.mobile_number,
						'user_id': row.user_id,
						'amount': row.amount,
						'currency': row.currency, 
						'tax': row.tax,
						'status': row.status,
						'delivery_status': row.delivery_status,
						'billing_address_id': row.billing_address_id,
						'created_at': row.created_at,
						'updated_at': row.updated_at
				})
		response = jsonify({
			"data": result
		})
		return response


	def search_orders_or_404(self, search_param):
		orders_search = OrderModel.query\
				.filter(OrderModel.ref_id.ilike(f'%{search_param}%'))\
				.order_by(OrderModel.id.desc())\
				.all()
				
		result = []
		if not orders_search:
			message = 'No search found'
			result = []
		else:
			for row in orders_search:
				result.append({
						'id': row.id,
						'ref_transaction_id': row.ref_transaction_id,
						'email': row.email,
						'ref_id': row.ref_id,
						'ref_order_id': row.ref_order_id,
						'first_name': row.first_name,
						'last_name': row.last_name,
						'mobile_number': row.mobile_number,
						'user_id': row.user_id,
						'amount': row.amount,
						'currency': row.currency, 
						'tax': row.tax,
						'status': row.status,
						'delivery_status': row.delivery_status,
						'billing_address_id': row.billing_address_id,
						'created_at': row.created_at,
						'updated_at': row.updated_at
				})
				message = 'Success'
		response = jsonify({
			"message": message,
			"data": result
		})
		return response


	def search_orders_by_date_or_404(self, search_param):
		convert_to_date = dateparser.parse(search_param)
		date = convert_to_date.strftime("%Y-%m-%d %H:%M:%S")
		date_substring = date[:-9]
		error = False

		try:
			orders_search = OrderModel.query\
					.filter(func.date(OrderModel.created_at)==date_substring)\
					.order_by(OrderModel.id.desc())\
					.all()
					
			result = []
			if not orders_search:
				message = 'No search found'
				result = []
			else:
				for row in orders_search:
					result.append({
							'id': row.id,
							'ref_transaction_id': row.ref_transaction_id,
							'email': row.email,
							'ref_id': row.ref_id,
							'ref_order_id': row.ref_order_id,
							'first_name': row.first_name,
							'last_name': row.last_name,
							'mobile_number': row.mobile_number,
							'user_id': row.user_id,
							'amount': row.amount,
							'currency': row.currency, 
							'tax': row.tax,
							'status': row.status,
							'delivery_status': row.delivery_status,
							'billing_address_id': row.billing_address_id,
							'created_at': row.created_at,
							'updated_at': row.updated_at
					})
					message = 'Success'
		except:
			error = True
			message = sys.exc_info()

		if error:
			response = jsonify({
				'message': message,
				'date_param': search_param,
				'convert_to_date': convert_to_date,
				'date': date,
				'date_substring':date_substring
			})
		
		if not error:
			response = jsonify({
				"message": message,
				"data": result
			})
		return response


	def search_orders_by_delivery_or_404(self, search_param):
		orders_search = OrderModel.query\
				.filter_by(delivery_status=search_param)\
				.order_by(OrderModel.id.desc())\
				.all()
				
		result = []
		if not orders_search:
			message = 'No search found'
			result = []
		else:
			for row in orders_search:
				result.append({
						'id': row.id,
						'ref_transaction_id': row.ref_transaction_id,
						'email': row.email,
						'ref_id': row.ref_id,
						'ref_order_id': row.ref_order_id,
						'first_name': row.first_name,
						'last_name': row.last_name,
						'mobile_number': row.mobile_number,
						'user_id': row.user_id,
						'amount': row.amount,
						'currency': row.currency, 
						'tax': row.tax,
						'status': row.status,
						'delivery_status': row.delivery_status,
						'billing_address_id': row.billing_address_id,
						'created_at': row.created_at,
						'updated_at': row.updated_at
				})
				message = 'Success'
		response = jsonify({
			"message": message,
			"data": result
		})
		return response


	def search_orders_by_payment_or_404(self, search_param):
		orders_search = OrderModel.query\
				.filter(OrderModel.status==search_param)\
				.order_by(OrderModel.id.desc())\
				.all()
				
		result = []
		if not orders_search:
			message = 'No search found'
			result = []
		else:
			for row in orders_search:
				result.append({
						'id': row.id,
						'ref_transaction_id': row.ref_transaction_id,
						'email': row.email,
						'ref_id': row.ref_id,
						'ref_order_id': row.ref_order_id,
						'first_name': row.first_name,
						'last_name': row.last_name,
						'mobile_number': row.mobile_number,
						'user_id': row.user_id,
						'amount': row.amount,
						'currency': row.currency, 
						'tax': row.tax,
						'status': row.status,
						'delivery_status': row.delivery_status,
						'billing_address_id': row.billing_address_id,
						'created_at': row.created_at,
						'updated_at': row.updated_at
				})
				message = 'Success'
		response = jsonify({
			"message": message,
			"data": result
		})
		return response


	def get_order_by_id_or_404(self, id):
		order = OrderModel.query\
			.filter_by(id=id)\
				.first_or_404()

		order_product_mapping =  OrderProductMappingModel.query\
			.filter(OrderProductMappingModel.order_id==order.id)\
				.filter(ProductsModel.id == OrderProductMappingModel.product_id)\
					.all()					

		get_address = VendorAddressClient.get_user_address(order.billing_address_id) 

		productMappingData = []
		for order_product in order_product_mapping:
			vendors = VendorClient.get_user(order_product.vendor_id)
			#print (vendors['vendor'])
			productMappingData.append({
				'id': order_product.id,
				'product_id': order_product.product_id,
				'order_id': order_product.order_id,
				'quantity': order_product.quantity,
				'price': order_product.price,
				'name': order_product.products.name,
				'product_description': order_product.products.description,
				'product_image_name': order_product.products.image_name,
				'product_image_path': order_product.products.image_path,
				'product_sku': order_product.products.sku,
				'vendor_business_name': vendors['vendor'][0]['business_name']
			})
		
		response = jsonify({
				'id': order.id,
				'ref_transaction_id': order.ref_transaction_id,
				'email': order.email,
				'ref_id': order.ref_id,
				'first_name': order.first_name,
				'last_name': order.last_name,
				'mobile_number': order.mobile_number,
				'user_id': order.user_id,
				'amount': order.amount,
				'currency': order.currency, 
				'tax': order.tax,
				'status': order.status,
				'delivery_status': order.delivery_status,
				'billing_address_id': order.billing_address_id,
				'address': get_address,
				'created_at': order.created_at,
				'updated_at': order.updated_at,
				'products': productMappingData
		})
		return response

	def get_order_by_ref_id(self, ref_id):
		return OrderModel.query.filter_by(ref_id=ref_id).first()


	def get_order_mapping_by_order_id(self, order_id):
		return _order_product_mapping.get_order_mapping_by_order_id(order_id)

	
	def get_order_by_ref_and_trxref_id(self, ref_id,ref_transaction_id):
		order = OrderModel.query\
			.filter_by(ref_id=ref_id)\
				.filter_by(ref_transaction_id=ref_transaction_id)\
					.first_or_404()
		
		order_product_mapping =  self.get_order_mapping_by_order_id(order.id)

		productMappingData = []
		for order_product in order_product_mapping:
			productMappingData.append({
				'id': order_product.id,
				'product_id': order_product.product_id,
				'order_id': order_product.order_id,
				'quantity': order_product.quantity,
				'price': order_product.price,
				'name': order_product.products.name,
				'product_description': order_product.products.description,
				'product_image_name': order_product.products.image_name,
				'product_image_path': order_product.products.image_path,
				'product_sku': order_product.products.sku
			})
		
		response = jsonify({
				'id': order.id,
				'ref_transaction_id': order.ref_transaction_id,
				'email': order.email,
				'ref_id': order.ref_id,
				'first_name': order.first_name,
				'last_name': order.last_name,
				'mobile_number': order.mobile_number,
				'user_id': order.user_id,
				'amount': order.amount,
				'currency': order.currency, 
				'tax': order.tax,
				'status': order.status,
				'billing_address_id': order.billing_address_id,
				'created_at': order.created_at,
				'updated_at': order.updated_at,
				'products': productMappingData
		})
		return response


	def get_order_by_ref_and_id(self, ref_id, id):
		order = OrderModel.query\
			.filter_by(ref_id=ref_id)\
				.filter_by(id=id)\
					.first_or_404()

		order_product_mapping =  self.get_order_mapping_by_order_id(order.id)

		productMappingData = []
		for order_product in order_product_mapping:
			productMappingData.append({
				'id': order_product.id,
				'product_id': order_product.product_id,
				'order_id': order_product.order_id,
				'quantity': order_product.quantity,
				'price': order_product.price,
				'name': order_product.products.name,
				'product_description': order_product.products.description,
				'product_image_name': order_product.products.image_name,
				'product_image_path': order_product.products.image_path,
				'product_sku': order_product.products.sku
			})
		
		response = jsonify({
				'id': order.id,
				'ref_transaction_id': order.ref_transaction_id,
				'email': order.email,
				'ref_id': order.ref_id,
				'first_name': order.first_name,
				'last_name': order.last_name,
				'mobile_number': order.mobile_number,
				'user_id': order.user_id,
				'amount': order.amount,
				'currency': order.currency, 
				'tax': order.tax,
				'status': order.status,
				'billing_address_id': order.billing_address_id,
				'created_at': order.created_at,
				'updated_at': order.updated_at,
				'products': productMappingData
		})
		return response


	def update_order_by_ref_id(self, args):
			ref_id = args['ref_id']
			orderModel = self.get_order_by_ref_id(ref_id)
			orderModel.ref_transaction_id = args['ref_transaction_id']
			orderModel.ref_id = ref_id
			orderModel.status = args['status']

			db.session.commit()

			if args['status'] == "Successful":
				_mail = {
					"subject":"Order compeleted",
					"template": "orderComplete",
					"first_name": f"{orderModel.first_name}",
					"email": f"{orderModel.email}",
					"order_id": f"{orderModel.ref_id}"
				}
			else:
				_mail = {
				"subject":"Order not successful",
				"template": "orderNotComplete",
				"first_name": f"{orderModel.first_name}",
				"email": f"{orderModel.email}"
				}
			_custom_mail.send_email_to_users(_mail)

			return orderModel


	def update_order_billing_address_id_by_ref_id(self, args):
			ref_id = args['ref_id']
			orderModel = self.get_order_by_ref_id(ref_id)
			orderModel.billing_address_id = args['billing_address_id']

			db.session.commit()
			return orderModel

	
	def update_order_split_code_by_id(self, id, split_code):
			orderModel = self.find_order(id)
			orderModel.split_code = split_code

			db.session.commit()
			return orderModel


	def delete_order_by_id(id):
		order = OrderModel.query.get_or_404(id)
		db.session.delete(order)
		db.session.commit


	def get_order_product_details_by_mapping_id_or_404(self, id):
		data = []
		order_products = OrderProductMappingModel.query\
				.filter(OrderProductMappingModel.order_id == OrderModel.id)\
				.filter(OrderProductMappingModel.product_id == ProductsModel.id)\
				.filter(OrderModel.id == id)\
				.filter(OrderProductMappingModel.order_id == OrderModel.id)\
				.all()
		for order_product in order_products:
			items = {
				'order_id': order_product.orders.id,
				'ref_transaction_id': order_product.orders.ref_transaction_id,
				'email': order_product.orders.email,
				'ref_id': order_product.orders.ref_id,
				'first_name': order_product.orders.first_name,
				'last_name': order_product.orders.last_name,
				'mobile_number': order_product.orders.mobile_number,
				'user_id': order_product.orders.user_id,
				"delivery_status": order_product.orders.delivery_status,
				'amount': order_product.orders.amount,
				'currency': order_product.orders.currency, 
				'tax': order_product.orders.tax,
				'status': order_product.orders.status,
				'billing_address_id': order_product.orders.billing_address_id,
				'created_at': order_product.orders.created_at,
				'updated_at': order_product.orders.updated_at,
				'order_product_mapping_id': order_product.id,
				'order_product_mapping_product_id': order_product.product_id,
				'order_product_mapping_order_id': order_product.order_id,
				'order_product_mapping_quantity': order_product.quantity,
				'order_product_mapping_price': order_product.price,
				'product_id': order_product.products.id,
				'product_name': order_product.products.name,
				'product_description': order_product.products.description,
				'product_sale_price': order_product.products.sale_price,
				'product_image_name': order_product.products.image_name,
				'product_image_path': order_product.products.image_path,
				'product_sku': order_product.products.sku
			}
			data.append(items)
		response = jsonify(data)
		return response or abort(404)
		# data = []
		# order_product = OrderProductMappingModel.query.filter_by(id=id).first_or_404()
		# items = {
		# 		'order_id': order_product.orders.id,
		# 		'ref_transaction_id': order_product.orders.ref_transaction_id,
		# 		'email': order_product.orders.email,
		# 		'ref_id': order_product.orders.ref_id,
		# 		'first_name': order_product.orders.first_name,
		# 		'last_name': order_product.orders.last_name,
		# 		'mobile_number': order_product.orders.mobile_number,
		# 		'user_id': order_product.orders.user_id,
		# 		'amount': order_product.orders.amount,
		# 		'currency': order_product.orders.currency, 
		# 		'tax': order_product.orders.tax,
		# 		'status': order_product.orders.status,
		# 		'billing_address_id': order_product.orders.billing_address_id,
		# 		'created_at': order_product.orders.created_at,
		# 		'updated_at': order_product.orders.updated_at,
		# 		'order_product_mapping_id': order_product.id,
		# 		'order_product_mapping_product_id': order_product.product_id,
		# 		'order_product_mapping_order_id': order_product.order_id,
		# 		'order_product_mapping_quantity': order_product.quantity,
		# 		'order_product_mapping_price': order_product.price,
		# 		'product_id': order_product.products.id,
		# 		'product_name': order_product.products.name,
		# 		'product_description': order_product.products.description,
		# 		'product_sale_price': order_product.products.sale_price,
		# 		'product_image_name': order_product.products.image_name,
		# 		'product_image_path': order_product.products.image_path,
		# 		'product_sku': order_product.products.sku
		# 	}
		# data.append(items)
		# response = jsonify(items)
		# return response

	def get_user_order_details_by_user_id_or_404(self, user_id):
		data = []
		order_products = OrderModel.query\
				.filter(OrderModel.user_id == user_id)\
				.all()

		for order_product in order_products:
			items = {
				'order_id': order_product.id,
				'ref_transaction_id': order_product.ref_transaction_id,
				'email': order_product.email,
				'ref_id': order_product.ref_id,
				'mobile_number': order_product.mobile_number,
				'user_id': order_product.user_id,
				"delivery_status": order_product.delivery_status,
				'amount': order_product.amount,
				'currency': order_product.currency, 
				'tax': order_product.tax,
				'status': order_product.status,
				'billing_address_id': order_product.billing_address_id,
				'created_at': order_product.created_at,
				'updated_at': order_product.updated_at,
		
			}
			data.append(items)
		response = jsonify(data)
		return response or abort(404)
		# data = []
		# order_products = OrderProductMappingModel.query\
		# 		.filter(OrderModel.user_id == user_id)\
		# 		.filter(ProductsModel.id == OrderProductMappingModel.product_id)\
		# 		.filter(OrderProductMappingModel.order_id == OrderModel.id)\
		# 		.filter(OrderProductMappingModel.user_id == user_id)\
		# 		.all()
		# for order_product in order_products:
		# 	items = {
		# 		'order_id': order_product.orders.id,
		# 		'ref_transaction_id': order_product.orders.ref_transaction_id,
		# 		'email': order_product.orders.email,
		# 		'ref_id': order_product.orders.ref_id,
		# 		'first_name': order_product.orders.first_name,
		# 		'last_name': order_product.orders.last_name,
		# 		'mobile_number': order_product.orders.mobile_number,
		# 		'user_id': order_product.orders.user_id,
		# 		"delivery_status": order_product.orders.delivery_status,
		# 		'amount': order_product.orders.amount,
		# 		'currency': order_product.orders.currency, 
		# 		'tax': order_product.orders.tax,
		# 		'status': order_product.orders.status,
		# 		'billing_address_id': order_product.orders.billing_address_id,
		# 		'created_at': order_product.orders.created_at,
		# 		'updated_at': order_product.orders.updated_at,
		# 		'order_product_mapping_id': order_product.id,
		# 		'order_product_mapping_product_id': order_product.product_id,
		# 		'order_product_mapping_order_id': order_product.order_id,
		# 		'order_product_mapping_quantity': order_product.quantity,
		# 		'order_product_mapping_price': order_product.price,
		# 		'product_id': order_product.products.id,
		# 		'product_name': order_product.products.name,
		# 		'product_description': order_product.products.description,
		# 		'product_sale_price': order_product.products.sale_price,
		# 		'product_image_name': order_product.products.image_name,
		# 		'product_image_path': order_product.products.image_path,
		# 		'product_sku': order_product.products.sku
		# 	}
		# 	data.append(items)
		# response = jsonify(data)
		# return response or abort(404)

	def get_order_by_vendor_id_or_404(self, _id):
		order_products = OrderProductMappingModel.query\
			.filter(
				OrderProductMappingModel.vendor_id ==_id, 
				ProductsModel.id == OrderProductMappingModel.product_id, 
				OrderModel.id == OrderProductMappingModel.order_id, 
				OrderModel.status == k.OrderStatus.SUCCESS.value
			)\
			.order_by(OrderProductMappingModel.id.desc())\
			.all()

		productMappingData = []
		for order_product in order_products:
			productMappingData.append({
				'product_id': order_product.products.id,
				'product_name': order_product.products.name,
				'image_path': order_product.products.image_path,
				'product_ref': order_product.products.sku,
				'Order_ref': order_product.orders.ref_id,
				'delivery_status': order_product.orders.delivery_status,
				'quantity': order_product.quantity,
				'quantity_remaining': order_product.products.quantity,
				'price': order_product.price,
				'date_sold': order_product.orders.created_at
			})

		response = jsonify({
			"data": productMappingData
		})
		
		return response

	def search_orders_by_sku_and_vendoe_id_or_404(self, search_param, _id):
		orders_search = OrderProductMappingModel.query\
			.filter(
				OrderProductMappingModel.vendor_id ==_id, 
				ProductsModel.id == OrderProductMappingModel.product_id, 
				OrderModel.id == OrderProductMappingModel.order_id, 
				OrderModel.status == k.OrderStatus.SUCCESS.value, 
				ProductsModel.sku.ilike(f'%{search_param}%')
			)\
			.order_by(OrderProductMappingModel.id.desc())\
			.all()
		
				
		result = []
		if not orders_search:
			message = 'No search found'
			result = []
		else:
			for row in orders_search:
				result.append({
					'product_id': row.products.id,
					'product_name': row.products.name,
					'image_path': row.products.image_path,
					'product_ref': row.products.sku,
					'Order_ref': row.orders.ref_id,
					'delivery_status': row.orders.delivery_status,
					'quantity': row.quantity,
					'quantity_remaining': row.products.quantity,
					'price': row.price,
					'date_sold': row.orders.created_at,
				})
				message = 'Success'
		response = jsonify({
			"message": message,
			"data": result
		})
		return response

	def search_orders_by_date_and_vendoe_id_or_404(self, _id, search_param):
		convert_to_date = dateparser.parse(search_param)
		date = convert_to_date.strftime("%Y-%m-%d %H:%M:%S")
		date_substring = date[:-9]
		
		orders_search = OrderProductMappingModel.query\
			.filter(
				OrderProductMappingModel.vendor_id == _id, 
				ProductsModel.id == OrderProductMappingModel.product_id, 
				OrderModel.id == OrderProductMappingModel.order_id, 
				OrderModel.status == k.OrderStatus.SUCCESS.value,
				func.date(OrderModel.created_at) == date_substring
			)\
			.order_by(OrderProductMappingModel.id.desc())\
			.all()
		
				
		result = []
		if not orders_search:
			message = 'No search found'
			result = []
		else:
			for row in orders_search:
				result.append({
					'product_id': row.products.id,
					'product_name': row.products.name,
					'image_path': row.products.image_path,
					'product_ref': row.products.sku,
					'Order_ref': row.orders.ref_id,
					'delivery_status': row.orders.delivery_status,
					'quantity': row.quantity,
					'quantity_remaining': row.products.quantity,
					'price': row.price,
					'date_sold': row.orders.created_at,
				})
				message = 'Success'
		response = jsonify({
			"message": message,
			"data": result
		})
		return response


	def search_orders_by_status_and_vendoe_id_or_404(self, _id, search_param):
		
		orders_search = OrderProductMappingModel.query\
			.filter(
				OrderProductMappingModel.vendor_id ==_id, 
				ProductsModel.id == OrderProductMappingModel.product_id, 
				OrderModel.id == OrderProductMappingModel.order_id, 
				OrderModel.status == k.OrderStatus.SUCCESS.value, 
				OrderModel.delivery_status == search_param
			)\
			.order_by(OrderProductMappingModel.id.desc())\
			.all()
		
				
		result = []
		if not orders_search:
			message = 'No search found'
			result = []
		else:
			for row in orders_search:
				result.append({
					'product_id': row.products.id,
					'product_name': row.products.name,
					'image_path': row.products.image_path,
					'product_ref': row.products.sku,
					'Order_ref': row.orders.ref_id,
					'delivery_status': row.orders.delivery_status,
					'quantity': row.quantity,
					'quantity_remaining': row.products.quantity,
					'price': row.price,
					'date_sold': row.created_at,
				})
				message = 'Success'
		response = jsonify({
			"message": message,
			"data": result
		})
		return response
