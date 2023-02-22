"""
README NOTES ON PYTEST IN AGT

1. From ... luday-dev\application-generator\generated\www.bestdealnaija.com\api\blogs>
Activate venv and start the server "py run.py"

2. From ... luday-dev\application-generator\generated>
Run the test  "pytest"

(Fix) Under "generated/www.bestdealnaija.com", create an "images" folder and "blogs" folder under it.
"""

from app import create_app
from app.models import BlogsModel
import io

flask_app = create_app()

"""
GET BLOG SECTION
"""
def test_getting_all_blogs():
    with flask_app.test_client() as test_client:
        response = test_client.get('/api/blogs')
        assert response.status_code == 200
        assert BlogsModel.query.count() > 0
        assert b'Some long content' in response.data

def test_getting_specific_blog():
    with flask_app.test_client() as test_client:
        response = test_client.get('/api/blogs/3')
        assert response.status_code == 200
        assert BlogsModel.query.count() > 0
        assert b'Sample' in response.data

def test_getting_single_blog_with_invalid_id():
    with flask_app.test_client() as test_client:
        blog_id = 99
        response = test_client.get(f'/api/blogs/{blog_id}')
        assert b"Blog post does not exist" in response.data

# def test_displaying_correct_msg_if_blog_is_empty():
#     with flask_app.test_client() as test_client:
#         response = test_client.get('/api/blogs')
#         # assert BlogsModel.query.count() == 0  #set this to zero when u run this test
#         # assert b'empty' in response.data    #*** THIS TEST HAS FAILED


"""
POST BLOG SECTION
"""
def test_post_blog_with_valid_image_extension_and_blog_image():
    with flask_app.test_client() as test_client:

        image_name = "1.png"
        image_path = fr"C:\Users\akpab\OneDrive\Desktop\{image_name}"

        response = test_client.post('/api/blogs', 
                                    data={"title":"Newest", 
                                    "summary":"all about tech", 
                                    "content":"New trials", 
                                    "blog_image":(open(image_path, 'rb'), image_name) }, 
                                    content_type='multipart/form-data')
        assert b"Blog posted successfully" in response.data


def test_posting_blog_without_uploading_blog_image():
    with flask_app.test_client() as test_client:
        response = test_client.post('/api/blogs', 
                                    data={"title":"images", 
                                    "summary":"all about tech", 
                                    "content":"this should be long but ko neccestri"}, 
                                    content_type='multipart/form-data')
        assert b"At least one image is required for blog" in response.data


# def test_post_blog_with_invalid_image_extension():
#     with flask_app.test_client() as test_client:

#         image_name = "1.docx"
#         image_path = fr"C:\Users\akpab\OneDrive\Desktop\{image_name}"

#         response = test_client.post('/api/blogs', 
#                                     data={"title":"Newest", 
#                                     "summary":"all about tech", 
#                                     "content":"New trials", 
#                                     "blog_image":(open(image_path, 'rb'), image_name) }, 
#                                     content_type='multipart/form-data')
#         assert b"Image filetype not valid" in response.data


# def test_post_blog_with_non_existing_blog_image():
#     with flask_app.test_client() as test_client:

#         image_name = "notexist.png"
#         image_path = fr"C:\Users\akpab\OneDrive\Desktop\{image_name}"

#         response = test_client.post('/api/blogs', 
#                                     data={"title":"Newest", 
#                                     "summary":"all about tech", 
#                                     "content":"New trials", 
#                                     "blog_image":(open(image_path, 'rb'), image_name) }, 
#                                     content_type='multipart/form-data')
#         assert b"Image filetype not valid" in response.data

"""
UPDATE BLOG SECTION
"""
def test_update_blog_with_valid_image_extension_and_blog_image():
    with flask_app.test_client() as test_client:
        blog_id = 4

        image_name = "1.png"
        image_path = fr"C:\Users\akpab\OneDrive\Desktop\{image_name}"

        response = test_client.put(f'/api/blogs/{blog_id}', 
                                    data={"title":"UPDATED", 
                                    "summary":"Not so random", 
                                    "content":"Newer different", 
                                   "blog_image":(open(image_path, 'rb'), "img.txt") }, 
                                    content_type='multipart/form-data')
        assert b"Blog post updated successfully" in response.data


# def test_update_blog_with_invalid_image_extension():
#     with flask_app.test_client() as test_client:
#         blog_id = 4

#         image_name = "1.png"
#         image_path = fr"C:\Users\akpab\OneDrive\Desktop\{image_name}"

#         response = test_client.put(f'/api/blogs/{blog_id}', 
#                                     data={"title":"UPDATED", 
#                                     "summary":"Not so random", 
#                                     "content":"Newer different", 
#                                    "blog_image":(open(image_path, 'rb'), "img.txt") }, 
#                                     content_type='multipart/form-data')
#         assert b"Blog post updated successfully" in response.data

"""
DELETE BLOG SECTION
"""
# def test_deleting_blogpost_with_valid_id():
#     with flask_app.test_client() as test_client:
#         blog_id = 2
#         response = test_client.delete(f'/api/blogs/{blog_id}')
#         assert response.status_code == 200
#         assert b"Blog post successfully deleted" in response.data

        
#  -------------------------------------------------------------------------

# def test_get_count_of_blogs():
#     with flask_app.test_client() as test_client:
#         response = test_client.get('/api/blogs/count')
#         count = BlogsModel.query.count()
#         valid_count = bytes(str(count), 'utf-8')
#         assert valid_count in response.data

