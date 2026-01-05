# QUICK START GUIDE

## 🚀 Quick Setup (Windows)

1. **Run the setup script:**
   ```bash
   setup.bat
   ```

2. **Follow the prompts** to create an admin account

3. **Generate and add encryption key:**
   - The script will generate a key in `backend\.env.generated`
   - Create `backend\.env` file and add the encryption key
   - Copy other settings from `.env.example`

4. **Start the backend:**
   ```bash
   python start.py
   ```
   Or manually:
   ```bash
   cd backend
   python manage.py runserver
   ```

5. **Start the frontend** (in a new terminal):
   ```bash
   cd frontend\admin
   npm install
   npm run dev
   ```

6. **Access the platform:**
   - Admin Dashboard: http://localhost:5173
   - Django Admin: http://localhost:8000/admin
   - API: http://localhost:8000/api/

## 📋 Manual Setup

If the automatic setup doesn't work:

```bash
# 1. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Generate encryption key
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"

# 4. Create backend\.env file with the key
# Copy from .env.example and add ENCRYPTION_KEY

# 5. Run migrations
cd backend
python manage.py makemigrations
python manage.py migrate

# 6. Create superuser
python manage.py createsuperuser

# 7. Load API providers
python manage.py load_api_providers

# 8. Run server
python manage.py runserver
```

## 🎯 First Steps

1. **Login to Django Admin** (http://localhost:8000/admin)
   - Use the superuser credentials you created
   - View all your models and data

2. **Access Admin Dashboard** (http://localhost:5173)
   - Modern React interface
   - Configure APIs and AI chatbot

3. **Configure API Integrations:**
   - Go to "API Configuration"
   - Add your Stripe, SendGrid, or Twilio credentials
   - Test connections

4. **Setup AI Chatbot:**
   - Go to "AI Configuration"
   - Choose provider (OpenAI, Claude, or Gemini)
   - Add your API key
   - Configure settings
   - Preview the chatbot

## 🔑 Getting API Keys

- **Stripe:** https://dashboard.stripe.com/apikeys
- **SendGrid:** https://app.sendgrid.com/settings/api_keys
- **Twilio:** https://console.twilio.com/
- **OpenAI:** https://platform.openai.com/api-keys
- **Anthropic Claude:** https://console.anthropic.com/
- **Google Gemini:** https://makersuite.google.com/app/apikey

## 📚 Documentation

- [README.md](README.md) - Full documentation
- [walkthrough.md](.gemini/antigravity/brain/.../walkthrough.md) - Detailed walkthrough

## ❗ Troubleshooting

**Issue:** `npm` not found
- **Solution:** Install Node.js from https://nodejs.org/

**Issue:** Migration errors
- **Solution:** Delete `db.sqlite3` and run migrations again

**Issue:** Module not found
- **Solution:** Make sure virtual environment is activated
  - Windows: `venv\Scripts\activate`
  - Linux/Mac: `source venv/bin/activate`

**Issue:** Encryption key error
- **Solution:** Make sure `ENCRYPTION_KEY` is set in `backend\.env`

## 🎉 You're Ready!

The platform is now fully functional with:
- ✅ Django backend with all models
- ✅ Encrypted API key storage
- ✅ Multi-provider AI chatbot
- ✅ Premium admin dashboard
- ✅ WebSocket support
- ✅ Complete documentation
