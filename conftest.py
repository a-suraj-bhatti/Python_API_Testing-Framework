import json
import os
import pytest
from typing import Dict, Any
from utils.api_client import APIClient

def load_config(env: str = None) -> Dict[str, Any]:
    """
    Load configuration from config file based on environment
    
    Args:
        env: Environment to load config for (dev/staging/prod)
             If None, reads from ENV environment variable or defaults to 'dev'
             
    Returns:
        Dict containing the configuration for specified environment
    """
    # Get environment from ENV var if not provided, default to 'dev'
    env = env or os.getenv('ENV', 'dev')
    
    # Load base config
    with open('config/config.json') as f:
        config = json.load(f)
    
    # Override base_url with environment specific value
    if env in config['environments']:
        config.update(config['environments'][env])
    
    return config

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", 
                    help="Environment to run tests against (dev/staging/prod)")

@pytest.fixture(scope="session")
def config(request) -> Dict[str, Any]:
    """Fixture to provide configuration based on environment"""
    env = request.config.getoption("--env")
    return load_config(env)

@pytest.fixture(scope="session")
def api_client(config: Dict[str, Any]) -> APIClient:
    """Fixture to provide API client instance"""
    return APIClient(config['base_url'])

@pytest.fixture(scope="function")
def cleanup_test_data() -> None:
    """Fixture for cleaning up test data after tests"""
    yield
    # Add cleanup logic here if needed 