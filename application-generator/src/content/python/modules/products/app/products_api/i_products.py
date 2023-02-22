from abc import ABC, abstractmethod

class IProducts(ABC):
	@abstractmethod
	def paginate_results(self, request, selection):
		pass

	@abstractmethod
	def generateSKU(self, category, product_name, quantity):
		pass

	@abstractmethod
	def add_products(self, _db):
		pass

	@abstractmethod
	def handle_images_upload(self, _db, images_array, name, product_id):
		pass
	
	@abstractmethod
	def get_products(self, _db):
		pass

	@abstractmethod
	def search_products(self):
		pass

	@abstractmethod
	def get_products_by_slug(self, slug):
		pass

	@abstractmethod
	def get_count_of_products(self):
		pass

	@abstractmethod
	def get_featured_products(self):
		pass

	@abstractmethod
	def get_single_product(self, _db, product_id):
		pass

	@abstractmethod
	def update_product(self, _db, product_id):
		pass

	@abstractmethod
	def delete_products(self, _db, product_id):
		pass

	@abstractmethod
	def get_unverified_products(self, _db):
		pass

	@abstractmethod
	def get_verified_products(self, _db):
		pass

	@abstractmethod
	def verify_product(self, _db, product_id):
		pass

	@abstractmethod
	def unverify_product(self, _db, product_id):
		pass

	@abstractmethod
	def verify_all_products(self, _db):
		pass

	@abstractmethod
	def feature_product(self, _db, product_id):
		pass

	@abstractmethod
	def unfeature_product(self, _db, product_id):
		pass

	@abstractmethod
	def allowed_file(self, filename, allowed_extensions):
		pass

	@abstractmethod
	def add_categories(self, _db):
		pass

	@abstractmethod
	def get_categories(self):
		pass

	@abstractmethod
	def get_single_category(self, category_id):
		pass

	@abstractmethod
	def update_category(self, _db, category_id):
		pass

	@abstractmethod
	def delete_categories(self, _db, category_id):
		pass

	@abstractmethod
	def retrieve_products_by_category(category_id):
		pass

	@abstractmethod
	def delete_products_gallery(self, _db, product_gallery_id):
		pass

	@abstractmethod
	def retrieve_products_by_vendor(self, vendor_id):
		pass