@echo off
echo.
echo ========================================
echo   AI E-commerce Platform with Ngrok
echo ========================================
echo.

REM Check if backend server is running
echo Step 1: Starting Django Backend...
start "Django Backend" cmd /k "cd backend && python manage.py runserver 0.0.0.0:8000"

REM Wait for server to start
timeout /t 5 /nobreak > nul

echo Step 2: Starting Ngrok Tunnel...
echo.
echo Your public URL will appear below:
echo.

REM Start ngrok
ngrok http 8000 --log=stdout

pause
