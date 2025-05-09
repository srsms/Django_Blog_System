from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Post, Tag
from django.utils import timezone
import os

class Command(BaseCommand):
    help = 'Seeds the database with initial data after resets'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')
        
        # Create a superuser if none exists
        if not User.objects.filter(username='admin').exists():
            admin_user = User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='AdminPassword123'  # should be changed after first login
            )
            self.stdout.write(self.style.SUCCESS('Created superuser: admin'))
        else:
            admin_user = User.objects.get(username='admin')
            self.stdout.write('Superuser already exists')
        
        # Create sample tags
        tags = []
        for tag_name in ['Django', 'Python', 'Web Development', 'Tutorial', 'Deployment']:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            tags.append(tag)
            if created:
                self.stdout.write(f'Created tag: {tag_name}')
            else:
                self.stdout.write(f'Tag already exists: {tag_name}')
        
        # Create sample posts
        sample_posts = [
            {
                'title': 'Welcome to My Django Blog',
                'content': """
This is the first post on my Django blog platform. I'm excited to share my journey in web development and Django!

## Features of this Blog

- User authentication
- Post creation and management
- Tag filtering and search
- Responsive design with Bootstrap
- Deployed on Render

I'll be sharing more tutorials and tips about Django development soon.
                """,
                'tags': [tags[0], tags[1], tags[2]]
            },
            {
                'title': 'How to Deploy Django Apps on Render',
                'content': """
Deploying Django applications on Render is a straightforward process, but there are some specific configurations to be aware of.

## Steps for Deployment

1. Prepare your Django project with proper settings
2. Configure your render.yaml file
3. Set up the PostgreSQL database
4. Configure static and media files

### Working with Free Tier Limitations

One important note about Render's free tier: your database will reset after periods of inactivity. To handle this, you can implement a data seeding strategy like the one used in this blog.

Stay tuned for more deployment tips!
                """,
                'tags': [tags[0], tags[3], tags[4]]
            }
        ]
        
        # Create posts if they don't exist
        for post_data in sample_posts:
            # Check if a post with this title exists
            if not Post.objects.filter(title=post_data['title']).exists():
                post = Post.objects.create(
                    title=post_data['title'],
                    content=post_data['content'],
                    author=admin_user,
                    date_posted=timezone.now()
                )
                post.tags.set(post_data['tags'])
                self.stdout.write(f'Created post: {post_data["title"]}')
            else:
                self.stdout.write(f'Post already exists: {post_data["title"]}')
        
        self.stdout.write(self.style.SUCCESS('Data seeding completed successfully!'))