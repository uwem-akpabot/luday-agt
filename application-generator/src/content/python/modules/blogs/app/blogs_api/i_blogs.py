from abc import ABC, abstractmethod

class IBlogs(ABC):
	@abstractmethod
	def get_blogs(self, _db):
		pass
	
	@abstractmethod
	def add_blogs(self, _db):
		pass

	@abstractmethod
	def paginate_results(self, request, selection):
		pass

	@abstractmethod
	def search_blogs(self):
		pass

	@abstractmethod
	def get_blogs_by_slug(self, slug):
		pass

	@abstractmethod
	def get_count_of_blogs(self):
		pass

	@abstractmethod
	def get_single_blog(self, _db, blog_id):
		pass

	@abstractmethod
	def update_blog(self, _db, blog_id):
		pass

	@abstractmethod
	def delete_blogs(self, _db, blog_id):
		pass

	@abstractmethod
	def allowed_file(self, filename, allowed_extensions):
		pass
