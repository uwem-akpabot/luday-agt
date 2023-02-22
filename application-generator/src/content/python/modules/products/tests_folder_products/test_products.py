from app import create_app
# from app.models import ProductsModel

flask_app = create_app()

def test_get_products():
    with flask_app.test_client() as test_client:
        response = test_client.get('/api/products')
        assert response.status_code == 200


def test_get_products_by_slug():
    with flask_app.test_client() as test_client:
        slug = ""
        response = test_client.get(f'/api/products/details/{slug}')
        assert response.status_code == 200


def test_search_products():
    with flask_app.test_client() as test_client:
        search_query = ""
        response = test_client.get(f'/api/products/{search_query}')
        assert response.status_code == 200


def test_update_product():
    with flask_app.test_client() as test_client:
        product_id = 1
        response = test_client.put(f'/api/products/{product_id}', data={})
        assert response.status_code == 200


def test_verify_product():
    with flask_app.test_client() as test_client:
        product_id = 1
        response = test_client.put(f'/api/products/{product_id}/verify', data={})
        assert response.status_code == 200


def test_verify_all_product():
    with flask_app.test_client() as test_client:
        response = test_client.put(f'/api/products/verify/all', data={})
        assert response.status_code == 200


def test_feature_product():
    with flask_app.test_client() as test_client:
        product_id = 1
        response = test_client.put(f'/api/products/{product_id}/feature', data={})
        assert response.status_code == 200


def test_unfeature_product():
    with flask_app.test_client() as test_client:
        product_id = 1
        response = test_client.put(f'/api/products/{product_id}/unfeature', data={})
        assert response.status_code == 200


def test_get_single_product():
    with flask_app.test_client() as test_client:
        product_id = 1
        response = test_client.get(f'/api/products/{product_id}')
        assert response.status_code == 200


def test_get_count_of_product():
    with flask_app.test_client() as test_client:
        response = test_client.get('/api/products/count')
        assert response.status_code == 200


def test_get_featured_product():
    with flask_app.test_client() as test_client:
        response = test_client.get('/api/products/featured')
        assert response.status_code == 200


def test_get_unverified_products():
    with flask_app.test_client() as test_client:
        response = test_client.get('/api/products/unverified')
        assert response.status_code == 200


def test_get_verified_products():
    with flask_app.test_client() as test_client:
        response = test_client.get('/api/products/verified')
        assert response.status_code == 200


def test_delete_product():
    with flask_app.test_client() as test_client:
        product_id = 1
        response = test_client.delete(f'/api/products/{product_id}')
        assert response.status_code == 200


def test_delete_products_gallery():
    with flask_app.test_client() as test_client:
        products_gallery_id = 1
        response = test_client.delete(f'/api/products/{products_gallery_id}/gallery')
        assert response.status_code == 200








