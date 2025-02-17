import pytest
from http import HTTPStatus
from utils.test_data import TestData
from utils.validators import validate_schema
from utils.api_client import APIClient
from schemas.schema_loader import UserSchemas
from constants.endpoints import UserEndpoints
from typing import Dict, Any

class TestReqResAPI:
    """Test suite for ReqRes API endpoints"""

    def test_get_users_list_with_schema_validation(self, api_client: APIClient):
        """Test getting list of users with schema validation"""
        # Arrange
        schema = UserSchemas.get_users_list()
        
        # Act
        response = api_client.get(f"{UserEndpoints.GET_USERS_LIST.value}?page=2")
        
        # Assert
        validate_schema(
            response=response,
            schema=schema,
            error_message="Users list response schema validation failed"
        )
        assert response['page'] == 2
        assert response['per_page'] == 6
        assert isinstance(response['data'], list)
        assert 'total' in response

    def test_get_single_user_with_schema_validation(self, api_client: APIClient):
        """Test getting a single user with schema validation"""
        # Arrange
        user_id = 2
        schema = UserSchemas.get_single_user()
        
        # Act
        response = api_client.get(UserEndpoints.GET_SINGLE_USER.format(user_id=user_id))
        
        # Assert
        validate_schema(
            response=response,
            schema=schema,
            error_message="Single user response schema validation failed"
        )
        assert response['data']['id'] == user_id
        assert response['data']['email'] == 'janet.weaver@reqres.in'
        assert response['data']['first_name'] == 'Janet'

    def test_create_user(self, api_client: APIClient):
        """Test creating a new user"""
        # Arrange
        payload = TestData.get_user_payload()
        
        # Act
        response = api_client.post(UserEndpoints.CREATE_USER.value, json=payload)
        
        # Assert
        assert response['name'] == payload['name']
        assert response['job'] == payload['job']
        assert 'id' in response
        assert 'createdAt' in response

    def test_update_user(self, api_client: APIClient):
        """Test updating an existing user"""
        # Arrange
        user_id = 2
        payload = TestData.get_user_update_payload()
        
        # Act
        response = api_client.put(
            UserEndpoints.UPDATE_USER.format(user_id=user_id), 
            json=payload
        )
        
        # Assert
        assert response['name'] == payload['name']
        assert response['job'] == payload['job']
        assert 'updatedAt' in response

    def test_delete_user(self, api_client: APIClient):
        """Test deleting a user"""
        # Arrange
        user_id = 2
        
        # Act
        response = api_client.delete(UserEndpoints.DELETE_USER.format(user_id=user_id))
        
        # Assert
        assert response.get('status_code') == HTTPStatus.NO_CONTENT

    def test_register_user_successful(self, api_client: APIClient):
        """Test successful user registration"""
        # Arrange
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        
        # Act
        response = api_client.post(UserEndpoints.REGISTER.value, json=payload)
        
        # Assert
        assert 'id' in response
        assert 'token' in response

    def test_login_successful(self, api_client: APIClient):
        """Test successful login"""
        # Arrange
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        
        # Act
        response = api_client.post(UserEndpoints.LOGIN.value, json=payload)
        
        # Assert
        assert 'token' in response 