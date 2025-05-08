# Django Blog Management System

A complete blog system with admin panel and public-facing interface, built with Django and PostgreSQL.

## Features

### Admin Panel
✅ Secure session-based authentication  
✅ Blog post management (CRUD operations)  
✅ Image uploads with preview  
✅ Tag management (comma-separated input)  
✅ Paginated post listing  

### Public Frontend
✅ View all blog posts with pagination  
✅ Search posts by title/content  
✅ View individual post details  
✅ Responsive Bootstrap design  

## Tech Stack
- **Backend**: Django 5.0
- **Database**: PostgreSQL
- **Frontend**: Bootstrap 5
- **Hosting**: Render (Free Tier)

## Setup Instructions

1. Local Development
```bash
# Clone repository
git clone https://github.com/srsms/django-blog-system.git
cd django-blog-system

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your settings

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver

2. Deployment on Render
Create PostgreSQL database on Render

Connect your GitHub repository

Configure environment variables:

DATABASE_URL (auto-set from PostgreSQL)

SECRET_KEY (generate new)

DEBUG=False

Manual deploy after first setup

Project Structure
django-blog-system/
├── blog/                  # Main app
│   ├── templates/         # HTML templates
│   ├── models.py          # Post, Tag models
│   └── views.py           # View logic
├── blog_project/          # Project config
├── media/                 # Uploaded files (dev)
├── static/                # CSS/JS assets
├── .env.example           # Environment template
├── render.yaml            # Render config
└── requirements.txt       # Dependencies
```

Troubleshooting
Images Not Displaying?

Check MEDIA_URL and MEDIA_ROOT in settings.py

Verify file permissions: chmod -R 755 media/

For production, use AWS S3 or Cloudinary

```bash
Database Issues?
# Reset database (dev only)
python manage.py flush
python manage.py migrate
License
MIT License - Free for personal and commercial use
```

Live Demo: https://django-blog-6lnv.onrender.com
