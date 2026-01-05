@echo off
TITLE AI E-commerce Platform - Client Demo Launcher
COLOR 0A

echo ========================================================
echo       🚀 Starting AI E-commerce Platform Demo
echo ========================================================
echo.
echo [1/3] Starting Backend Server (api.mystore.local:8000)...
start "Backend API" cmd /k "cd backend && python manage.py runserver 0.0.0.0:8000"

echo [2/3] Starting Admin Dashboard (admin.mystore.local:5173)...
start "Admin Dashboard" cmd /k "cd frontend/admin && npm run dev"

echo [3/3] Starting Customer Store (mystore.local:3000)...
start "Customer Store" cmd /k "cd frontend/store && npm run dev"

echo.
echo ========================================================
echo       ✅ All Systems Launching!
echo ========================================================
echo.
echo Please access the platforms here:
echo.
echo 🛍️  Customer Store:  http://mystore.local:3000
echo 🔧  Admin Panel:     http://admin.mystore.local:5173
echo ⚙️  Backend API:     http://api.mystore.local:8000
echo.
echo NOTE: Ensure you have updated your hosts file!
echo.
pause
