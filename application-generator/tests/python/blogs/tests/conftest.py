import pytest
from app import create_app

# This fixture creates a test client using a context manager
@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('flask_test.cfg')

    # create a test client using the flask application configured for testing
    with flask_app.test_client() as testing_client:
        # establish an application context
        with flask_app.app_context():
            yield testing_client # testing occurs here


