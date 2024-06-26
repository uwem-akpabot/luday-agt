# Create a test client using the Flask application configured for testing
import pytest
import config
from app import db
import app
from app.models import User

@pytest.fixture
def client():
    app.config.from_object(config.TestingConfig)
    with app.test_client() as client: # app.test_client() is a function that returns a Flask application configured for testing
        with app.app_context(): # This is required to initialize the database
            yield client # yield is used to return the client to the test function

@pytest.fixture()
def init_database():
    # Create the database and the database table
    db.create_all()

    # List of test users
    test_users = [
        {"name": "Test User 1", "email": "test1@gmail.com", "password": "12345"},
        {"name": "Test User 2", "email": "test2@gmail.com", "password": "12345"},
        {"name": "Test User 3", "email": "test3@gmail.com", "password": "12345"},
    ]

    # Convert the list of dictionaries to a list of User objects
    def create_post_model(user):
        return User(**user)

    # Create a list of User objects
    mapped_users = map(create_post_model, test_users)
    t_users = list(mapped_users)

    # Add the users to the database - add_all() is used to add multiple records
    db.session.add_all(t_users)

    # Commit the changes for the users
    db.session.commit()

    yield db  # this is where the testing happens!
    db.session.remove()  # looks like db.session.close() would work as well
    # Drop the database table
    db.drop_all()