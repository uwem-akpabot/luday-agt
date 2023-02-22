from doctest import FAIL_FAST
from pickle import FALSE, TRUE
from flask import request, abort, jsonify
import uuid, time, calendar, \
    os, pathlib, json

from apifairy import body, response
from apifairy.decorators import other_responses

from app.order_api import order_api_blueprint
from app import db
from app import constants as k

from app.order_api.orders import Orders
from app.helpers import ShareHandler
from app.products_api.product_vendor_mapping import ProductVendorMapping
from app.order_api.order_product_mapping import OrderProductMapping
from app.models import ProductsModel
from app.products_api.products import Products
from app.schemas import OrderSchema, \
    OrderProductMappingSchema, UpdateOrderTrxrefSchema

from .api.UserClient import UserClient
from app.models import ProductsModel
from app.products_api.products import Products
from .. import db
from .api.PaystackClient import PaystackClient
from ..shared_api.email_client.CustomMailClient import CustomMailClient
from ..shared_api.vendor_client.VendorClient import VendorClient

order_schema = OrderSchema()
order_product_mapping_schema = OrderProductMappingSchema()
update_order_trxref_schema = UpdateOrderTrxrefSchema()

order = Orders()
_products = Products()
order_product_mapping = OrderProductMapping()
product_vendor_mapping = ProductVendorMapping()

_custom_mail = CustomMailClient()

def get_order_by_id_or_404(id):
    return order.get_order_by_id_or_404(id)


def update_product_qty(product):
    main_quantity = ProductsModel.query\
        .with_entities(ProductsModel.quantity)\
        .filter(ProductsModel.id == product['id'])\
        .first_or_404()
        
    remaining_quantity = main_quantity.quantity - product['cart_quantity']
    if (remaining_quantity > 0) and (remaining_quantity <= 5):
        product_name = product['name']
        vendor = VendorClient.get_vendor_by_id(product['vendor_id'])
        if vendor:
            user = UserClient.get_unauthenticated_user_by_id(vendor['user_id'])

            first_name = user['first_name']
            venodr_business_name = vendor['name']
            _products.update_product_quantity(db, product['id'], remaining_quantity)
            message = {
                "subject":"Your product quantity is running low",
                "template": "lowProduct",
                "first_name": f"{first_name}",
                "business_name": f"{venodr_business_name}",
                "remaining_quantity": f"{remaining_quantity}",
                "product_name": f"{product_name}",
                "email": user['email']
            }
            _custom_mail.send_email_to_users(message)
            return True
        abort(404)
        
    elif(remaining_quantity > 5):
        _products.update_product_quantity(db, product['id'], remaining_quantity)
        return True

    return False


@order_api_blueprint.route('/order/user', methods=['POST'])
@body(order_product_mapping_schema)
@response(order_product_mapping_schema)
@other_responses({401: 'Unauthorized'})
@other_responses({403: 'Forbidden'})
def add_user_order(args):
    token = request.headers.get('Authorization')
    user_client_response = UserClient.get_user(token)

    if not user_client_response:
        abort(401)

    args['user_id'] = user_client_response['id']
    args['email'] = user_client_response['email']
    order_model = order.add_order(args)
    products = args['products']
    if order_model and products:
        for product in products:
            if args['status'] != k.OrderStatus.PAYMENT_FAILED:
                qty_check_update = update_product_qty(product)
                if not qty_check_update:
                    abort(403)
                order_product_mapping.add_order_product_mapping(order_model, product)

        if products:
            ShareHandler.handle_transaction_split(args, order_model)

    return order_model


@order_api_blueprint.route('/order/guest', methods=['POST'])
@body(order_product_mapping_schema)
@response(order_product_mapping_schema)
@other_responses({404: 'Not Found.'})
@other_responses({403: 'Forbidden'})
@other_responses({400: 'Bad Request'})
def add_guest_order(args):
    order_model = order.add_guest_order(args)
    products = args['products']
    if order_model and products:
        for product in products:            
            if args['status'] != k.OrderStatus.PAYMENT_FAILED:
                qty_check_update = update_product_qty(product)
                if not qty_check_update:
                    abort(403)
                order_product_mapping.add_guest_order_product_mapping(order_model, product)
    
        if products:
            ShareHandler.handle_transaction_split(args, order_model)

    return order_model


@order_api_blueprint.route('/order/user/', methods=['GET'])
@other_responses({401: 'Unauthorized'})
def get_user_order_details_or_404():
    token = request.headers.get('Authorization')
    user_client_response = UserClient.get_user(token)

    if not user_client_response:
        abort(401)
    user = user_client_response
    if user:
        user_id = user['id']
        return order.get_user_order_details_by_user_id_or_404(user_id)


@order_api_blueprint.route('/order/id', methods=['GET'])
@other_responses({404: 'Order not found'})
@other_responses({401: 'Unauthorized'})
def get_guest_order_details_by_id_or_404():
    args = request.args
    _id =  args.get('order_id')
    if not _id:
        abort(401)

    return  get_order_by_id_or_404(_id)


@order_api_blueprint.route('/order/vendor/id', methods=['GET'])
@other_responses({404: 'Order not found'})
@other_responses({401: 'Unauthorized'})
def get_order_by_vendor_user_id_or_404():
    args = request.args
    _id =  args.get('user_id')
    if not _id:
        abort(401)
        
    vendor_id = VendorClient.get_vendor_details_by_user_id(_id)
    
    return  order.get_order_by_vendor_id_or_404(vendor_id["id"])


@order_api_blueprint.route('/order/mapping/<int:id>', methods=['GET'])
@other_responses({404: 'Order not found'})
@other_responses({401: 'Unauthorized'})
def get_order_details_by_id_or_404(id):
    token = request.headers.get('Authorization')
    user_client_response = UserClient.get_user(token)

    if not user_client_response:
        abort(401)
    get_order_by_id = get_order_by_id_or_404(id)
    if get_order_by_id:
    
        return order.get_order_product_details_by_mapping_id_or_404(id)


@order_api_blueprint.route('/order/reference', methods=['GET'])
@other_responses({401: 'Unauthorized'})
@other_responses({404: 'Order not found'})
def get_order_by_ref_and_trxref_id():
    args = request.args
    ref_transaction_id =  args.get('trxref')
    ref_id = args.get('reference')

    if not ref_id or not ref_transaction_id:
        abort(401)

    return order.get_order_by_ref_and_trxref_id(ref_id, ref_transaction_id)


@order_api_blueprint.route('/order/all', methods=['GET'])
@other_responses({401: 'Unauthorized'})
@other_responses({404: 'Order not found'})
def get_all_order():
    return order.get_all_order_or_404()


@order_api_blueprint.route('/order/search/<search_param>', methods=['GET'])
@other_responses({401: 'Unauthorized'})
@other_responses({404: 'Order not found'})
def search_orders(search_param):
    return order.search_orders_or_404(search_param)


@order_api_blueprint.route('/order/sort', methods=['GET'])
@other_responses({404: 'Order not found'})
def search_orders_by_date():
    args = request.args
    date_query =  args.get('date')
    if not date_query:
        abort(404)

    return order.search_orders_by_date_or_404(date_query)


@order_api_blueprint.route('/order/payment/<payment_qurey>', methods=['GET'])
@other_responses({404: 'Order not found'})
def search_orders_by_payment(payment_qurey):
    return order.search_orders_by_payment_or_404(payment_qurey)


@order_api_blueprint.route('/order/delivery/<delivery_qurey>', methods=['GET'])
@other_responses({404: 'Order not found'})
def search_orders_by_delivery(delivery_qurey):
    return order.search_orders_by_delivery_or_404(delivery_qurey)


@order_api_blueprint.route('/order/trxref', methods=['PUT'])
@body(update_order_trxref_schema)
@response(update_order_trxref_schema)
@other_responses({401: 'Unauthorized'})
@other_responses({404: 'Order not found'})
def update_order_by_ref_id(args):
    ref_transaction_id =  args['ref_transaction_id']
    ref_id = args['ref_id']
    status = args['status']

    if not ref_id and not ref_transaction_id and not status:
        abort(401)
    get_order_by_ref_id = order.get_order_by_ref_id(ref_id)

    if not get_order_by_ref_id:
        abort(404)

    return order.update_order_by_ref_id(args)


@order_api_blueprint.route('/order/billing-address', methods=['PUT'])
@body(order_schema)
@response(order_schema)
@other_responses({401: 'Unauthorized'})
@other_responses({404: 'Order not found'})
def update_order_billing_address_id_by_ref_id(args):
    ref_id = args['ref_id']
    billing_address_id = args['billing_address_id']

    if not ref_id and not billing_address_id:
        abort(401)
    _order = order.get_order_by_ref_id(ref_id)

    if not _order:
        abort(404)

    return order.update_order_billing_address_id_by_ref_id(args)


@order_api_blueprint.route('/order/vendor/search/<search_param>/<int:_id>', methods=['GET'])
@other_responses({401: 'Unauthorized'})
@other_responses({404: 'Order not found'})
def search_vendor_orders_view_by_product_sku(search_param, _id):
    vendor_id = VendorClient.get_vendor_details_by_user_id(_id)
    return order.search_orders_by_sku_and_vendoe_id_or_404(search_param, vendor_id["id"])


@order_api_blueprint.route('/order/vendor/<int:_id>/sort', methods=['GET'])
@other_responses({404: 'Order not found'})
def search_vendor_orders_view_by_purchase_date(_id):
    args = request.args
    search_param =  args.get('date')
    if not search_param:
        abort(404)

    vendor_id = VendorClient.get_vendor_details_by_user_id(_id)
    return order.search_orders_by_date_and_vendoe_id_or_404(vendor_id["id"], search_param)


@order_api_blueprint.route('/order/vendor/delivery/<int:_id>/<search_param>', methods=['GET'])
@other_responses({404: 'Order not found'})
def search_vendor_orders_view_by_delivery_status(_id, search_param):
    vendor_id = VendorClient.get_vendor_details_by_user_id(_id)
    return order.search_orders_by_status_and_vendoe_id_or_404(vendor_id["id"], search_param)
