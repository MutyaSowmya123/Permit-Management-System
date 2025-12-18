import pytest
from app import create_app, db
from app.models import User

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_register(client):
    response = client.post('/api/auth/register', json={
        'username': 'testuser',
        'password': 'testpass123'
    })
    assert response.status_code == 201
    assert b'Registered successfully' in response.data

def test_register_duplicate_username(client):
    # First registration
    client.post('/api/auth/register', json={
        'username': 'testuser',
        'password': 'testpass123'
    })

    # Duplicate registration
    response = client.post('/api/auth/register', json={
        'username': 'testuser',
        'password': 'testpass123'
    })
    assert response.status_code == 409
    assert b'Username already exists' in response.data

def test_login(client):
    # Register first
    client.post('/api/auth/register', json={
        'username': 'testuser',
        'password': 'testpass123'
    })

    # Login
    response = client.post('/api/auth/login', json={
        'username': 'testuser',
        'password': 'testpass123'
    })
    assert response.status_code == 200
    assert 'access_token' in response.get_json()

def test_login_invalid_credentials(client):
    response = client.post('/api/auth/login', json={
        'username': 'nonexistent',
        'password': 'wrongpass'
    })
    assert response.status_code == 401
    assert b'Invalid credentials' in response.data
