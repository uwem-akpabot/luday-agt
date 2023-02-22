from app import create_app
# from app.models import BlogsModel

flask_app = create_app()

def test_get_user_order_details_or_404():
    with flask_app.test_client() as test_client:
        response = test_client.get('/api/order/user')
        assert response.status_code == 200


def test_get_guest_order_details_by_id_or_404():
    with flask_app.test_client() as test_client:
        order_id = 1
        response = test_client.get(f'/api/order/{order_id}')
        assert response.status_code == 200


def test_get_order_by_vendor_user_id_or_404():
    with flask_app.test_client() as test_client:
        vendor_id = 1
        response = test_client.get(f'/api/order/vendor/{vendor_id}')
        assert response.status_code == 200


def test_get_order_details_by_id_or_404():
    with flask_app.test_client() as test_client:
        order_id = 1
        response = test_client.get(f'/api/order/mapping/{order_id}')
        assert response.status_code == 200


def test_get_order_by_ref_and_trxref_id():
    with flask_app.test_client() as test_client:
        response = test_client.get(f'/api/order/reference')
        assert response.status_code == 200


def test_get_all_order():
    with flask_app.test_client() as test_client:
        response = test_client.get(f'/api/order/all')
        assert response.status_code == 200


def test_search_orders():
    with flask_app.test_client() as test_client:
        search_param = "random"
        response = test_client.get(f'/api/order/search/{search_param}')
        assert response.status_code == 200


def test_search_orders_by_date():
    with flask_app.test_client() as test_client:
        response = test_client.get(f'/api/order/sort')
        assert response.status_code == 200


def test_search_orders_by_payment():
    with flask_app.test_client() as test_client:
        payment_query = "some data"
        response = test_client.get(f'/api/order/payment/{payment_query}')
        assert response.status_code == 200


def test_search_orders_by_delivery():
    with flask_app.test_client() as test_client:
        delivery_query = "some data"
        response = test_client.get(f'/api/order/payment/{delivery_query}')
        assert response.status_code == 200


def test_update_order_by_ref_id():
    with flask_app.test_client() as test_client:
        response = test_client.put(f'/api/order/trxref', data={

        })
        assert response.status_code == 200


def test_update_order_billing_address_id_by_ref_id():
    with flask_app.test_client() as test_client:
        response = test_client.put(f'/api/order/billing-address', data={

        })
        assert response.status_code == 200


def test_search_vendor_orders_view_by_product_sku():
    with flask_app.test_client() as test_client:
        search_param = "some data"
        vendor_id = 1
        response = test_client.get(f'/api/order/vendor/search/{search_param}/{vendor_id}')
        assert response.status_code == 200


def test_search_vendor_orders_view_by_purchase_date():
    with flask_app.test_client() as test_client:
        vendor_id = 1
        response = test_client.get(f'/api/order/vendor/{vendor_id}/sort')
        assert response.status_code == 200


def test_search_vendor_orders_view_by_delivery_status():
    with flask_app.test_client() as test_client:
        search_param = "some data"
        vendor_id = 1
        response = test_client.get(f'/order/vendor/delivery/{vendor_id}/{search_param}')
        assert response.status_code == 200

            









