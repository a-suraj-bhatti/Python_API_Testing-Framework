import json
import os
from typing import Dict, Any

class SchemaLoader:
    """Utility class for loading JSON schemas"""
    
    @staticmethod
    def load_schema(schema_path: str) -> Dict[str, Any]:
        """
        Load a JSON schema file
        
        Args:
            schema_path: Path to the schema file relative to the schemas directory
            
        Returns:
            Dict containing the loaded schema
            
        Raises:
            FileNotFoundError: If schema file doesn't exist
            json.JSONDecodeError: If schema file is invalid JSON
        """
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        full_path = os.path.join(base_path, 'schemas', schema_path)
        
        with open(full_path, 'r') as schema_file:
            return json.load(schema_file)

class UserSchemas:
    """Class containing methods to load user-related schemas"""
    
    @staticmethod
    def get_users_list() -> Dict[str, Any]:
        """Load schema for users list endpoint"""
        return SchemaLoader.load_schema('users/get_users_list.json')
    
    @staticmethod
    def get_single_user() -> Dict[str, Any]:
        """Load schema for single user endpoint"""
        return SchemaLoader.load_schema('users/get_single_user.json') 