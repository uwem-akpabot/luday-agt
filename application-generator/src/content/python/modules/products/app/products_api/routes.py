import os
from flask_restful import reqparse
from flask import request, jsonify, abort

from pickle import INT
from urllib import response
from apifairy.decorators import other_responses

from . import products_api_blueprint
from .. import db
from .products import Products
from app.products_api import products
from app.products_api.product_vendor_mapping import ProductVendorMapping
from app.products_api.api.VendorClient import VendorClient

_products = Products()
_product_vendor_mapping = ProductVendorMapping()
parser = reqparse.RequestParser(bundle_errors=True)

@products_api_blueprint.route('/products', methods=['POST'])
def add_products():
    try:
        product = _products.add_products(db)
        if product:
            return product

    except Exception as e:
        return {
            'message' : str(e)
        }, 400

@products_api_blueprint.route('/products', methods=['GET'])
def get_products():
    page = request.args.get('page', 1, type=int)
    last_key = request.args.get('last_key', None, type=int)

    post_per_page = int(os.environ.get('POSTS_PER_PAGE') or '20')
    if last_key and last_key <= post_per_page:
        last_key = post_per_page + 1

    products = Products()
    response = products.get_products(db, page, last_key)
    return response

@products_api_blueprint.route('/products/details/<slug>', methods=['GET'])
def get_products_by_slug(slug):
    products = Products()
    response = products.get_products_by_slug(slug)
    return response

@products_api_blueprint.route('/products/search', methods=['GET'])
@other_responses({404: 'Not Found.'})
def search_products():
    search_query = request.args.get('q')
    page = request.args.get('page', 1, type=int)
    last_key = request.args.get('last_key', None, type=int)

    if search_query:
        products = Products()
        response = products.search_products(search_query, page, last_key)
        return response
    abort(404)


@products_api_blueprint.route('/products/<product_id>', methods=['PUT'])
def update_product(product_id):
    products = Products()
    response = products.update_product(db, product_id)
    return response

@products_api_blueprint.route('/products/<product_id>/verify', methods=['PUT'])
def verify_product(product_id):
    products = Products()
    response = products.verify_product(db, product_id)
    return response

@products_api_blueprint.route('/products/<product_id>/unverify', methods=['PUT'])
def unverify_product(product_id):
    products = Products()
    response = products.unverify_product(db, product_id)
    return response

@products_api_blueprint.route('/products/verify/all', methods=['PUT'])
def verify_all_products():
    products = Products()
    response = products.verify_all_products(db)
    return response

@products_api_blueprint.route('/products/<product_id>/feature', methods=['PUT'])
def feature_product(product_id):
    products = Products()
    response = products.feature_product(db, product_id)
    return response

@products_api_blueprint.route('/products/<product_id>/unfeature', methods=['PUT'])
def unfeature_product(product_id):
    products = Products()
    response = products.unfeature_product(db, product_id)
    return response

@products_api_blueprint.route('/products/<product_id>', methods=['GET'])
def get_single_product(product_id):
    products = Products()
    response = products.get_single_product(db, product_id)
    return response

@products_api_blueprint.route('/products/count', methods=['GET'])
def get_count_of_product():
    products = Products()
    response = products.get_count_of_products()
    return response

@products_api_blueprint.route('/products/featured', methods=['GET'])
def get_featured_product():
    products = Products()
    response = products.get_featured_products()
    return response

@products_api_blueprint.route('/products/unverified', methods=['GET'])
def get_unverified_products():
    products = Products()
    response = products.get_unverified_products(db)
    return response

@products_api_blueprint.route('/products/verified', methods=['GET'])
def get_verified_products():
    page = request.args.get('page', 1, type=int)
    last_key = request.args.get('last_key', None, type=int)

    post_per_page = int(os.environ.get('POSTS_PER_PAGE') or '10')
    if last_key and last_key <= post_per_page:
        last_key = post_per_page + 1

    products = Products()
    response = products.get_verified_products(db, page, last_key)
    return response


@products_api_blueprint.route('/products/<product_id>', methods=['DELETE'])
def delete_products(product_id):
    products = Products()
    response = products.delete_products(db, product_id)
    return response

@products_api_blueprint.route('/categories', methods=['GET'])
def get_categories():
    products = Products()
    response = products.get_categories()
    return response

@products_api_blueprint.route('/categories', methods=['POST'])
def add_categories():
    try:
        categories = Products()
        response = categories.add_categories(db)
        return response

    except Exception as e:
            return {
                'message' : str(e)
            }, 400

@products_api_blueprint.route('/categories/<category_id>', methods=['GET'])
def get_single_category(category_id):
    products = Products()
    response = products.get_single_category(category_id)
    return response
    
@products_api_blueprint.route('/categories/<category_id>', methods=['PUT'])
def update_category(category_id):
    products = Products()
    response = products.update_category(db, category_id)
    return response

@products_api_blueprint.route('/categories/<category_id>', methods=['DELETE'])
def delete_categories(category_id):
    products = Products()
    response = products.delete_categories(db, category_id)
    return response

@products_api_blueprint.route('/categories/<slug>/products', methods=['GET'])
def retrieve_products_by_category(slug):
    products = Products()
    response = products.retrieve_products_by_category(slug)
    return response

@products_api_blueprint.route('/vendors/<int:user_id>/products', methods=['GET'])
def retrieve_products_by_vendor(user_id):
    _vendor = VendorClient.get_vendor_by_user_id(user_id)
    products = Products()
    response = products.retrieve_products_by_vendor(_vendor['id'])
    return response

@products_api_blueprint.route('/vendors/products/<int:vendor_id>/verified', methods=['GET'])
def retrieve_verified_products_by_vendor(vendor_id):
    products = Products()
    response = products.retrieve_verified_products_by_vendor(vendor_id)
    return response

@products_api_blueprint.route('/products/<product_gallery_id>/gallery', methods=['DELETE'])
def delete_products_gallery(product_gallery_id):
    products = Products()
    response = products.delete_products_gallery(db, product_gallery_id)
    return response

@products_api_blueprint.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


@products_api_blueprint.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422

@products_api_blueprint.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    }), 400