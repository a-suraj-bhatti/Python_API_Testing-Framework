from enum import Enum
from typing import Dict

class BaseEndpoint(Enum):
    """Base class for endpoint enums"""
    
    def format(self, **kwargs) -> str:
        """Format the endpoint with provided parameters"""
        return self.value.format(**kwargs)

class UserEndpoints(BaseEndpoint):
    """User-related endpoint paths"""
    GET_USERS_LIST = "/users"
    GET_SINGLE_USER = "/users/{user_id}"
    CREATE_USER = "/users"
    UPDATE_USER = "/users/{user_id}"
    DELETE_USER = "/users/{user_id}"
    REGISTER = "/register"
    LOGIN = "/login"

class ProductEndpoints(BaseEndpoint):
    """Product-related endpoint paths"""
    GET_PRODUCTS = "/products"
    GET_SINGLE_PRODUCT = "/products/{product_id}"
    # ... more endpoints ... 