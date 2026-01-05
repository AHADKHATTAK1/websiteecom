# 🚀 Quick Start Script - One Command Setup
# Run this to start everything automatically

Write-Host "🎉 AI E-commerce Platform - Quick Start" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Navigate to backend
Set-Location -Path "C:\Users\pc\OneDrive\Desktop\WEBSITE ECOMERCE\backend"

Write-Host "📦 Step 1: Setting up database..." -ForegroundColor Yellow
# Delete old database if exists
if (Test-Path "db.sqlite3") {
    Remove-Item "db.sqlite3" -Force -ErrorAction SilentlyContinue
}

Write-Host "🗄️ Step 2: Running migrations..." -ForegroundColor Yellow
python manage.py makemigrations
python manage.py migrate

Write-Host "👤 Step 3: Creating admin user..." -ForegroundColor Yellow
Write-Host "Enter admin username (default: admin):" -ForegroundColor Green
$username = Read-Host
if ([string]::IsNullOrWhiteSpace($username)) { $username = "admin" }

Write-Host "Enter admin email (default: admin@example.com):" -ForegroundColor Green
$email = Read-Host
if ([string]::IsNullOrWhiteSpace($email)) { $email = "admin@example.com" }

python manage.py createsuperuser --username $username --email $email

Write-Host "📚 Step 4: Loading API providers..." -ForegroundColor Yellow
python manage.py load_api_providers

Write-Host ""
Write-Host "✅ Setup Complete!" -ForegroundColor Green
Write-Host ""
Write-Host "🌐 Access Points:" -ForegroundColor Cyan
Write-Host "   Django Admin: http://localhost:8000/admin" -ForegroundColor White
Write-Host "   API: http://localhost:8000/api/" -ForegroundColor White
Write-Host ""
Write-Host "🚀 Starting server..." -ForegroundColor Yellow
Write-Host ""

# Start server
python manage.py runserver
