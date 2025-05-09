from django.conf import settings
import os

class MediaUrlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # For Render deployment, set necessary headers
        if os.environ.get('RENDER'):
            # Allow images from our domain
            csp = "default-src 'self'; img-src 'self' data:; style-src 'self' 'unsafe-inline' cdn.jsdelivr.net; script-src 'self' cdn.jsdelivr.net;"
            response['Content-Security-Policy'] = csp
            
        return response