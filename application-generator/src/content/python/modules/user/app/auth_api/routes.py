# app/auth_api/routes.py
import imp, os
from flask import request, abort, current_app, url_for, jsonify
from werkzeug.http import dump_cookie
from apifairy import authenticate, body, \
    response, other_responses

from app.auth_api import auth_api_blueprint, \
    tokens_api_blueprint
from app import db
from app.auth_api.auth import basic_auth
from app.models import User, Token
from app.schemas import TokenSchema, PasswordResetRequestSchema, \
    PasswordResetSchema, EmptySchema
from app.user_api.api.CustomMailClient import CustomMailClient

token_schema = TokenSchema()
_custom_mail = CustomMailClient()

def token_response(token):
    headers = {}
    if current_app.config['REFRESH_TOKEN_IN_COOKIE']:
        samesite = 'strict'
        if current_app.config['USE_CORS']:
            samesite = 'none' if not current_app.debug else 'lax'
        headers['Set-Cookie'] = dump_cookie(
            'refresh_token', token.refresh_token,
            path=url_for('tokens.new'), secure=not current_app.debug,
            httponly=True, samesite=samesite)
    return {
        'access_token': token.access_token,
        'refresh_token': token.refresh_token
        if current_app.config['REFRESH_TOKEN_IN_BODY'] else None,
    }, 200, headers

@tokens_api_blueprint.route('/auth/tokens', methods=['POST'])
@authenticate(basic_auth)
@response(token_schema)
@other_responses({401: 'Invalid username or password'})
def new():
    """Create new access and refresh tokens
    The refresh token is returned in the body of the request.
    """
    user = basic_auth.current_user()
    token = user.generate_auth_token()
    db.session.add(token)
    Token.clean()
    db.session.commit()
    return token_response(token)


@tokens_api_blueprint.route('/auth/tokens', methods=['PUT'])
@body(token_schema)
@response(token_schema, description='Newly issued access and refresh tokens')
@other_responses({401: 'Invalid access or refresh token'})
def refresh(args):
    """Refresh an access token
    The client has the option to pass the refresh token in the body of the
    request or in a `refresh_token` cookie. The access token must be passed in
    the body of the request.
    """
    access_token = args['access_token']
    refresh_token = args.get('refresh_token', request.cookies.get(
        'refresh_token'))
    if not access_token or not refresh_token:
        abort(401)
    token = User.verify_refresh_token(refresh_token, access_token)
    if not token:
        abort(401)
    token.expire()
    new_token = token.user.generate_auth_token()
    db.session.add_all([token, new_token])
    db.session.commit()
    return token_response(new_token)


@tokens_api_blueprint.route('/auth/tokens', methods=['DELETE'])
@response(EmptySchema, status_code=204, description='Token revoked')
@other_responses({401: 'Invalid access token'})
def revoke():
    """Revoke an access token"""
    access_token = request.headers['Authorization'].split()[1]
    token = db.session.scalar(Token.query.filter_by(
        access_token=access_token))
    if not token:
        abort(401)
    token.expire()
    db.session.commit()
    return {}


@tokens_api_blueprint.route('/auth/tokens/reset', methods=['POST'])
@body(PasswordResetRequestSchema)
@response(EmptySchema, status_code=204, description='Password reset email sent')
def reset(args):
    """Request a password reset token"""
    user = db.session.scalar(User.query.filter_by(email=args['email']))
    if user is not None:
        try:
            #reset_token = "user.generate_reset_token()"
            reset_token = user.generate_reset_token()
            reset_url = str(os.environ.get('PASSWORD_RESET_URL') + \
                '/' + reset_token)

            mailmessage = {
                "subject" : "Reset Your Password",
                "url": reset_url,
                "first_name" : user.first_name,
                "email" : args['email'],
                "template" : "reset"
            }
            _custom_mail.send_email_to_users(mailmessage)
            return{}
        except Exception as e:
            return f'<p>{e} </p>'
            
    return {}
    


@tokens_api_blueprint.route('/auth/tokens/reset', methods=['PUT'])
@body(PasswordResetSchema)
@response(EmptySchema, status_code=204,
          description='Password reset successful')
@other_responses({400: 'Invalid reset token'})
def password_reset(args):
    """Reset a user password"""
    user = User.verify_reset_token(args['token'])
    if user is None:
        abort(400)
    user.password = args['new_password']
    db.session.commit()
    return {}