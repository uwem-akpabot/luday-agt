from app import create_app
# from app.models import ProductsModel

flask_app = create_app()

def test_get_categories():
    with flask_app.test_client() as test_client:
        response = test_client.get('api/categories')
        assert response.status_code == 200


def test_add_categories():
    with flask_app.test_client() as test_client:
        response = test_client.post('/api/categories', data={})
        assert response.status_code == 200


def test_get_single_category():
    with flask_app.test_client() as test_client:
        category_id = 1
        response = test_client.get(f'/api/categories/{category_id}')
        assert response.status_code == 200


def test_update_category():
    with flask_app.test_client() as test_client:
        category_id = 1
        response = test_client.put(f'/api/categories/{category_id}', data={})
        assert response.status_code == 200


def test_delete_category():
    with flask_app.test_client() as test_client:
        category_id = 1
        response = test_client.delete(f'/api/categories/{category_id}')
        assert response.status_code == 200


def test_retrieve_products_by_category():
    with flask_app.test_client() as test_client:
        slug= 1
        response = test_client.get(f'/api/categories/{slug}/products')
        assert response.status_code == 200


def test_retrieve_products_by_vendor():
    with flask_app.test_client() as test_client:
        user_id = 1
        response = test_client.get(f'/api/vendors/{user_id}/products')
        assert response.status_code == 200


def test_retrieve_verified_products_by_vendor():
    with flask_app.test_client() as test_client:
        vendor_id = 1
        response = test_client.get(f'/api/vendors/products/{vendor_id}/verified')
        assert response.status_code == 200








