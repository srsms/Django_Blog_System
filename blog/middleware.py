from django.conf import settings
import os

class MediaUrlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        if os.environ.get('RENDER'):
            response['Content-Security-Policy'] = "img-src 'self' data:;"
            
        return response