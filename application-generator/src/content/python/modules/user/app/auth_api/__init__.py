# app/auth_api/__init__.py

## Authentication
""" The authentication flow for this API is based on *access* and *refresh*
tokens.

To obtain an access and refresh token pair, the client must send a `POST`
request to the `/api/tokens` endpoint, passing the username and password of
the user in a `Authorization` header, according to HTTP Basic Authentication
scheme. The response includes the access and refresh tokens in the body.

Most endpoints in this API are authenticated with the access token, passed
in the `Authorization` header, using the `Bearer` scheme.

Access tokens are valid for 15 minutes (by default) from the time they are
issued. When the access token is expired, the client can renew it using the
refresh token. For this, the client must send a `PUT` request to the
`/api/tokens` endpoint, passing the expired access token in the body of the
request, and the refresh token either in the body. The response to this request 
will include a new pair of tokens. Refresh tokens have a default validity period
of 7 days, and can only be used to renew the access token they were returned with.
An attempt to use a refresh token more than once is considered a possible attack,
and will cause all existing tokens for the user to be revoked immediately as a
mitigation measure.
All authentication failures are handled with a `401` status code in the
response.
"""
from flask import Blueprint

auth_api_blueprint = Blueprint('auth_api', __name__)
tokens_api_blueprint = Blueprint('tokens_api', __name__)

from app.auth_api import routes