"""
Base API Manager for all integrations
"""
import requests
import time
from abc import ABC, abstractmethod
from .models import APILog


class BaseAPIManager(ABC):
    """Base class for all API integrations"""
    
    def __init__(self, configuration):
        self.configuration = configuration
        self.api_key = configuration.get_api_key()
        self.api_secret = configuration.get_api_secret()
        self.endpoint_url = configuration.endpoint_url
        self.is_test_mode = configuration.is_test_mode
        self.extra_config = configuration.configuration
    
    @abstractmethod
    def test_connection(self):
        """Test API connection - must be implemented by subclasses"""
        pass
    
    def _make_request(self, method, endpoint, data=None, headers=None, params=None):
        """Make HTTP request and log it"""
        start_time = time.time()
        
        # Prepare headers
        if headers is None:
            headers = {}
        
        # Add authentication
        headers.update(self._get_auth_headers())
        
        # Full URL
        url = f"{self.endpoint_url}/{endpoint}" if self.endpoint_url else endpoint
        
        try:
            # Make request
            response = requests.request(
                method=method,
                url=url,
                json=data,
                headers=headers,
                params=params,
                timeout=30
            )
            
            response_time = time.time() - start_time
            
            # Log the request
            self._log_request(
                endpoint=url,
                method=method,
                request_data=data or {},
                request_headers=headers,
                response_data=response.json() if response.headers.get('content-type', '').startswith('application/json') else {},
                response_headers=dict(response.headers),
                status_code=response.status_code,
                response_time=response_time,
                is_error=not response.ok
            )
            
            response.raise_for_status()
            return response
        
        except requests.exceptions.RequestException as e:
            response_time = time.time() - start_time
            
            # Log error
            self._log_request(
                endpoint=url,
                method=method,
                request_data=data or {},
                request_headers=headers,
                response_data={},
                response_headers={},
                status_code=getattr(e.response, 'status_code', None) if hasattr(e, 'response') else None,
                response_time=response_time,
                is_error=True,
                error_message=str(e),
                error_type=type(e).__name__
            )
            
            raise
    
    def _log_request(self, endpoint, method, request_data, request_headers,
                     response_data, response_headers, status_code, response_time,
                     is_error=False, error_message='', error_type=''):
        """Log API request to database"""
        # Remove sensitive data from headers
        safe_headers = {k: v for k, v in request_headers.items() 
                       if k.lower() not in ['authorization', 'api-key', 'api_key']}
        
        APILog.objects.create(
            configuration=self.configuration,
            endpoint=endpoint,
            method=method,
            request_data=request_data,
            request_headers=safe_headers,
            response_data=response_data,
            response_headers=dict(response_headers),
            status_code=status_code,
            response_time=response_time,
            is_error=is_error,
            error_message=error_message,
            error_type=error_type
        )
    
    @abstractmethod
    def _get_auth_headers(self):
        """Get authentication headers - must be implemented by subclasses"""
        return {}
