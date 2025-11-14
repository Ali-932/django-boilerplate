#!/bin/bash
# Setup script for new project

echo "Enter your new project name (lowercase, hyphens allowed):"
read PROJECT_NAME

# Update pyproject.toml
sed -i "s/name = \"django-boilerplate\"/name = \"$PROJECT_NAME\"/" pyproject.toml

# Setup environment
cp example.env .env
echo "Created .env file - please update with your values"

# Install dependencies
uv sync

# Setup database
cd backend
uv run python manage.py migrate
echo "Database migrations complete"

echo "Setup complete! Update .env and run: uv run python manage.py runserver"