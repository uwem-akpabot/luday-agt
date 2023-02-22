from app import create_app
from app.models import BlogsModel

flask_app = create_app()

def test_get_blogs():
    with flask_app.test_client() as test_client:
        response = test_client.get('/api/blog')
        assert response.status_code == 200

# def test_get_single_blog_by_id():
#     with flask_app.test_client() as test_client:
#         blog_id = 1
#         response = test_client.get(f'/api/blogs/{blog_id}')
#         valid_blog_id = bytes(str(blog_id), 'utf-8')
#         assert valid_blog_id in response.data

def test_get_single_blog_with_invalid_id():
    with flask_app.test_client() as test_client:
        blog_id = 99
        response = test_client.get(f'/api/blogs/{blog_id}')
        assert b"Blog post does not exist" in response.data     

# def test_post_blog_with_valid_image_extension_and_blog_image():
#     with flask_app.test_client() as test_client:

#         image_name = "1.jpg"
#         image_path = fr"C:\Users\akugb\Desktop\{image_name}"

#         response = test_client.post('/api/blogs', 
#                                     data={"title":"picturkkes", 
#                                     "summary":"all about tech", 
#                                     "content":"new new", 
#                                     "blog_image":(open(image_path, 'rb'), image_name) }, 
#                                     content_type='multipart/form-data')
#         assert b"Blog posted successfully" in response.data

# def test_post_blog_with_invalid_image_extension():
#     with flask_app.test_client() as test_client:

#         image_name = "1.jpg"
#         image_path = fr"C:\Users\akugb\Desktop\{image_name}"


#         response = test_client.post('/api/blogs', 
#                                     data={"title":"images", 
#                                     "summary":"all about tech", 
#                                     "content":"this should be long but ko neccestri", 
#                                     "blog_image":(open(image_path, 'rb'), "img.txt") }, 
#                                     content_type='multipart/form-data')
#         assert b"Image filetype not valid" in response.data

def test_post_blog_without_blog_image():
    with flask_app.test_client() as test_client:
        response = test_client.post('/api/blogs', 
                                    data={"title":"images", 
                                    "summary":"all about tech", 
                                    "content":"this should be long but ko neccestri"}, 
                                    content_type='multipart/form-data')
        assert b"At least one image is required for blog" in response.data

# def test_update_blog_with_valid_image_extension_and_blog_image():
#     with flask_app.test_client() as test_client:
#         blog_id = 71

#         image_name = "1.jpg"
#         image_path = fr"C:\Users\akugb\Desktop\{image_name}"

#         response = test_client.put(f'/api/blogs/{blog_id}', 
#                                     data={"title":"goes", 
#                                     "summary":"purely random", 
#                                     "content":"something different", 
#                                    "blog_image":(open(image_path, 'rb'), "img.txt") }, 
#                                     content_type='multipart/form-data')
#         assert b"Blog post updated successfully" in response.data







# def test_update_blog_with_invalid_image_extension():
#     with flask_app.test_client() as test_client:
#         blog_id = 2
#         response = test_client.put(f'/api/blogs/{blog_id}', 
#                                     data={"title":"pictures", 
#                                     "summary":"purely random", 
#                                     "content":"something different", 
#                                     "blog_image":(io.BytesIO(b'picture'), "images.g"), }, 
#                                     content_type='multipart/form-data')
#         assert b"Blog post updated successfully" in response.data



# def test_delete_blogpost_with_valid_id():
#     with flask_app.test_client() as test_client:
#         blog_id = 72
#         response = test_client.delete(f'/api/blogs/{blog_id}')
#         assert response.status_code == 200
#         assert b"Blog post successfully deleted" in response.data
        

# def test_delete_blogpost_with_invalid_id():
#     with flask_app.test_client() as test_client:
#         blog_id = 74
#         response = test_client.delete(f'/api/blogs/{blog_id}')
#         assert response.status_code == 200
#         assert b"Blog post does not exist" in response.data
        
   
# def test_get_blogs_by_slugs():
#     with flask_app.test_client() as test_client:
#         slug = "images"
#         response = test_client.get(f'/api/sblog/{slug}')
#         valid_slug = bytes(slug, 'utf-8')
#         assert valid_slug in response.data


# def test_get_blogs_by_non_existing_slug():
#     with flask_app.test_client() as test_client:
#         slug = "imags"
#         response = test_client.get(f'/api/sblog/{slug}')
#         assert b"Blog not found" in response.data


# def test_get_count_of_blogs():
#     with flask_app.test_client() as test_client:
#         response = test_client.get('/api/blogs/count')
#         count = BlogsModel.query.count()
#         valid_count = bytes(str(count), 'utf-8')
#         assert valid_count in response.data


# def test_search_blogs():
#     with flask_app.test_client() as test_client:
#         response = test_client.post('/api/blogs/search', data={"search_term":"goes"})
#         assert b"pic" in response.data

