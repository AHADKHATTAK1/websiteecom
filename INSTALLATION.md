# 🎯 INSTALLATION GUIDE - Complete Step by Step

## ⚠️ Prerequisites Install Karein

### 1. Python Installation (Zaruri!)

**Windows:**
1. Visit: https://www.python.org/downloads/
2. Download latest Python (3.11 or higher)
3. **Important:** Install karte waqt:
   - ✅ Check "Add Python to PATH" 
   - ✅ Check "Install pip"
4. Install karein
5. Verify:
   ```bash
   python --version
   pip --version
   ```

### 2. Node.js Installation (Optional - Only for React frontend)

**Windows:**
1. Visit: https://nodejs.org/
2. Download LTS version
3. Install karein (default settings)
4. Verify:
   ```bash
   node --version
   npm --version
   ```

---

## 🚀 Quick Start (Python-Only Version)

Agar Node.js nahi hai, toh Django admin panel use karein:

### Step 1: Setup Backend

```bash
# Go to project directory
cd C:\Users\pc\OneDrive\Desktop\WEBSITE ECOMERCE\backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r ..\requirements.txt

# Setup database
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser
# Enter username, email, password when prompted

# Load API providers
python manage.py load_api_providers

# Start server
python manage.py runserver
```

### Step 2: Access Django Admin

Open browser:
```
http://localhost:8000/admin
```

Login with credentials you created in createsuperuser.

### ✅ What You Can Do in Django Admin:

- ✅ Manage Users
- ✅ Configure APIs (Stripe, SendGrid, etc.)
- ✅ Setup AI Chatbot
- ✅ Add Products
- ✅ Manage Orders
- ✅ View API Logs
- ✅ Manage Chat Conversations

---

## 🎨 For React Frontend (Optional)

**Only if Node.js is installed:**

### Terminal 1: Backend (already running)

### Terminal 2: Admin Dashboard
```bash
cd C:\Users\pc\OneDrive\Desktop\WEBSITE ECOMERCE\frontend\admin
npm install
npm run dev
```
Access: http://localhost:5173

### Terminal 3: Customer Store
```bash
cd C:\Users\pc\OneDrive\Desktop\WEBSITE ECOMERCE\frontend\store
npm install
npm run dev
```
Access: http://localhost:3000

---

## 🔧 Troubleshooting

### Problem: "python is not recognized"
**Solution:** Python PATH mein nahi hai
- Python reinstall karein with "Add to PATH" checked
- Ya manually PATH add karein

### Problem: "pip install" fails
**Solution:** 
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Problem: "npm is not recognized"
**Solution:** Node.js install nahi hai
- Node.js install karein from nodejs.org
- Computer restart karein

### Problem: Port already in use
**Solution:**
```bash
# Kill process on port 8000
netstat -ano | findstr :8000
taskkill /PID <PID_NUMBER> /F

# Or use different port
python manage.py runserver 8001
```

### Problem: Migration errors
**Solution:**
```bash
# Delete database
del db.sqlite3

# Delete migration files (except __init__.py)
# Then run:
python manage.py makemigrations
python manage.py migrate
```

---

## 📱 Minimal Setup (Just Python)

Agar sirf backend chahiye:

1. Install Python ✅
2. Run these commands:
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install django djangorestframework django-cors-headers
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

3. Access: http://localhost:8000/admin

---

## 🎯 Next Steps After Installation

1. **Login to Django Admin:** http://localhost:8000/admin
2. **Add API Configuration:** Click "API configurations" → Add your Stripe/SendGrid keys
3. **Setup AI Chatbot:** Click "Chatbot configurations" → Add OpenAI/Claude key
4. **Add Products:** Click "Products" → Add new products
5. **Test Everything:** Use the API endpoints

---

## 📞 Still Having Issues?

Share the exact error message and I'll help you fix it!

Common commands to check installation:
```bash
python --version
pip --version
node --version
npm --version
```

All should show version numbers if installed correctly.
