# Django Blog Management System

A complete blog system with admin panel and public-facing interface, built with Django and PostgreSQL.

## Features

### Admin Panel
✅ Secure session-based authentication  
✅ Blog post management (CRUD operations)  
⚠️ Image uploads (currently not functioning properly)  
✅ Tag management (comma-separated input)  
✅ Paginated post listing  

### Public Frontend
✅ View all blog posts with pagination  
✅ Search posts by title/content/tags  
✅ View individual post details  
✅ Responsive Bootstrap design  
✅ Tag filtering and display

## Tech Stack
- **Backend**: Django 5.0
- **Database**: PostgreSQL (with SQLite fallback for development)
- **Frontend**: Bootstrap 5, Crispy Forms
- **Media Storage**: Custom storage solution for Render deployment
- **Hosting**: Render (Free Tier)

## Setup Instructions

### 1. Local Development
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
```

### 2. Deployment on Render
- Create PostgreSQL database on Render
- Connect your GitHub repository
- Configure environment variables:
  - `DATABASE_URL` (auto-set from PostgreSQL)
  - `SECRET_KEY` (generate new)
  - `DEBUG=False`
  - `RENDER=true`
- Manual deploy after first setup

## Project Structure
```
django-blog-system/
├── blog/                  # Main app
│   ├── templates/         # HTML templates
│   ├── static/            # CSS/JS files
│   ├── migrations/        # Database migrations
│   ├── admin.py           # Admin panel configuration
│   ├── forms.py           # Form classes for posts and auth
│   ├── models.py          # Post, Tag models
│   ├── urls.py            # App URL routing
│   └── views.py           # View logic
├── blog_project/          # Project config
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL routing
│   └── wsgi.py            # WSGI interface
├── media/                 # Uploaded files (dev)
├── staticfiles/           # Collected static files
├── .env.example           # Environment template
├── build.sh               # Render build script
├── render.yaml            # Render config
└── requirements.txt       # Dependencies
```

## Key Features Implementation

### Custom Storage for Media Files
The project includes a custom storage solution (`MediaFileStorage`) for image uploads, but this feature currently has implementation issues. The intended design aims to handle file uploads differently between development and production environments, especially for Render hosting.

### Tag Management
Tags can be added to posts using a comma-separated input field. The system automatically creates new tags or uses existing ones.

### Search Functionality
Posts can be searched by title, content, or tags using a unified search field.

### User Authentication
Complete user authentication system with registration, login, and logout functionality. Post editing is restricted to the author.

## Known Issues and Troubleshooting

### ⚠️ File Upload Not Working
The image upload functionality is currently not working properly. This is a known issue that needs to be fixed.

#### Possible Solutions:
- Check the `MediaFileStorage` implementation in `custom_storage.py`
- Verify media URL configuration in `settings.py` for both development and production
- Ensure proper file permissions in both environments: `chmod -R 755 media/`
- Check for issues with the Render disk mount configuration in `render.yaml`

### Database Issues?
```bash
# Reset database (dev only)
python manage.py flush
python manage.py migrate
```

### Deployment Issues on Render?
- Check the build logs for errors
- Ensure all environment variables are set correctly
- Verify the disk is mounted correctly for media storage

## License
MIT License - Free for personal and commercial use

## Live Demo
https://django-blog-6lnv.onrender.com
