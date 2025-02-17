import requests
from typing import Dict, Any, Optional

class APIClient:
    """Base API client for handling HTTP requests"""
    
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
    
    def _build_url(self, endpoint: str) -> str:
        """Builds full URL by combining base URL and endpoint"""
        return f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
    
    def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
        """Handle API response and raise exceptions if needed"""
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return {"status_code": response.status_code, "text": response.text}
    
    def get(self, endpoint: str, params: Optional[Dict] = None, headers: Optional[Dict] = None) -> Dict[str, Any]:
        """Perform GET request"""
        url = self._build_url(endpoint)
        response = self.session.get(url, params=params, headers=headers)
        return self._handle_response(response)
    
    def post(self, endpoint: str, data: Optional[Dict] = None, json: Optional[Dict] = None, 
             headers: Optional[Dict] = None) -> Dict[str, Any]:
        """Perform POST request"""
        url = self._build_url(endpoint)
        response = self.session.post(url, data=data, json=json, headers=headers)
        return self._handle_response(response)
    
    def put(self, endpoint: str, data: Optional[Dict] = None, json: Optional[Dict] = None, 
            headers: Optional[Dict] = None) -> Dict[str, Any]:
        """Perform PUT request"""
        url = self._build_url(endpoint)
        response = self.session.put(url, data=data, json=json, headers=headers)
        return self._handle_response(response)
    
    def delete(self, endpoint: str, headers: Optional[Dict] = None) -> Dict[str, Any]:
        """Perform DELETE request"""
        url = self._build_url(endpoint)
        response = self.session.delete(url, headers=headers)
        return self._handle_response(response) 