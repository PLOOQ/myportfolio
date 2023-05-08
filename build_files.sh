#!/bin/bash

# Install dependencies
python3.9 -m pip install -r requirements.txt

# Collect static files
python3.9 manage.py collectstatic --noinput --clear

# Run database migrations (if applicable)
# python manage.py migrate

# Run additional build commands as needed

# Set execute permissions for manage.py
# chmod +x manage.py
