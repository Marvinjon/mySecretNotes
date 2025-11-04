#!/usr/bin/python3
import sys
import os

# Add your project directory to the sys.path
project_home = '/home/student/MySecretNotes'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Change to the project directory
os.chdir(project_home)

# Import the Flask app
from app import app as application

# Initialize the database if it doesn't exist
if not os.path.exists(application.database):
    from app import init_db
    init_db()
