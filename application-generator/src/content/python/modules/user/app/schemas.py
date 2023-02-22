# app/schemas.py
from flask import current_app	
from marshmallow import validate, validates, \
    ValidationError
from apifairy.fields import FileField

from app.auth_api.auth import token_auth
from app import ma, db
from app.models import User, Address, Vendors

class EmptySchema(ma.Schema):
    pass


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        # ordered = current_app.config['JSON_SORT_KEYS']

    id = ma.auto_field(dump_only=True)
    first_name = ma.auto_field(required=True,
                             validate=validate.Length(min=2, max=15))
    last_name = ma.auto_field(required=True,
                             validate=validate.Length(min=2, max=15))
    email = ma.auto_field(required=True, validate=[validate.Length(max=120),
                            validate.Email()],
                            error_messages = {
                                'required': 'Missing data for required field.',
                                'null': 'Field may not be null.',
                            } )
    password = ma.String(required=True, load_only=True,
                         validate=validate.Length(min=3))
    gender = ma.String(required=False)
    user_type = ma.String(required=False)
    dob = ma.String(required=False)
    mobile_number = ma.String(required=False)
    provider = ma.String(required=False)
    is_active = ma.auto_field(required=False)
    first_seen = ma.auto_field(dump_only=True)
    last_seen = ma.auto_field(dump_only=True)

    @validates('email')
    def validate_email(self, value):
        user = token_auth.current_user()
        old_email = user.email if user else None
        if value != old_email and \
                db.session.scalar(User.query.filter_by(email=value)):
            raise ValidationError('Email already exists.')


class UpdateUserSchema(UserSchema):
    old_password = ma.String(load_only=True, validate=validate.Length(min=3))

    @validates('old_password')
    def validate_old_password(self, value):
        if not token_auth.current_user().verify_password(value):
            raise ValidationError('Password is incorrect')


class VendorsSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Vendors

    id = ma.auto_field(dump_only=True)
    name = ma.String(required=True)
    slug = ma.auto_field(dump_only=True)
    business_description = ma.String(required=True)
    business_image_path = ma.String(dump_only=True)
    user_id = ma.auto_field(required=False)
    business_bank_name = ma.String(required=True)
    business_bank_name_value = ma.String(required=True)
    business_account_no = ma.String(required=True)
    business_account_name = ma.String(required=True)
    business_account_name = ma.String(required=True)
    business_address = ma.String(required=True)
    business_city = ma.String(required=True)
    business_state = ma.String(required=True)
    business_state_value = ma.auto_field(required=True)
    business_subaccount_code = ma.auto_field(dump_only=True)
    business_percentage_charge = ma.auto_field(dump_only=True)
    image_file = FileField()
    user_id = ma.auto_field(required=True)


class GetUnAuthenticatedUserByIdsSchema(ma.Schema):
    id = ma.Integer(required=False)


class UpdateVendorSubacctSchema(ma.Schema):
    subaccount_code = ma.String(required=True)
    percentage_charge = ma.Integer(required=True)


class GetVendorByIdsSchema(ma.Schema):
    id = ma.Integer(required=False)
    user_id = ma.Integer(required=False)


class AddressSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Address

    ref_address_id = ma.auto_field(dump_only=True)
    address = ma.auto_field(required=True)
    ref_local_govt = ma.String(required=True)
    ref_state = ma.String(required=True)
    postal_code = ma.String(required=False)
    email = ma.String(required=False)
    user_id = ma.auto_field(required=False)

class TokenSchema(ma.Schema):

    access_token = ma.String(required=True)
    refresh_token = ma.String()


class PasswordResetRequestSchema(ma.Schema):
    class Meta:
        ordered = True

    email = ma.String(required=True, validate=[validate.Length(max=120),
                                               validate.Email()])


class PasswordResetSchema(ma.Schema):

    token = ma.String(required=True)
    new_password = ma.String(required=True, validate=validate.Length(min=3))
