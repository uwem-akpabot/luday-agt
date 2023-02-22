# app/user_api/routes.py
from pickle import NONE
from flask import request, abort
from apifairy import body, response, arguments
from apifairy.decorators import other_responses
import os

from app import constants as k
from app.auth_api.auth import token_auth
from app.user_api import user_api_blueprint
from app.schemas import UserSchema, UpdateUserSchema, \
    AddressSchema, VendorsSchema, UpdateVendorSubacctSchema, \
    GetVendorByIdsSchema, GetUnAuthenticatedUserByIdsSchema
from app.user_api.user import User
from app.user_api.vendor import Vendor
from app.user_api.address import Address
from .api.PaystackClient import PaystackClient


from .. import db

user_schema = UserSchema()
vendor_schema = VendorsSchema()
address_schema = AddressSchema()
update_user_schema = UpdateUserSchema(partial=True)
update_vendor_subacct_schema = UpdateVendorSubacctSchema()
get_unauth_user_schema = GetUnAuthenticatedUserByIdsSchema()
get_vendor_by_ids_schema = GetVendorByIdsSchema()

user = User()
_vendor = Vendor()
address = Address()

"""
User role must sync with user_type column Enum values
app/models.py
"""
user_role = k.UserType.USER.value
vendor_role = k.UserType.VENDOR.value
super_admin = k.UserType.SUPER_ADMIN.value
sub_admin = k.UserType.SUB_ADMIN.value

@token_auth.get_user_roles
def get_user_roles(user):
    return user.get_roles()


@user_api_blueprint.route('/user', methods=['POST'])
@body(user_schema)
@response(user_schema, 201)
def add_user(args):
    response = user.add_user(args)
    return response


@user_api_blueprint.route('/user/auth', methods=['GET'])
@token_auth.login_required(role=[super_admin, sub_admin, user_role, vendor_role])
@response(user_schema)
def get_authenticated_user():
    return token_auth.current_user()


@user_api_blueprint.route('/user/sub-admin', methods=['GET'])
# @token_auth.login_required(role=super_admin)
def get_sub_admins():
    response = user.get_sub_admin()
    return response


@user_api_blueprint.route('/users', methods=['GET'])
@token_auth.login_required(role=super_admin)
def get_users():
    response = user.get_users()
    return response


@user_api_blueprint.route('/user/<int:id>', methods=['GET'])
# @token_auth.login_required(role=[super_admin, user_role, vendor_role])
@response(user_schema)
@other_responses({404: 'User not found'})
def get_user_by_id(id):
    return user.get_user_by_id_or_404(id)


@user_api_blueprint.route('/unauth/user', methods=['GET'])
@arguments(get_unauth_user_schema)
@response(user_schema)
@other_responses({404: 'User not found'})
def get_unauthenticated_user_by_id(args):
    _id = args['id']
    return user.get_user_by_id_or_404(_id)


@user_api_blueprint.route('/user/<email>', methods=['GET'])
@token_auth.login_required(role=[super_admin, user_role, vendor_role])
@response(user_schema)
@other_responses({404: 'User not found'})
def get_user_by_email(email):
    return user.get_user_by_email_or_404(email)


@user_api_blueprint.route('/auth/user/address', methods=['PUT'])
@token_auth.login_required(role=[super_admin, user_role, vendor_role])
@body(address_schema)
@response(address_schema, 201)
@other_responses({403: 'Forbidden.'})
def add_auth_user_address(args):
    auth_user = token_auth.current_user()
    user_id = args['user_id']
    args['email'] = auth_user.email
    
    if not auth_user:
        abort(403)

    user = address.get_address_by_user_id(user_id)    
    if user:
        response = address.update_address_by_user(user, args)
        return response
        
    response = address.add_user_address(args)
    return response

@user_api_blueprint.route('/user/address', methods=['PUT'])
@body(address_schema)
@response(address_schema, 201)
@other_responses({403: 'Forbidden.'})
def add_user_address(args):
    email = args['email']
    if not email:
        abort(403)
    
    guest = address.get_address_by_email(email)    
    if guest:
        response = address.update_address_by_guest(guest, args)
        return response
        
    response = address.add_user_address(args)
    return response


@user_api_blueprint.route('/user/attachment', methods=['GET'])
@token_auth.login_required(role=[super_admin, user_role, vendor_role])
def get_user_attachment():
    user = token_auth.current_user()
    return user.attachment_select()


@user_api_blueprint.route('/user/address', methods=['GET'])
@token_auth.login_required(role=[super_admin, user_role, vendor_role])
def get_user_address():
    user = token_auth.current_user()
    return user.address_select()

@user_api_blueprint.route('/user/deliveryaddress/<int:_id>', methods=['GET'])
#@token_auth.login_required(role=[super_admin, user_role, vendor_role])
def get_user_address_by_id(_id):
    user = address.get_address_by_address_id(_id)
    return user


@user_api_blueprint.route('/user/edit', methods=['PUT'])
@token_auth.login_required(role=[user_role, vendor_role])
@body(update_user_schema)
@response(user_schema)
@other_responses({403: 'Forbidden.'})
def update_user_details(data):
    auth_user = token_auth.current_user()
    if not auth_user:
        abort(403)

    if 'password' in data and ('old_password' not in data or
            not auth_user.verify_password(data['old_password'])):
        abort(400)
    user.update_authenticated_user(auth_user, data)
    return auth_user


@user_api_blueprint.route('/auth/user/vendors', methods=['PUT'])
@token_auth.login_required(role=[vendor_role])
@body(vendor_schema, location='form')
@response(vendor_schema, 201)
@other_responses({400: 'Image file is not allowed', 403: 'Forbidden.'})
def update_auth_vendor_details(args):
    auth_user = token_auth.current_user()
    if not auth_user:
        abort(403)
    user_id = args['user_id']
    if user_id == auth_user.id:
        response = _vendor.add_or_update_vendor(args)
        data = {
            "is_active": False
        }
        user.update_authenticated_user(auth_user, data)
        return response
    abort(403)

@other_responses({401: 'Unauthorized.'})
def update_vendor_subaccount_details(vendor):
    data = {
        "business_name": vendor.name,
        "account_number": vendor.business_account_no,
        "bank_code": vendor.business_bank_name_value,
        "percentage_charge": os.environ['PAYSTACK_SUBACCOUNT_PERCENTAGE_CHARGE']
    }
    subacount_data = PaystackClient.create_subaccount(data)
    if subacount_data:
       return _vendor.update_vendor_subaccount_details(vendor.id, subacount_data)
    abort(401)


@user_api_blueprint.route('/user/vendors', methods=['POST'])
# @token_auth.login_required(role=[super_admin])
# TODO: create vendor sechma and response data
def add_vendors():
    _user = user.add_vendors(db)
    if _user:
        return _user

    abort(400)


@user_api_blueprint.route('/user/vendors', methods=['GET'])
# @token_auth.login_required(role=super_admin)
def get_vendors():
    response = user.get_vendors(db)
    return response


@user_api_blueprint.route('/user/vendor', methods=['GET'])
@arguments(get_vendor_by_ids_schema)
@response(vendor_schema)
@other_responses({404: 'Vendor not found',
                  400: "Bad Request"})
def get_vendor_by_id(args):
    if 'id' in args:
        _id = args['id']
        response = _vendor.get_user_by_id_or_404(_id)
        return response
    if 'user_id' in args:
        user_id = args['user_id']
        response = _vendor.get_user_by_user_id(user_id)
        return response

    abort(400)


@user_api_blueprint.route('/user/vendors/<int:vendor_id>/<slug>', methods=['PUT'])
def edit_vendor(vendor_id, slug):
    response = user.edit_vendor(db, vendor_id, slug)
    return response


@user_api_blueprint.route('/user/vendors/verify/<int:user_id>', methods=['PUT'])
# @token_auth.login_required(role=[super_admin])
@other_responses({404: 'Vendor not found'})
def verify_vendor(user_id):
    vendor = _vendor.get_user_by_user_id(user_id)
    if vendor:
        subacount_data = update_vendor_subaccount_details(vendor)
        if subacount_data:
            response = user.verify_vendor(db, user_id)
            return response

    abort(404)


@user_api_blueprint.route('/user/vendors/unverify/<int:user_id>', methods=['PUT'])
def unverify_vendor(user_id):
    
    response = user.unverify_vendor(db, user_id)
    return response


@user_api_blueprint.route('/vendors/verify/all', methods=['PUT'])
@other_responses({404: 'Vendor not found'})
def verify_all_vendors():
    users = user.get_unverified_vendors()
    if users:
        for unverified_user in users:
            vendor = _vendor.get_user_by_user_id(unverified_user.id)
            if not vendor:
                abort(404)
            update_vendor_subaccount_details(vendor)

    response = user.verify_all_vendors(db)
    return response


@user_api_blueprint.route('/user/vendors/<slug>', methods=['GET'])
def get_single_vendors_slug(slug):
    response = user.get_single_vendor_by_slug(db, slug)
    return response


@user_api_blueprint.route('/user/vendors/<int:vendor_id>/<slug>', methods=['GET'])
def get_single_vendors(vendor_id, slug):
    response = user.get_single_vendors(vendor_id, slug)
    return response


@user_api_blueprint.route('/user/vendors/<int:vendor_id>/<slug>', methods=['DELETE'])
def delete_vendor(vendor_id, slug):
    vendor = User()
    response = vendor.delete_vendor(db, vendor_id, slug)
    return response

@user_api_blueprint.route('/admin/<int:id>', methods=['DELETE'])
def delete_admin(id):
    user = User()
    response = user.delete_admin(db, id)
    return response

@user_api_blueprint.route('/admin/<int:_id>', methods=['PUT'])
def edit_admin(_id):
    response = user.edit_admin(db, _id)
    return response