@echo off
echo ========================================
echo   E-COMMERCE PLATFORM - AUTO START
echo ========================================
echo.
echo Starting all services...
echo.

REM Start Store (Port 3000)
echo [1/2] Starting Customer Store...
start "Store Frontend" cmd /k "cd frontend\store && npm run dev"
timeout /t 3 /nobreak >nul

REM Start Admin (Port 5173)
echo [2/2] Starting Admin Dashboard...
start "Admin Dashboard" cmd /k "cd frontend\admin && npm run dev"
timeout /t 3 /nobreak >nul

echo.
echo ========================================
echo   ALL SERVICES STARTED!
echo ========================================
echo.
echo Store:  http://localhost:3000/
echo Admin:  http://localhost:5173/
echo Backend: https://web-production-615d5.up.railway.app
echo.
echo Press any key to open in browser...
pause >nul

REM Open in default browser
start http://localhost:3000/
start http://localhost:5173/

echo.
echo Services running in separate windows.
echo Close those windows to stop services.
echo.
pause
