#!/bin/bash
set -e

python -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

# Create media directories if they don't exist
mkdir -p /opt/render/project/src/media/post_images
chmod -R 777 /opt/render/project/src/media  # More permissive for troubleshooting

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

# Install gunicorn
pip install gunicorn