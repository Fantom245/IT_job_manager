#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
DJANGO_SETTINGS_MODULE=it_job_manager.settings.prod python manage.py collectstatic --no-input

# Apply any outstanding database migrations
DJANGO_SETTINGS_MODULE=it_job_manager.settings.prod python manage.py migrate