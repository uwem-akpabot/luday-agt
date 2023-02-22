from app import create_app
from app.models import CategoriesModel

"""
GIVEN THAT BestDealNaija is configured for testing 
WHEN the '/categories' page is requested (GET) 
THEN verify that the response is valid 
"""
flask_app = create_app()
        
def test_categories_with_fixture():
    with flask_app.test_client() as test_client:
        response = test_client.get('api/categories')
        assert response.status_code == 200
        assert b"Wine" in response.data
        assert CategoriesModel.query.count() > 0

def test_categories2():
    with flask_app.test_client() as test_client:
        response = test_client.get('/api/categories')
        assert response.status_code == 200
        assert b"The description" in response.data
        assert CategoriesModel.query.count() > 0

# flask_app = create_app()

# # create a test client using the flask application configured for testing
# with flask_app.test_client() as test_client:
#     response = test_client.get('/api/categories')
#     assert response.status_code == 200
#     assert b"cream" in response.data
#     assert CategoriesModel.query.count() > 0
    