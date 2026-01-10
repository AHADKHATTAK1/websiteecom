@echo off
TITLE Admin Dashboard - Starting...
COLOR 0B

echo ========================================================
echo       🚀 Starting Admin Dashboard
echo ========================================================
echo.
echo Location: frontend/admin
echo URL: http://localhost:5173
echo.
echo Starting Vite development server...
echo.

cd "frontend\admin"
npm run dev

pause
