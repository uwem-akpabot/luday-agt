# app/helpers.py
from flask import abort
import uuid, time, calendar, \
    os, pathlib, json

from app.order_api.api.PaystackClient import PaystackClient
from app.order_api.api.UserClient import UserClient
from app.order_api.orders import Orders
from app.order_api.order_product_mapping import OrderProductMapping
from app.products_api.product_vendor_mapping import ProductVendorMapping

order = Orders()
order_product_mapping = OrderProductMapping()
product_vendor_mapping = ProductVendorMapping()

subaccount_json_file = \
"""{
    "name":"Percentage Split Main", 
    "type":"percentage", 
    "currency": "NGN",
    "subaccounts":[],
    "bearer_type":"all"
}
"""

class FileHandler:
	def create_folder(path):
		try:
			os.makedirs(path)
		except FileExistsError:
			# directory already exists
			pass


	def remove_file(path):
		if(os.path.isfile(path)):
			file = pathlib.Path(path)
			file.unlink(path)
			print("File Deleted successfully")
		else:
			print("File does not exist")


	def write_json(new_data, filename):
		with open(filename,'r+') as file:
			file_data = json.load(file)
			file_data["subaccounts"].append(new_data)
			file.seek(0)

			json.dump(file_data, file, indent = 2)        


class ShareHandler:
	def getTransactionCharge(amount):
		charge = 0.05 * amount
		return  round(charge, 2)


	def getCheckoutShare(products_total, product_sub_total):
		share = (product_sub_total/products_total) * 100
		return round(share, 2)


	def getActualShare(share, charge):
		return share - charge


	def handle_transaction_split(args, order_model):
		order_id = order_model.id
		products = args['products']
		current_GMT = time.gmtime()
		time_stamp = calendar.timegm(current_GMT)
		file_name = f"{args['first_name']}-{args['last_name']}-{str(uuid.uuid4())}-{time_stamp}.json"
		path = f'app/order_api/temp/{file_name}'

		try:
			FileHandler.create_folder(pathlib.Path(path).parent.resolve())
			with open(path, 'w', encoding='utf-8') as f:
				f.write(subaccount_json_file)
		except FileNotFoundError:
			print("The 'assets' directory does not exist")
		
		product_id_key = 'id'
		product_id_key_unique_list = []

		for product in products:
			product_id_key_unique_list.append(product[product_id_key])
		product_id_key_unique_list = list(set(product_id_key_unique_list))

		for product[product_id_key] in product_id_key_unique_list:
			_vendor = product_vendor_mapping.get_product_vendor_mapping_by_product_id_or_404(product[product_id_key])
			if not _vendor:
				abort(404)
			vendor_id = _vendor.vendor_id

			vendor_details = UserClient.get_vendor_by_id(vendor_id)
			if not vendor_details:
				abort(404)
			product_items_sum = order_product_mapping.get_order_product_item_sum_by_order_id_and_product_id(
									order_id, product[product_id_key]
								)
			share_amount = product_items_sum[0][0]
			txn_charge = ShareHandler.getTransactionCharge(share_amount)
			actual_share = ShareHandler.getActualShare(share_amount, txn_charge)
			share = ShareHandler.getCheckoutShare(float(args['amount']), actual_share)
			vendor_subaccount = vendor_details['business_subaccount_code']
			user_subaccount_share = {
									"subaccount": vendor_subaccount,
									"share": share
								}
			FileHandler.write_json(user_subaccount_share, path)
		
		subaccount_json = open(path)
		param = json.load(subaccount_json)
		create_split = PaystackClient.create_transaction_split(param)

		if not create_split:
			abort(400)
		split_code = create_split['split_code']

		order_update = order.update_order_split_code_by_id(order_id, split_code)
		if order_update and subaccount_json:
			subaccount_json.close()
			FileHandler.remove_file(path)
