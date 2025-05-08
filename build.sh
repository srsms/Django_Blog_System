#!/bin/bash
set -e

python -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

mkdir -p /opt/render/project/src/media/post_images
chmod -R 755 /opt/render/project/src/media

python manage.py collectstatic --no-input

python manage.py migrate

pip install gunicorn