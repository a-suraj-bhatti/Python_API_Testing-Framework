from typing import Dict, Any
from jsonschema import validate as json_validate
from jsonschema.exceptions import ValidationError

def validate_schema(response: Dict[str, Any], schema: Dict[str, Any], error_message: str = "Schema validation failed") -> None:
    """
    Validate response against JSON schema
    
    Args:
        response: API response to validate
        schema: JSON schema to validate against
        error_message: Custom error message to show if validation fails
    
    Raises:
        AssertionError: If schema validation fails
    """
    try:
        json_validate(instance=response, schema=schema)
    except ValidationError as e:
        raise AssertionError(f"{error_message}: {str(e)}") 