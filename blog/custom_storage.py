from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

class MediaFileStorage(FileSystemStorage):
    def __init__(self):
        super().__init__(location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL)
        
    def url(self, name):
        """
        Override the URL method to ensure proper URL generation for media files
        in both development and production environments.
        """
        url = super().url(name)
        
        if os.environ.get('RENDER'):
            if not url.startswith('/media/'):
                return f"{settings.MEDIA_URL}{name}"
        
        return url