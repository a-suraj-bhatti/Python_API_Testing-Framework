from typing import Dict, Any

class TestData:
    """Class to manage test data and payloads"""
    
    @staticmethod
    def get_user_payload() -> Dict[str, Any]:
        """Returns test data for user creation"""
        return {
            "name": "morpheus",
            "job": "leader"
        }
    
    @staticmethod
    def get_user_update_payload() -> Dict[str, Any]:
        """Returns test data for user update"""
        return {
            "name": "morpheus",
            "job": "zion resident"
        } 