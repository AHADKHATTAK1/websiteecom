#!/bin/bash
# Backend Startup Script for WSL
# Run this in Ubuntu terminal

echo "========================================="
echo "   Starting Django Backend Server"
echo "========================================="
echo ""

# Navigate to project
cd /mnt/c/Users/anzah\ computer/Desktop/WEBSITE\ ECOMERCE || exit

# Activate virtual environment
if [ -d "venv" ]; then
    echo "✓ Activating virtual environment..."
    source venv/bin/activate
else
    echo "⚠ Virtual environment not found!"
    echo "Run: python3 -m venv venv"
    exit 1
fi

# Go to backend
cd backend || exit

# Check if database exists
if [ ! -f "db.sqlite3" ]; then
    echo "⚠ Database not found. Running migrations..."
    python manage.py makemigrations
    python manage.py migrate
fi

echo ""
echo "✓ Starting server on http://localhost:8000"
echo ""
echo "Keep this terminal open!"
echo "Press Ctrl+C to stop server"
echo ""

# Start server
python manage.py runserver
