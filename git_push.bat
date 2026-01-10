@echo off
REM Quick Git Push Script
REM Run this to commit and push all changes

TITLE Git Push - E-commerce Project
COLOR 0A

echo ========================================
echo    Git Push - E-commerce Platform
echo ========================================
echo.

echo [Step 1/4] Checking git status...
git status
echo.

echo [Step 2/4] Adding all changes...
git add .
echo.

echo [Step 3/4] Creating commit...
set /p commit_msg="Enter commit message (or press Enter for default): "
if "%commit_msg%"=="" set commit_msg=feat: Add promotional banner and setup scripts

git commit -m "%commit_msg%"
echo.

echo [Step 4/4] Pushing to repository...
echo Repository: https://github.com/AHADKHATTAK1/websiteecom.git
echo.

REM Check if remote exists
git remote -v | findstr "origin" >nul
if %errorlevel% NEQ 0 (
    echo Setting up remote...
    git remote add origin https://github.com/AHADKHATTAK1/websiteecom.git
)

git push origin main
echo.

if %errorlevel% EQU 0 (
    echo ========================================
    echo    ✅ Push Successful!
    echo ========================================
) else (
    echo ========================================
    echo    ❌ Push Failed
    echo    Check error messages above
    echo ========================================
)
echo.

pause
