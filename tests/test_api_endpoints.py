import pytest
from http import HTTPStatus
from utils.test_data import TestData
from utils.api_client import APIClient
from typing import Dict, Any

class TestUserAPI:
    """Test suite for User API endpoints"""

    def test_get_users_list(self, api_client: APIClient):
        """Test getting list of users"""
        # Arrange & Act
        response = api_client.get('/users')
        
        # Assert
        assert response['status_code'] == HTTPStatus.OK
        assert isinstance(response['data'], list)

    def test_create_user(self, api_client: APIClient):
        """Test creating a new user"""
        # Arrange
        payload = TestData.get_user_payload()
        
        # Act
        response = api_client.post('/users', json=payload)
        
        # Assert
        assert response['status_code'] == HTTPStatus.CREATED
        assert response['data']['name'] == payload['name']
        assert response['data']['email'] == payload['email']

    def test_update_user(self, api_client: APIClient):
        """Test updating an existing user"""
        # Arrange
        user_id = "123"  # You might want to create a user first and get their ID
        payload = TestData.get_user_update_payload()
        
        # Act
        response = api_client.put(f'/users/{user_id}', json=payload)
        
        # Assert
        assert response['status_code'] == HTTPStatus.OK
        assert response['data']['name'] == payload['name']
        assert response['data']['age'] == payload['age']

    def test_delete_user(self, api_client: APIClient):
        """Test deleting a user"""
        # Arrange
        user_id = "123"  # You might want to create a user first and get their ID
        
        # Act
        response = api_client.delete(f'/users/{user_id}')
        
        # Assert
        assert response['status_code'] == HTTPStatus.NO_CONTENT

    @pytest.mark.parametrize("invalid_payload", [
        {},
        {"name": ""},
        {"email": "invalid_email"},
        {"name": "John", "email": "john@example.com", "age": "invalid"}
    ])
    def test_create_user_invalid_data(self, api_client: APIClient, invalid_payload: Dict[str, Any]):
        """Test creating user with invalid data"""
        # Act
        response = api_client.post('/users', json=invalid_payload)
        
        # Assert
        assert response['status_code'] == HTTPStatus.BAD_REQUEST 