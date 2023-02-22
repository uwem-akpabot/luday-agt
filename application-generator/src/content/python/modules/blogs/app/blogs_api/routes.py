from pickle import INT
from urllib import response
from . import blogs_api_blueprint
from flask import jsonify
from .blogs import Blogs
from flask_restful import reqparse
from .. import db
from ..blogs_api import blogs

parser = reqparse.RequestParser(bundle_errors=True)

@blogs_api_blueprint.route('/api/blogs', methods=['GET'])
def get_blogs():
    blogs = Blogs()
    response = blogs.get_blogs(db)
    return response
    
@blogs_api_blueprint.route('/api/blogs', methods=['POST'])
def add_blogs():
    try:
        blogs = Blogs()
        response = blogs.add_blogs(db)
        return response

    except Exception as e:
        return {
            'message' : str(e)
        }, 400

@blogs_api_blueprint.route('/api/sblog/<slug>', methods=['GET'])
def get_blog_by_slug(slug):
    products = Blogs()
    response = products.get_blogs_by_slug(slug)
    return response

@blogs_api_blueprint.route('/api/blogs/search', methods=['POST'])
def search_blogs():
    blogs = Blogs()
    response = blogs.search_blogs()
    return response
    
@blogs_api_blueprint.route('/api/blogs/<blog_id>', methods=['PUT'])
def update_blog(blog_id):
    blogs = Blogs()
    response = blogs.update_blog(db, blog_id)
    return response

@blogs_api_blueprint.route('/api/blogs/<blog_id>', methods=['GET'])
def get_single_blog(blog_id):
    blogs = Blogs()
    response = blogs.get_single_blog(db, blog_id)
    return response

@blogs_api_blueprint.route('/api/blogs/count', methods=['GET'])
def get_count_of_blog():
    blogs = Blogs()
    response = blogs.get_count_of_blogs()
    return response

@blogs_api_blueprint.route('/api/blogs/<blog_id>', methods=['DELETE'])
def delete_blogs(blog_id):
    blogs = Blogs()
    response = blogs.delete_blogs(db, blog_id)
    return response

@blogs_api_blueprint.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


@blogs_api_blueprint.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422

@blogs_api_blueprint.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    }), 400