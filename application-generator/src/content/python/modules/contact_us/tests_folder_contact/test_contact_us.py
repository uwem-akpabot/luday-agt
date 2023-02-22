from app import create_app
import io

flask_app = create_app()
        


def test_get_contact_us():
    with flask_app.test_client() as test_client:
        response = test_client.get('/api/contact')
        assert response.status_code == 200
        assert b'xx' in response.data


def test_post_contct_us_details():
    with flask_app.test_client() as test_client:
        response = test_client.post('api/contact/add', data={
                                        "name":"Excel",
                                        "subject":"HELP",
                                        "email":"excel.luday.se",
                                        "mobile":"26780157",
                                        "mssg":"I need help with pytest"
                                    })
        assert b'1' in response.data


