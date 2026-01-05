#!/bin/bash

echo "============================================"
echo "AI E-commerce Platform - Setup Script"
echo "============================================"
echo ""

echo "Step 1: Creating virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to create virtual environment"
    echo "Make sure Python 3.8+ is installed"
    exit 1
fi
echo "Virtual environment created successfully!"
echo ""

echo "Step 2: Activating virtual environment..."
source venv/bin/activate
echo ""

echo "Step 3: Installing dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi
echo "Dependencies installed successfully!"
echo ""

echo "Step 4: Generating encryption key..."
python -c "from cryptography.fernet import Fernet; print('ENCRYPTION_KEY=' + Fernet.generate_key().decode())" > backend/.env.generated
echo ""
echo "Encryption key generated! Add it to backend/.env"
echo ""

echo "Step 5: Running migrations..."
cd backend
python manage.py makemigrations
python manage.py migrate
if [ $? -ne 0 ]; then
    echo "ERROR: Migration failed"
    exit 1
fi
echo ""

echo "Step 6: Creating superuser..."
echo ""
echo "Please create an admin account:"
python manage.py createsuperuser
echo ""

echo "Step 7: Loading API providers..."
python manage.py load_api_providers
echo ""

echo "============================================"
echo "Setup completed successfully!"
echo "============================================"
echo ""
echo "To run the backend server:"
echo "  cd backend"
echo "  python manage.py runserver"
echo ""
echo "To run the frontend (requires Node.js):"
echo "  cd frontend/admin"
echo "  npm install"
echo "  npm run dev"
echo ""
echo "Backend will be at: http://localhost:8000"
echo "Admin Dashboard at: http://localhost:5173"
echo "Django Admin at: http://localhost:8000/admin"
echo ""
