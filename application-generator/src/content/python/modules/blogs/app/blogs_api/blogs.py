from distutils.log import error
from email import message
from itertools import product
import logging
import sys, os
from unicodedata import category, name
from urllib import response
from flask import request, jsonify
from sqlalchemy import desc
from werkzeug.utils import secure_filename
from ..models import BlogsModel
from .i_blogs import IBlogs
from config import ROOT_DIR, blog_upload_folder
import base64

class Blogs(IBlogs):
	def get_blogs(self, _db):
		query = _db.session.query(BlogsModel).order_by(BlogsModel.id.desc()).all()
		items = []
		for row in query:
			items.append({
				"id": row.id,
				"title": row.title,
				"slug": row.slug,
				"summary": row.summary,
				#"content": base64.b64decode(row.content).decode('ascii'),
				"content": row.content,
				"image_path": row.image_path,
				"created_at": row.created_at.strftime("%d %B %Y"),
			})
		response = jsonify({'results': items})
		return response

	def add_blogs(self, _db):
		blog_image = request.files.get('blog_image')
		title = request.form.get('title')
		summary = request.form.get('summary')
		content = request.form.get('content')
		error = False
		
		allowed_extensions = {'webp', 'png', 'jpg', 'jpeg'}
		if not blog_image:
			error = True
			message = 'At least one image is required for blog'
		if blog_image:
			if self.allowed_file(blog_image.filename, allowed_extensions):
				filename = secure_filename(title + '.' + blog_image.filename.rsplit('.',1)[1])
				blog_image.save(os.path.join(blog_upload_folder, filename))
				try:
					blog = BlogsModel()
					blog.title = title
					blog.summary = summary
					blog.content = content
					blog.image_name = filename
					blog.image_path = 'images/blogs/'+filename
					_db.session.add(blog)
					_db.session.commit()
					message = 'Blog posted successfully'
				except:
					error = True
					_db.session.rollback()
					print(sys.exc_info())
					message = 'An error occurred! try again'
			if not self.allowed_file(blog_image.filename, allowed_extensions):
				error = True
				message = 'Image filetype not valid'
		if error:
			response = jsonify({
				'message': message, 
				'result': ''
			})
		if not error:
			response = jsonify({
				'message': message, 
				'result': blog.to_json()
			})
		return response

	def delete_blogs(self, _db, blog_id):
		print('Blog id: ', blog_id)
		blog = BlogsModel.query.get(blog_id)
		error = False
		if blog:
			_db.session.delete(blog)
			_db.session.commit()
			message = 'Blog post successfully deleted'	
		else:
			error = True
			message = 'Blog post does not exist'			
		response = jsonify({
			'message': message, 
			'result': blog_id
		})
		return response

	def update_blog(self, _db, blog_id):
		blog = BlogsModel.query.get(blog_id)
		image_name = blog.image_name
		image_path = blog.image_path
		
		error = False
		if blog:
			blog_image = request.files.get('blog_image')
			title = request.form.get('title')
			summary = request.form.get('summary')
			content = request.form.get('content')
			allowed_extensions = {'webp', 'png', 'jpg', 'jpeg'}
			
			if blog_image:
				if self.allowed_file(blog_image.filename, allowed_extensions):
					filename = secure_filename(secure_filename(name + '.' + blog_image.filename.rsplit('.',1)[1]))
					blog_image.save(os.path.join(blog_upload_folder, filename))
					image_name = filename
					image_path = 'images/blogs/'+filename
				else:
					error = True
					message = 'Invalid image file type'
			try:
				blog.title = title
				blog.summary = summary
				blog.content = content
				blog.image_name = image_name
				blog.image_path = image_path
				_db.session.add(blog)
				_db.session.commit()
				message = 'Blog post updated successfully'
			except:
				error = True
				_db.session.rollback()
				print(sys.exc_info())
				message = 'An error occurred please try again'
		if error:
			response = jsonify({
				'message': message,
				'result': ''
			})
		if not error:
			response = jsonify({
				'message': message,
				'result': blog.to_json()
			})
		return response
		
	def paginate_results(request, selection):
		RESULTS_PER_PAGE = 10
		page = request.args.get('page', 1, type=int)
		start = (page - 1) * RESULTS_PER_PAGE
		end = start + RESULTS_PER_PAGE

		results = [results.format() for results in selection]
		current_result = results[start:end]

		return current_result
	

	def get_blogs_by_slug(self, slug):
		blog = BlogsModel.query.filter_by(slug=slug).first()
		data = []
		if blog:
			data.append({
				"id": blog.id,
				"title": blog.title,
				"content": blog.content,
				"image_path": blog.image_path,
				#"created_at": self.created_at.strftime("%d %B %Y")	
			})
			message = 'Success'
		else:
			message = 'Blog not found'
			data = ''
		response = {'data': data, 'message': message }
		return response	

	def get_count_of_blogs(self):
		blog = BlogsModel.query.count()
		response = blog
		return jsonify({'results': response})

	def search_blogs(self):
		search_term = request.form.get('search_term')
		search_result = BlogsModel.query.filter(BlogsModel.name.ilike(f'%{search_term}%')).all()
		items = []

		for row in search_result:
			items.append({
				"id": row.id,
				"title": row.title,
				"content": row.content,
				"image_path": row.image_path,
				"created_at": row.created_at,
				"created_at": self.created_at.strftime("%d %B %Y")
			})		
		response=jsonify({
			"count": len(search_result),
			"results": items
		})
		return response

	def get_single_blog(self, _db, blog_id):
		print(blog_id)
		blog = _db.session.query(BlogsModel).get(blog_id)
		data = []
		if not blog:
			message = 'Blog post does not exist'
			data = ''
		if blog:
			data.append({
				"id": blog.id,
				"title": blog.title,
				"summary": blog.summary,
				"content": blog.content,
				"image_path": blog.image_path			
			})
			message = 'Success'
		response = jsonify({'data': data, 'message': message })
		return response

	def allowed_file(self, filename, allowed_extensions):
		return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions
		category = BlogCategoryMappingModel.query.filter_by(category_id=category_id).all()
		items = []
		message = ''
		if category:
			for blog in category:
				row = BlogsModel.query.get(blog.blog_id)
				items.append({
					"id": row.id,
					"name": row.name,
					"price": row.price,
					"sale_price": row.sale_price,
					"sku": row.sku,
					"featured": row.featured,
					"quantity": row.quantity,
					"description": row.description,
					"image_path": row.image_path,
					'blog_category_id': blog.category_id,
					"blog_category": BlogsModel.query.get(blog.category_id).name,
				})
		else:
			message = 'No blog post found or category does not exist'
		response = jsonify({
			'results': items, 
			'message': message
		})
		return response