from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from .custom_storage import MediaFileStorage  

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', 
                             storage=MediaFileStorage(),
                             blank=True, 
                             null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.pk})
    
    @property
    def tag_list(self):
        return ", ".join([tag.name for tag in self.tags.all()])
        
    class Meta:
        ordering = ['-date_posted']