from distutils.log import error
from email import message
from itertools import product
import sys, os
from urllib import response
from flask import request, jsonify, abort
from werkzeug.utils import secure_filename
from app.models import (
	CategoriesModel,
	OrderProductMapping, 
	ProductsModel, 
	ProductVendorMappingModel,
	ProductAttachmentsModel,
	ProductCategoryMappingModel
) 
from app.products_api.i_products import IProducts
from app.products_api.product_vendor_mapping import ProductVendorMapping
from app.products_api.api.VendorClient import VendorClient
from sqlalchemy import desc
from config import ROOT_DIR, product_upload_folder, category_upload_folder
from ..shared_api.email_client.CustomMailClient import CustomMailClient
from ..shared_api.vendor_client.VendorClient import VendorClient as v_client

_product_vendor_mapping = ProductVendorMapping()
allowed_extensions = {'webp', 'png', 'jpg', 'jpeg'}
_custom_mail = CustomMailClient()
_vendor_by_id = v_client()

class Products(IProducts):

	def paginate_results(request, selection):
		RESULTS_PER_PAGE = 10
		page = request.args.get('page', 1, type=int)
		start = (page - 1) * RESULTS_PER_PAGE
		end = start + RESULTS_PER_PAGE

		results = [results.format() for results in selection]
		current_result = results[start:end]

		return current_result
	
	def generateSKU(self, category, product_name, quantity):
		sku = category[:3] + quantity + product_name[:3]
		return sku

	def add_products(self, _db):
		product_img = request.files.get('product_image')
		name = request.form.get('name')
		message = ''
		description = request.form.get('description')
		price = request.form.get('price')
		sale_price = request.form.get('sale_price')
		quantity = request.form.get('quantity')
		category_id = request.form.get('category_id')
		category = CategoriesModel.query.get(category_id).name
		images_array = request.files.getlist('product_gallery_image')
		error = False
		
		if not product_img:
			error = True
			message = 'At least one image is required for product'
			code = 422
			
		if product_img:
			if self.allowed_file(product_img.filename, allowed_extensions):
				filename = secure_filename(name + '.' + product_img.filename.rsplit('.',1)[1])
				product_img.save(os.path.join(product_upload_folder, filename))
				try:
					if sale_price == '':
						actual_sale_price = 0.0
					else:
						actual_sale_price = sale_price
					product = ProductsModel()
					product.name = name
					product.description = description
					product.price = price
					product.sale_price = actual_sale_price
					product.quantity = quantity
					product.image_name = filename
					product.sku = self.generateSKU(category, name, quantity)
					product.featured = 0
					product.status = 1
					product.is_verified = 0
					product.image_path = 'images/products/'+filename
					_db.session.add(product)
					_db.session.flush()

					product_id = product.id
					self.handle_images_upload(_db, images_array, name, product_id)

					# Insert record into product category mapping
					product_category_mapping = ProductCategoryMappingModel()
					product_category_mapping.product_id = product_id
					product_category_mapping.category_id = category_id
					_db.session.add(product_category_mapping)

					# Insert record into product vendor mapping from frontend
					user_id = request.form.get('user_id')
					_vendor = VendorClient.get_vendor_by_user_id(user_id)
					_product_vendor_mapping.add_product_vendor_mapping(product.id, _vendor['id'])

					_db.session.commit()
					message = 'Product added successfully'
				except:
					error = True
					_db.session.rollback()
					print(sys.exc_info())
			else:
				error = True
				message = 'Image filetype not valid'
		if error:
			response = jsonify({
				'message': message, 
				'result': ''
			}), code or ''
		if not error:
			response = jsonify({
				'message': message, 
				'result': product.to_json()
			})
		return response
		
	def handle_images_upload(self, _db, images_array, name, product_id):
		error = False
		#Check if images gallery already exists in database
		count_of_gallery = ProductAttachmentsModel.query.filter_by(product_id=product_id).count()
		i = 0 if count_of_gallery == 0 else count_of_gallery
		for images in images_array:
			i+=1
			if self.allowed_file(images.filename, allowed_extensions):
				new_image_name = f"{name} gallery {i}"
				filename = secure_filename(new_image_name + '.' + images.filename.rsplit('.',1)[1])
				images.save(os.path.join(product_upload_folder, filename))
				try:
					product_attachment = ProductAttachmentsModel()
					product_attachment.name = filename
					product_attachment.path = 'images/products/'+filename
					product_attachment.product_id = product_id
					_db.session.add(product_attachment)
					_db.session.commit()
				except:
					error = True
					_db.session.rollback()
					print(sys.exc_info())
			else:
				error = True
				message = 'One of the images filetype is not valid'
		return

	def get_products(self, _db, page, last_key):
		if last_key:
			query = ProductsModel.query\
				.filter(ProductsModel.id < last_key)\
				.order_by(ProductsModel.id.desc())
		else:
			query = ProductsModel.query.order_by(ProductsModel.id.desc())

		post_per_page = int(os.environ.get('POSTS_PER_PAGE'))

		paginate = query.paginate(page, post_per_page, error_out=False)
		last_product_id = paginate.items[len(paginate.items) - 1].id
		next_page = paginate.next_num if paginate.has_next else None
		prev_page = paginate.prev_num if paginate.has_prev else None

		items = []
		for row in paginate.items:
			category_mapping = _db.session.query(ProductCategoryMappingModel).filter_by(product_id=row.id).first()
			category = CategoriesModel.query.get(category_mapping.category_id)
			products_gallery=[]
			products_attachment = _db.session.query(ProductAttachmentsModel).filter_by(product_id=row.id)
			for products in products_attachment:
				products_gallery.append({
					"id": products.id,
					"name": products.name,
					"path": products.path,
					"product_id": products.product_id
				})
			# Get product - vendor mapping
			vendor_mapping = _db.session.query(ProductVendorMappingModel).filter_by(product_id=row.id).first()

			items.append({
				"id": row.id,
				"name": row.name,
				"price": row.price,
				"sale_price": row.sale_price,
				"slug": row.slug,
				"sku": row.sku,
				"product_category": category.name,
				"product_category_id": category.id,
				"featured": row.featured,
				'is_verified': row.is_verified,
				'vendor_id': vendor_mapping.vendor_id,
				"quantity": row.quantity,
				"cart_quantity": 1,
				"description": row.description,
				"image_path": row.image_path,
				"products_gallery": products_gallery
			})
		response = jsonify({
			'results': items,
			"last_product_id": last_product_id,
			"next_page": next_page,
			"prev_page": prev_page
		})
		return response

	def get_products_by_slug(self, slug):
		product = ProductsModel.query.filter_by(slug=slug).first()
		data = []
		products_gallery=[]
		products_attachment = ProductAttachmentsModel.query.filter_by(product_id=product.id)
		for products in products_attachment:
			products_gallery.append({
				"id": products.id,
				"name": products.name,
				"path": products.path,
				"product_id": products.product_id
			})
		if product:
			category_mapping = ProductCategoryMappingModel.query.filter_by(product_id=product.id).first()
			vendor = ProductVendorMappingModel.query.filter_by(product_id=product.id).first()
			category = CategoriesModel.query.get(category_mapping.category_id)
			products_gallery=[]
			products_attachment = ProductAttachmentsModel.query.filter_by(product_id=product.id)
			for products in products_attachment:
				products_gallery.append({
					"id": products.id,
					"name": products.name,
					"path": products.path,
					"product_id": products.product_id
				})

			data.append({
				"id": product.id,
				"name": product.name,
				"price": product.price,
				"sale_price": product.sale_price,
				"slug": product.slug,
				"sku": product.sku,
				"product_category": category.name,
				"product_category_slug": category.slug,
				"product_category_id": category.id,
				"featured": product.featured,
				"vendor_id": vendor.vendor_id,
				"quantity": product.quantity,
				"cart_quantity": 1,
				"description": product.description,
				"image_path": product.image_path,
				"products_gallery": products_gallery					
			})
			message = 'Success'
		else:
			message = 'Product not found'
			data = ''
		response = {'data': data, 'message': message }
		return response	

	def get_count_of_products(self):
		products = ProductsModel.query.count()
		response = products
		return jsonify({'results': response})

	def get_featured_products(self):
		products = ProductsModel.query.filter_by(featured=1).all()
		data = []
		for product in products:
			category_mapping = ProductCategoryMappingModel.query.filter_by(product_id=product.id).first()
			vendor = ProductVendorMappingModel.query.filter_by(product_id=product.id).first()
			category = CategoriesModel.query.get(category_mapping.category_id)
			products_gallery=[]
			products_attachment = ProductAttachmentsModel.query.filter_by(product_id=product.id)
			for products in products_attachment:
				products_gallery.append({
					"id": products.id,
					"name": products.name,
					"path": products.path,
					"product_id": products.product_id
			})
			data.append({
				"id": product.id,
				"name": product.name,
				"price": product.price,
				"sale_price": product.sale_price,
				"sku": product.sku,
				"slug": product.slug,
				"product_category": category.name,
				"product_category_id": category.id,
				"featured": product.featured,
				'vendor_id': vendor.vendor_id,
				"quantity": product.quantity,
				"cart_quantity": 1,
				"description": product.description,
				"image_path": product.image_path,
				"products_gallery": products_gallery				
			})
		response = {'results': data }
		return response	

	def search_products(self, search_query, page, last_key):
		if last_key:
			search_result = ProductsModel.query\
				.filter(ProductsModel.name.ilike(f'%{search_query}%'))\
				.filter(ProductsModel.id < last_key)\
				.order_by(ProductsModel.id.desc())
		else:
			search_result = ProductsModel.query\
				.filter(ProductsModel.name.ilike(f'%{search_query}%'))\
				.order_by(ProductsModel.id.desc())

		post_per_page = int(os.environ.get('POSTS_PER_PAGE'))

		paginate = search_result.paginate(page, post_per_page, error_out=False)
		last_product_id = paginate.items[len(paginate.items) - 1].id
		next_page = paginate.next_num if paginate.has_next else None
		prev_page = paginate.prev_num if paginate.has_prev else None

		items = []
		if not search_result:
			message = f'No search found for {search_query}'
			items = ''
		else:
			for row in paginate.items:
				category_mapping = ProductCategoryMappingModel.query.filter_by(product_id=row.id).first()
				vendor = ProductVendorMappingModel.query.filter_by(product_id=row.id).first()
				category = CategoriesModel.query.get(category_mapping.category_id)

				items.append({
					"id": row.id,
					"name": row.name,
					"price": row.price,
					"sale_price": row.sale_price,
					"slug": row.slug,
					"sku": row.sku,
					"product_category": category.name,
					"product_category_id": category.id,
					'is_verified': row.is_verified,
					"featured": row.featured,
					'vendor_id': vendor.vendor_id,
					"quantity": row.quantity,
					"cart_quantity": 1,
					"description": row.description,
					"image_path": row.image_path,
					# "products_gallery": products_gallery
				})
				message = 'Success'
		response=jsonify({
			"results": items,
			"message": message,
			"last_product_id": last_product_id,
			"next_page": next_page,
			"prev_page": prev_page
		})
		return response

	def get_single_product(self, _db, product_id):
		product = _db.session.query(ProductsModel).get(product_id)
		data = []
		products_gallery=[]
		products_attachment = _db.session.query(ProductAttachmentsModel).filter_by(product_id=product_id)
		for products in products_attachment:
			products_gallery.append({
				"id": products.id,
				"name": products.name,
				"path": products.path,
				"product_id": products.product_id
			})
		if not product:
			message = 'Product does not exist'
			data = ''
		if product:
			category_mapping = _db.session.query(ProductCategoryMappingModel).filter_by(product_id=product_id).first()
			vendor = ProductVendorMappingModel.query.filter_by(product_id=product.id).first()
			category = CategoriesModel.query.get(category_mapping.category_id)
			data.append({
				"id": product.id,
				"name": product.name,
				"price": product.price,
				"sale_price": product.sale_price,
				"slug": product.slug,
				"sku": product.sku,
				'is_verified': product.is_verified,
				"product_category": category.name,
				"product_category_id": category.id,
				"featured": product.featured,
				'vendor_id': vendor.vendor_id,
				"quantity": product.quantity,
				"cart_quantity": 1,
				"description": product.description,
				"image_path": product.image_path,
				"products_gallery": products_gallery				
			})
			message = 'Success'
		response = jsonify({'data': data, 'message': message })
		return response

	def delete_products(self, _db, product_id):
		product = ProductsModel.query.get(product_id)
		error = False
		if product:
			#Check if product exists as an order
			product_order_check = OrderProductMapping.query.filter_by(product_id=product_id).all()
			if product_order_check:
				product.status = 0
				_db.session.add(product)
				_db.session.commit()
			if not product_order_check:
				os.remove(os.path.join(product_upload_folder, product.image_name))
				product_gallery = ProductAttachmentsModel.query.filter_by(product_id=product_id)
				for products in product_gallery:
					self.delete_products_gallery(_db, products.id)	
				_db.session.delete(product)
				_db.session.commit()
			message = 'Product successfully deleted'	
		else:
			error = True
			message = 'Product does not exist'			
		response = jsonify({
			'message': message, 
			'result': product_id
		})
		return response
	
	def get_unverified_products(self, _db):
		query = _db.session.query(ProductsModel).filter_by(is_verified=0)
		items = []
		for row in query:
			# Get product - category mapping
			category_mapping = _db.session.query(ProductCategoryMappingModel).filter_by(product_id=row.id).first()
			category = CategoriesModel.query.get(category_mapping.category_id)
			products_gallery=[]
			products_attachment = _db.session.query(ProductAttachmentsModel).filter_by(product_id=row.id)
			for products in products_attachment:
				products_gallery.append({
					"id": products.id,
					"name": products.name,
					"path": products.path,
					"product_id": products.product_id
				})
			# Get product - vendor mapping
			vendor_mapping = _db.session.query(ProductVendorMappingModel).filter_by(product_id=row.id).first()

			items.append({
				"id": row.id,
				"name": row.name,
				"price": row.price,
				"sale_price": row.sale_price,
				"slug": row.slug,
				"sku": row.sku,
				'is_verified': row.is_verified,
				"product_category": category.name,
				"product_category_id": category.id,
				"featured": row.featured,
				'vendor_id': vendor_mapping.vendor_id,
				"quantity": row.quantity,
				"cart_quantity": 1,
				"description": row.description,
				"image_path": row.image_path,
				"products_gallery": products_gallery
			})
		response = jsonify({'results': items})
		return response

	def get_verified_products(self, _db, page, last_key):
		if last_key:
			query = ProductsModel.query\
				.filter(ProductsModel.id < last_key)\
				.order_by(ProductsModel.id.desc())
		else:
			query = ProductsModel.query.order_by(ProductsModel.id.desc())

		post_per_page = int(os.environ.get('POSTS_PER_PAGE'))

		paginate = query.paginate(page, post_per_page, error_out=False)
		last_product_id = paginate.items[len(paginate.items) - 1].id
		next_page = paginate.next_num if paginate.has_next else None
		prev_page = paginate.prev_num if paginate.has_prev else None

		items = []
		for row in paginate.items:
			category_mapping = _db.session.query(ProductCategoryMappingModel).filter_by(product_id=row.id).first()
			category = CategoriesModel.query.get(category_mapping.category_id)
			products_gallery=[]
			products_attachment = _db.session.query(ProductAttachmentsModel).filter_by(product_id=row.id)
			for products in products_attachment:
				products_gallery.append({
					"id": products.id,
					"name": products.name,
					"path": products.path,
					"product_id": products.product_id
				})
			# Get product - vendor mapping
			vendor_mapping = _db.session.query(ProductVendorMappingModel).filter_by(product_id=row.id).first()

			items.append({
				"id": row.id,
				"name": row.name,
				"price": row.price,
				"sale_price": row.sale_price,
				"slug": row.slug,
				"sku": row.sku,
				"product_category": category.name,
				"product_category_id": category.id,
				"product_category_img": category.image_path,
				"featured": row.featured,
				'is_verified': row.is_verified,
				'vendor_id': vendor_mapping.vendor_id,
				"quantity": row.quantity,
				"cart_quantity": 1,
				"description": row.description,
				"image_path": row.image_path,
				"products_gallery": products_gallery
			})
		response = jsonify({
			'results': items,
			"last_product_id": last_product_id,
			"next_page": next_page,
			"prev_page": prev_page
		})
		return response

	def verify_product(self, _db, product_id):
		product = ProductsModel.query.get(product_id)
		error = False
		if not product:
			message = 'Product does not exist'
		if product:
			get_vendor_id = ProductVendorMappingModel.query.filter_by(product_id = product.id).first()
			vendor = _vendor_by_id.get_user(get_vendor_id.vendor_id)
			
			try:
				product.is_verified = 1
				_db.session.add(product)
				_db.session.commit()
				_mail = {
					"subject":"Product Verified and Listed",
					"template": "productApproved",
					"first_name": vendor["vendor"][0]["first_name"],
					"email": vendor["vendor"][0]["email"],
					"product_slug": f"{product.slug}",
					"product_name": f"{product.name}"
				}
				_custom_mail.send_email_to_users(_mail)
				message = 'Product verified'
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
				'result': product.to_json()
			})
		return response

	def unverify_product(self, _db, product_id):
		product = ProductsModel.query.get(product_id)
		error = False
		if not product:
			message = 'Product does not exist'
		if product:
			get_vendor_id = ProductVendorMappingModel.query.filter_by(product_id = product.id).first()
			vendor = _vendor_by_id.get_user(get_vendor_id.vendor_id)
			try:
				product.is_verified = 0
				product.featured = 0
				_db.session.add(product)
				_db.session.commit()

				_mail = {
					"subject":"Product Unlisted",
					"template": "unListProduct",
					"first_name": vendor["vendor"][0]["first_name"],
					"email": vendor["vendor"][0]["email"],
					"product_name": f"{product.name}"
				}
				_custom_mail.send_email_to_users(_mail)

				message = 'Product unverified'
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
				'result': product.to_json()
			})
		return response

	def verify_all_products(self, _db):
		products = ProductsModel.query.filter_by(is_verified=0).all()
		if not products:
			message = 'No unverified products found'
		if products:
			for product in products:
				get_vendor_id = ProductVendorMappingModel.query.filter_by(product_id = product.id).first()
				vendor = _vendor_by_id.get_user(get_vendor_id.vendor_id)
				try:
					product.is_verified = 1
					_db.session.add(product)
					_db.session.commit()
					
					_mail = {
					"subject":"Product Verified and Listed",
					"template": "productApproved",
					"first_name": vendor["vendor"][0]["first_name"],
					"email": vendor["vendor"][0]["email"],
					"product_slug": f"{product.slug}",
					"product_name": f"{product.name}"
					}

					_custom_mail.send_email_to_users(_mail)
					message = 'All products verified'
				except:
					error = True
					_db.session.rollback()
					print(sys.exc_info())
					message = 'An error occurred please try again'
		response = jsonify({
			'message': message,
		})
		return response
			
	def update_product(self, _db, product_id):
		product = ProductsModel.query.get(product_id)
		image_name = product.image_name
		image_path = product.image_path
		images_array = request.files.getlist('product_gallery_image')

		error = False
		if product:
			product_img = request.files.get('product_image')
			name = request.form.get('name')
			description = request.form.get('description')
			price = request.form.get('price')
			sale_price = request.form.get('sale_price')
			quantity = request.form.get('quantity')
			category_id = request.form.get('category_id')
			allowed_extensions = {'webp', 'png', 'jpg', 'jpeg'}
			category = CategoriesModel.query.get(category_id).name
			
			if product_img:
				if self.allowed_file(product_img.filename, allowed_extensions):
					filename = secure_filename(secure_filename(name + '.' + product_img.filename.rsplit('.',1)[1]))
					product_img.save(os.path.join(product_upload_folder, filename))
					image_name = filename
					image_path = 'images/products/'+filename
				else:
					error = True
					message = 'Invalid image file type'
			try:
				product.name = name
				product.description = description
				product.price = price
				product.sale_price = sale_price
				product.quantity = quantity
				product.image_name = image_name
				product.sku = self.generateSKU(category, name, quantity)
				product.image_path = image_path
				_db.session.add(product)
				_db.session.flush()
				self.handle_images_upload(_db, images_array, name, product_id)
				product_category_mapping = ProductCategoryMappingModel.query.filter_by(product_id=product_id).first()
				product_category_mapping.product_id = product_id
				product_category_mapping.category_id = category_id
				_db.session.add(product_category_mapping)
				_db.session.commit()
				message = 'Product updated successfully'
			except:
				error = True
				_db.session.rollback()
				print(sys.exc_info())
				message = 'An error occured please try again'
		if error:
			response = jsonify({
				'message': message,
				'result': ''
			})
		if not error:
			response = jsonify({
				'message': message,
				'result': product.to_json()
			})
		return response


	def update_product_quantity(self, _db, product_id, remaining_quantity):
		product = ProductsModel.query.get(product_id)
		error = False
		if product:
			quantity = remaining_quantity

			try:
				product.quantity = quantity
				
				_db.session.add(product)
				_db.session.commit()
				message = 'Product quantity updated successfully'
			except:
				error = True
				_db.session.rollback()
				print(sys.exc_info())
				message = 'An error occured please try again'
		if error:
			response = jsonify({
				'message': message,
				'result': ''
			})
		if not error:
			response = jsonify({
				'message': message,
				'result': product.to_json()
			})
		return response
		

	# Accept filename and allowed extensions and checks if file is acceptable
	def allowed_file(self, filename, allowed_extensions):
		return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions
	
	def add_categories(self, _db):
		cat_img = request.files.get('category_image')
		name = request.form.get('name')
		description = request.form.get('description')
		allowed_extensions = {'webp', 'png', 'jpg', 'jpeg'}
		error = False
		if not cat_img:
			error = True
			message = 'Category image cannot be empty'
		else:
			if self.allowed_file(cat_img.filename, allowed_extensions):
				filename = secure_filename(name + '.' + cat_img.filename.rsplit('.',1)[1])
				cat_img.save(os.path.join(category_upload_folder, filename))	
				try:
					category = CategoriesModel()
					category.name = name
					category.description = description
					category.image_name = filename
					category.image_path = 'images/categories/'+filename
					_db.session.add(category)
					_db.session.commit()

				except:
					error = True
					_db.session.rollback()
					print(sys.exc_info())
			else:
				error = True
				message = 'Image filetype not valid'	
		if error:
			response = jsonify({
				'message': message, 
				'result': ''
			})
		if not error:
			response = jsonify({
				'message': 'Category added', 
				'result': category.to_json()
			})
		return response

	def get_categories(self):
		items = []
		for row in CategoriesModel.query.all():
			items.append(row.to_json())
		response = jsonify({'results': items})
		return response
	
	def get_single_category(self, category_id):
		category = CategoriesModel.query.get(category_id)
		if not category:
			message = 'Category does not exist'
			data = ''
		if category:
			data = category.to_json()
			message = 'Success'
		response = jsonify({'data': data, 'message': message })
		return response

	def update_category(self, _db, category_id):
		category = CategoriesModel.query.get(category_id)
		image_name = category.image_name
		image_path = category.image_path
		error = False
		if category:
			cat_img = request.files.get('category_image')
			name = request.form.get('name')
			description = request.form.get('description')
			allowed_extensions = {'webp', 'png', 'jpg', 'jpeg'}
			if cat_img:
				os.remove(os.path.join(category_upload_folder, image_name))
				if self.allowed_file(cat_img.filename, allowed_extensions):
					filename = secure_filename(name + '.' + cat_img.filename.rsplit('.',1)[1])
					image_name = filename
					image_path = 'images/categories/'+filename
					cat_img.save(os.path.join(category_upload_folder, filename))
				else:
					error = True
					message = 'Category image cannot be empty'
			try:
				category.name = name
				category.description = description
				category.image_name = image_name
				category.image_path = image_path
				_db.session.commit()
				message = 'Category updated successfully'
			except:
				error = True
				message = 'An error occured, please try again'
				_db.session.rollback()
		else:
			error = True
			message = 'Category does not exist'
		
		if error:
			response = jsonify({
				'message': message,
				'result': ''
			})
		if not error:
			response = jsonify({
				'message': message,
				'result': category.to_json()
			})			
				
		return response

	def delete_categories(self, _db, category_id):
		category = CategoriesModel.query.get(category_id)
		if not category:
			message = 'Category does not exist'
		if category:
			check_if_category_in_use = ProductCategoryMappingModel.query.filter_by(category_id=category_id).first()
			if not check_if_category_in_use:
				os.remove(os.path.join(category_upload_folder, category.image_name))
				_db.session.delete(category)
				_db.session.commit()
				message = 'Category successfully deleted'
			if check_if_category_in_use:
				message = 'Category is in use and cannot be deleted'		
		response = jsonify({
			'message': message, 
			'result': category_id
		})
		return response

	def retrieve_products_by_category(self, slug):
		categories = CategoriesModel.query.filter_by(slug=slug).first()
		category = ProductCategoryMappingModel.query.filter_by(category_id=categories.id).all()
		items = []
		message = ''
		if category:
			for product in category:
				row = ProductsModel.query.filter_by(id=product.product_id, is_verified=1).first()
				vendor = ProductVendorMappingModel.query.filter_by(product_id=product.product_id).first()
				products_gallery=[]
				if row:
					products_attachment = ProductAttachmentsModel.query.filter_by(product_id=row.id)
					for products in products_attachment:
						products_gallery.append({
							"name": products.name,
							"path": products.path,
							"product_id": products.product_id
						})
					items.append({
						"id": row.id,
						"name": row.name,
						"price": row.price,
						"sale_price": row.sale_price,
						"slug": row.slug,
						"sku": row.sku,
						"featured": row.featured,
						'is_verified': row.is_verified,
						# 'vendor': vendor.name,
						'vendor_id': vendor.vendor_id,
						"quantity": row.quantity,
						"cart_quantity": 1,
						"description": row.description,
						"image_path": row.image_path,
						'product_category_id': product.category_id,
						"product_category": CategoriesModel.query.get(product.category_id).name,
						"product_category_img": CategoriesModel.query.get(product.category_id).image_path,
						"products_gallery": products_gallery
					})
		else:
			message = 'No product found or category does not exist'
		response = jsonify({
			'results': items, 
			'message': message
		})
		return response

	def feature_product(self, _db, product_id):
		product = ProductsModel.query.get(product_id)
		error = False
		if not product:
			message = 'Product does not exist'
		if product:
			try:
				product.featured = 1
				_db.session.add(product)
				_db.session.commit()
				message = 'Product featured'
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
				'result': product.to_json()
			})
		return response

	def unfeature_product(self, _db, product_id):
		product = ProductsModel.query.get(product_id)
		error = False
		if not product:
			message = 'Product does not exist'
		if product:
			try:
				product.featured = 0
				_db.session.add(product)
				_db.session.commit()
				message = 'Product unfeatured'
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
				'result': product.to_json()
			})
		return response

	def delete_products_gallery(self, _db, product_gallery_id):
		product_gallery = ProductAttachmentsModel.query.get(product_gallery_id)
		if not product_gallery:
			message = 'Image does not exist'
		if product_gallery:
			os.remove(os.path.join(product_upload_folder, product_gallery.name))
			_db.session.delete(product_gallery)
			_db.session.commit()
			message = 'Image successfully deleted'		
		response = jsonify({
			'message': message, 
			'result': product_gallery_id
		})
		return response

	def retrieve_products_by_vendor(self, vendor_id):
		vendor = ProductVendorMappingModel.query.filter_by(vendor_id=vendor_id).order_by(ProductVendorMappingModel.id.desc()).all()
		items = []
		message = ''
		if vendor:
			for product in vendor:
				row = ProductsModel.query.get(product.product_id)
				category = ProductCategoryMappingModel.query.filter_by(product_id=product.product_id).first()
				products_gallery=[]
				products_attachment = ProductAttachmentsModel.query.filter_by(product_id=row.id)
				for products in products_attachment:
					products_gallery.append({
						"name": products.name,
						"path": products.path,
						"product_id": products.product_id
					})
				items.append({
					"id": row.id,
					"name": row.name,
					"price": row.price,
					"sale_price": row.sale_price,
					"slug": row.slug,
					"sku": row.sku,
					"featured": row.featured,
					'is_verified': row.is_verified,
					'vendor_id': vendor_id,
					"quantity": row.quantity,
					"cart_quantity": 1,
					"description": row.description,
					"image_path": row.image_path,
					'product_category_id': category.category_id,
					"product_category": CategoriesModel.query.get(category.category_id).name,
					"products_gallery": products_gallery
				})
		else:
			message = 'No product found for vendor'
		response = jsonify({
			'results': items, 
			'message': message
		})
		return response

	def retrieve_verified_products_by_vendor(self, vendor_id):
		vendor = ProductVendorMappingModel.query.filter_by(vendor_id=vendor_id).all()
		items = []
		message = ''
		if vendor:
			for product in vendor:
				row = ProductsModel.query.filter_by(id=product.product_id, is_verified=1).first()
				category = ProductCategoryMappingModel.query.filter_by(product_id=product.product_id).first()
				products_gallery=[]
				products_attachment = ProductAttachmentsModel.query.filter_by(product_id=row.id)
				for products in products_attachment:
					products_gallery.append({
						"name": products.name,
						"path": products.path,
						"product_id": products.product_id
					})
				items.append({
					"id": row.id,
					"name": row.name,
					"price": row.price,
					"sale_price": row.sale_price,
					"slug": row.slug,
					"sku": row.sku,
					"featured": row.featured,
					'is_verified': row.is_verified,
					'vendor_id': vendor_id,
					"quantity": row.quantity,
					"cart_quantity": 1,
					"description": row.description,
					"image_path": row.image_path,
					'product_category_id': category.category_id,
					"product_category": CategoriesModel.query.get(category.category_id).name,
					"products_gallery": products_gallery
				})
		else:
			message = 'No product found for vendor'
		response = jsonify({
			'results': items, 
			'message': message
		})
		return response