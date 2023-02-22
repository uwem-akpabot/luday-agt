
from sqlalchemy import select, delete, orm as db_orm
from datetime import datetime
from sqlalchemy import event
from slugify import slugify

from . import db
from app.constants import OrderStatus, DeliveryStatus

class CategoriesModel(db.Model):
	__tablename__ = 'categories'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text, nullable=False)
	slug = db.Column(db.Text, nullable=True)
	description = db.Column(db.Text, unique=False, nullable=False)
	image_name = db.Column(db.Text, unique=False, nullable=True)
	image_path = db.Column(db.Text, unique=False, nullable=True)
	created_at = db.Column(db.DateTime, default=datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

	category_mapping = db.relationship('ProductCategoryMappingModel', backref="categories", passive_deletes=True)

	@staticmethod
	def generate_slug(target, value, oldvalue, initiator):
		if value and (not target.slug or value != oldvalue):
			target.slug = slugify(value)

	def __repr__(self):
		return '<CategoriesModel {}-{}-{}-{}-{}-{}>'.format(self.id, self.name, self.slug, self.description, self.image_name, self.image_path)

	def to_json(self):
		return {
			'id': self.id,
			'name': self.name, 
			'slug': self.slug,
			'description': self.description,
			'image_name': self.image_name,
			'image_path': self.image_path
		}

event.listen(CategoriesModel.name, 'set', CategoriesModel.generate_slug, retval=False)

class SubCategoriesModel(db.Model):
	__tablename__ = 'subcategories'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	slug = db.Column(db.String(150), nullable=True)
	created_at = db.Column(db.DateTime, default=datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

	@staticmethod
	def generate_slug(target, value, oldvalue, initiator):
		if value and (not target.slug or value != oldvalue):
			target.slug = slugify(value)

	def __repr__(self):
		return '<SubCategoriesModel {}-{}-{}>'.format(self.id, self.name, self.slug)

	def to_json(self):
		return {
			'id': self.id,
			'name': self.name, 
			'slug': self.slug
		}

event.listen(SubCategoriesModel.name, 'set', SubCategoriesModel.generate_slug, retval=False)


class ProductsModel(db.Model):
	__tablename__ = 'products'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text, nullable=False)
	slug = db.Column(db.Text, nullable=True)
	description = db.Column(db.Text, unique=False, nullable=False)
	quantity = db.Column(db.Integer, nullable=True)
	price = db.Column(db.Float, nullable=False)
	sale_price = db.Column(db.Float, nullable=True)
	sku = db.Column(db.Text, nullable=True)
	featured = db.Column(db.Integer, nullable=True)
	image_name = db.Column(db.Text, unique=False, nullable=True)
	image_path = db.Column(db.Text, unique=False, nullable=True)
	status = db.Column(db.Integer, default=0)
	is_verified = db.Column(db.Integer, default=0)
	created_at = db.Column(db.DateTime, default=datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

	order_product_mapping = db.relationship('OrderProductMapping', backref="products", passive_deletes=True)
	product_mapping = db.relationship('ProductCategoryMappingModel', backref="products", passive_deletes=True)
	attachment_mapping = db.relationship('ProductAttachmentsModel', backref="products", passive_deletes=True)
	

	@staticmethod
	def generate_slug(target, value, oldvalue, initiator):
		if value and (not target.slug or value != oldvalue):
			target.slug = slugify(value)
	
	def __repr__(self):
		return '<Product %r>' % self.name

	def to_json(self):
		return {
			'id': self.id,
			'name': self.name, 
			'slug': self.slug,
			'description': self.description,
			'quantity': self.quantity,
			'price' : self.price,
			'sale_price': self.sale_price,
			'sku': self.sku,
			'featured': self.featured,
			'image_name': self.image_name,
			'image_path': self.image_path,
			'cart_quantity': 1
		}

event.listen(ProductsModel.name, 'set', ProductsModel.generate_slug, retval=False)

class ProductCategoryMappingModel(db.Model):
	__tablename__ = 'product_category_mapping'

	id = db.Column(db.Integer, primary_key=True)
	product_id = db.Column(db.Integer, db.ForeignKey('products.id', ondelete="CASCADE"), nullable=False)
	category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete="CASCADE"), nullable=False)
	created_at = db.Column(db.DateTime, default=datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

	def __repr__(self):
		return '<ProductCategoryMappingModel {}-{}-{}>'.format(self.id, self.product_id, self.category_id)

	def to_json(self):
		return {
			'id': self.id,
			'product_id': self.product_id, 
			'category_id': self.category_id
		}

class ProductVendorMappingModel(db.Model):
	__tablename__ = 'product_vendor_mapping'

	id = db.Column(db.Integer, primary_key=True)
	product_id = db.Column(db.Integer, db.ForeignKey('products.id', ondelete='CASCADE'), nullable=False)
	vendor_id = db.Column(db.Integer, nullable=False)
	created_at = db.Column(db.DateTime, default=datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

	def __repr__(self):
		return '<ProduuctVendorMappingModel {}-{}-{}>'.format(self.id, self.vendor_id, self.product_id)

	def to_json(self):
		return {
			'id': self.id,
			'vendor_id': self.vendor_id, 
			'product_id': self.product_id
		}
class ProductAttachmentsModel(db.Model):
	__tablename__ = 'product_attachments'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text, nullable=False)
	path = db.Column(db.Text, nullable=False)
	product_id = db.Column(db.Integer, db.ForeignKey('products.id', ondelete="CASCADE"), nullable=False)
	created_at = db.Column(db.DateTime, default=datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

	def __repr__(self):
		return '<ProductAttachmentsModel {}-{}-{}-{}>'.format(self.id, self.name, self.path, self.product_id)

	def to_json(self):
		return {
			'id': self.id,
			'name': self.name,
			'path': self.path,
			'product_id': self.product_id
		}


class Orders(db.Model):
	__tablename__ = 'orders'

	id = db.Column(db.Integer, primary_key=True)
	ref_transaction_id = db.Column(db.Text, nullable=True)
	ref_order_id = db.Column(db.Integer, nullable=True)
	ref_id = db.Column(db.Text, nullable=True)
	split_code = db.Column(db.Text, nullable=True)
	first_name = db.Column(db.String(30), index=True, nullable=False)
	last_name = db.Column(db.String(30), index=True, nullable=True)
	mobile_number = db.Column(db.String(15), index=True, nullable=True)
	user_id = db.Column(db.Integer, nullable=True)
	email = db.Column(db.Text, nullable=True)
	amount = db.Column(db.Float)
	currency = db.Column(db.String(5), index=True, nullable=False)
	tax = db.Column(db.Float, nullable=True)
	billing_address_id = db.Column(db.Text, nullable=True)
	status = db.Column("status", db.Enum("New", "Pending", "Failed", "Successful"), default="New")
	delivery_status = db.Column("delivery_status", db.Enum("Pending","Shipped", "Delivered"), default="Delivered")
	created_at = db.Column(db.DateTime, index=True, default=datetime.now)
	updated_at = db.Column(db.DateTime, index=True, default=datetime.now, 
							onupdate=datetime.now)

	order_product_mapping = db.relationship('OrderProductMapping', backref="orders", passive_deletes=True)
	
	def __repr__(self):
		return '<Orders {}>'.format(self.id)

	
	def to_dict(self):
		return {
			'id': self.id,
			'ref_transaction_id': self.ref_transaction_id,
			'ref_order_id': self.ref_order_id,
			'ref_id': self.ref_id,
			'split_code': self.split_code,
			'first_name': self.first_name,
			'last_name': self.last_name,
			'mobile_number': self.mobile_number,
			'user_id': self.user_id,
			'email': self.email,
			'amount': self.amount,
			'currency': self.currency, 
			'tax': self.tax,
			'billing_address_id': self.billing_address_id,
			'status': self.status,
			'delivery_status': self.delivery_status,
			'created_at': self.created_at,
			'updated_at': self.updated_at
		}

class OrderProductMapping(db.Model):
	__tablename__ = 'order_product_mapping'

	id = db.Column(db.Integer, primary_key=True)
	product_id = db.Column(db.Integer, db.ForeignKey('products.id', ondelete="CASCADE"), nullable=False)
	order_id = db.Column(db.Integer, db.ForeignKey('orders.id', ondelete="CASCADE"), nullable=False)
	quantity = db.Column(db.Integer)
	price = db.Column(db.Float, nullable=True)
	user_id = db.Column(db.Integer, nullable=True)
	vendor_id = db.Column(db.Integer, nullable=True)
	email = db.Column(db.Text, nullable=True)
	created_at = db.Column(db.DateTime, index=True, default=datetime.now)
	updated_at = db.Column(db.DateTime, index=True, default=datetime.now, onupdate=datetime.now)

	def __repr__(self):
		return '<Ordered Products ID: {}>'.format(self.order_id)


	def to_dict(self):
		return {
			'id': self.id,
			'product_id': self.product_id,
			'order_id': self.order_id,
			'quantity': self.quantity,
			'price': self.price,
			'user_id': self.user_id,
			'email': self.email,
			'created_at': self.created_at,
			'updated_at': self.updated_at
		}