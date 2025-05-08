from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

class MediaFileStorage(FileSystemStorage):
    def __init__(self):
        super().__init__(location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL)
        
    def url(self, name):
        """
        Override the URL method to ensure proper URL generation for media files
        """
        url = super().url(name)
        if settings.DEBUG or not os.environ.get('RENDER'):
            return url
            
        return f"{settings.MEDIA_URL}{name}"