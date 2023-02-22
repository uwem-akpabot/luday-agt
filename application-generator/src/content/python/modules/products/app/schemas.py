# app/schemas.py
from flask import current_app	
from marshmallow import validate

from app import ma, db
from app.models import Orders, OrderProductMapping

class EmptySchema(ma.Schema):
    pass


class OrderSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Orders
        ordered = current_app.config['JSON_SORT_KEYS']

    ref_order_id = ma.auto_field(dump_only=True)
    first_name = ma.auto_field(required=True,
                            error_messages={"required": "First name required."},
                            validate=validate.Length(min=2, max=15))
    last_name = ma.auto_field(required=False,
                            error_messages={"required": "Last name required."},
                            validate=validate.Length(min=2, max=15))
    mobile_number = ma.String(required=False)
    ref_transaction_id = ma.auto_field(required=False)
    ref_id = ma.auto_field(required=False)
    split_code = ma.auto_field(dump_only=True)
    user_id = ma.auto_field(dump_only=True)
    email = ma.auto_field(required=False)
    amount = ma.String(required=True, 
                    error_messages={"required": "Amount is required."})
    currency = ma.String(required=False)
    tax = ma.Integer(required=False)
    status = ma.String(required=False)
    billing_address_id = ma.Integer(required=False)
    delivery_status = ma.String(required=False)

class UpdateOrderTrxrefSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Orders

    id = ma.auto_field(dump_only=True)
    ref_transaction_id = ma.String(required=True)
    ref_id = ma.String(required=True)
    status = ma.String(required=True)
    updated_at = ma.auto_field(dump_only=True)
class OrderProductMappingSchema(OrderSchema):
    class Meta:
        model = OrderProductMapping
        ordered = current_app.config['JSON_SORT_KEYS']
   
    product_id = ma.auto_field(dump_only=True)
    order_id = ma.auto_field(dump_only=True)
    quantity = ma.auto_field(dump_only=True)
    price = ma.auto_field(dump_only=True)

    products = ma.List(ma.Dict(ma.String, ma.Raw), required=True)

