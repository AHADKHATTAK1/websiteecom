# AL DAR - UAE E-commerce Platform

Advanced e-commerce platform for United Arab Emirates market, featuring Django backend, React admin dashboard, and AI-powered customer tools.


## 🚀 Features

### Backend (Django)
- ✅ Custom user authentication with JWT
- ✅ Product & order management
- ✅ **API Integration System** - Configure payment, shipping, email, SMS APIs from admin
- ✅ **AI Chatbot** - Multi-provider support (OpenAI, Claude, Gemini)
- ✅ Encrypted API key storage
- ✅ Comprehensive logging and monitoring
- ✅ WebSocket support for real-time chat
- ✅ Celery for background tasks

### Frontend (React Admin Dashboard)
- ✅ Modern, premium dark theme UI
- ✅ Responsive design with glassmorphism effects
- ✅ **API Configuration Interface** - Manage all third-party APIs
- ✅ **AI Chatbot Configuration** - Configure AI providers and chatbot settings
- ✅ Real-time chat preview
- ✅ Dashboard with analytics
- ✅ Product & order management pages

## 📋 Prerequisites

- Python 3.8+
- Node.js 16+ (for frontend)
- pip and npm/yarn

## 🔧 Installation

### Backend Setup

1. **Create virtual environment:**
```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

2. **Install dependencies:**
```bash
pip install -r ../requirements.txt
```

3. **Setup environment variables:**
```bash
# Copy .env.example to .env
copy ..\.env.example .env

# Generate encryption key
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"

# Add the key to .env as ENCRYPTION_KEY
```

4. **Run migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create superuser:**
```bash
python manage.py createsuperuser
```

6. **Load initial API providers (optional):**
```bash
python manage.py shell
```
```python
from apps.api_integrations.models import APIProvider

# Add Payment providers
APIProvider.objects.create(
    name="Stripe",
    slug="stripe",
    category="payment",
    description="Accept payments online",
    required_fields=["api_key"],
    is_active=True
)

APIProvider.objects.create(
    name="SendGrid",
    slug="sendgrid",
    category="email",
    description="Email delivery service",
    required_fields=["api_key", "from_email"],
    is_active=True
)

APIProvider.objects.create(
    name="Twilio",
    slug="twilio",
    category="sms",
    description="SMS notifications",
    required_fields=["api_key", "api_secret", "from_number"],
    is_active=True
)
```

7. **Run development server:**
```bash
python manage.py runserver
```

### Frontend Setup

1. **Install dependencies:**
```bash
cd frontend/admin
npm install
```

2. **Run development server:**
```bash
npm run dev
```

The admin dashboard will be available at: http://localhost:5173

## 🎯 Usage

### Setting up API Integrations

1. Navigate to **API Configuration** in the admin dashboard
2. Click "Add New API"
3. Select your provider (Stripe, SendGrid, Twilio, etc.)
4. Enter your API credentials
5. Click "Test Connection" to verify
6. Save configuration

### Configuring AI Chatbot

1. Navigate to **AI Chatbot Configuration**
2. Select your AI provider (OpenAI, Claude, or Gemini)
3. Choose the model
4. Enter your API key
5. Customize system prompt and parameters
6. Enable features (Knowledge Base, Product Recommendations, Order Tracking)
7. Preview the chatbot
8. Save configuration

### Using the Chatbot API

```javascript
// Send a message to the chatbot
fetch('/api/chatbot/chat/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    message: 'Hello!',
    session_id: 'unique-session-id',
    context: {
      product_query: 'headphones'
    }
  })
})
```

### WebSocket Chat (Real-time)

```javascript
const ws = new WebSocket('ws://localhost:8000/ws/chat/session-id/');

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Bot response:', data.message);
};

ws.send(JSON.stringify({
  message: 'Hello!',
  user_id: 1
}));
```

## 🛠️ Database Models

### API Integration Models
- **APIProvider** - Catalog of available APIs
- **APIConfiguration** - User's configured APIs (encrypted keys)
- **APILog** - All API call history with response times

### AI Chatbot Models
- **ChatbotConfiguration** - Chatbot settings per user
- **ChatbotKnowledgeBase** - Custom training data
- **ChatConversation** - Chat history
- **ChatbotIntent** - Custom intents and responses

## 🔐 Security

- API keys are encrypted using Fernet symmetric encryption
- JWT authentication for API endpoints
- CORS configured for frontend
- Environment variables for sensitive data
- Secure password hashing

## 📦 Key Technologies

**Backend:**
- Django 4.2
- Django REST Framework
- Celery for background tasks
- Channels for WebSockets
- OpenAI, Anthropic, Google AI SDKs
- Stripe, SendGrid, Twilio SDKs

**Frontend:**
- React 18
- Vite
- React Router
- Lucide React icons
- Modern CSS with CSS Variables

## 🚀 Deployment

### Backend (Django)
1. Set DEBUG=False in production
2. Configure PostgreSQL database
3. Set up Redis for Celery and Channels
4. Collect static files: `python manage.py collectstatic`
5. Use gunicorn/uvicorn for WSGI/ASGI
6. Set up Celery workers

### Frontend
1. Build: `npm run build`
2. Serve the `dist` folder
3. Configure API endpoint in production

## 📝 API Endpoints

### Authentication
- POST `/api/auth/register/` - Register new user
- POST `/api/auth/login/` - Login
- GET `/api/auth/profile/` - Get user profile

### API Integrations
- GET `/api/integrations/providers/` - List available providers
- POST `/api/integrations/configurations/` - Create API config
- POST `/api/integrations/configurations/{id}/test_connection/` - Test API
- GET `/api/integrations/configurations/{id}/logs/` - Get API logs

### AI Chatbot
- GET `/api/chatbot/config/` - Get chatbot configuration
- POST `/api/chatbot/config/` - Create/update chatbot config
- POST `/api/chatbot/config/{id}/test_connection/` - Test AI connection
- POST `/api/chatbot/chat/` - Send chat message
- WS `/ws/chat/{session_id}/` - WebSocket chat

## 🎨 Customization

### Changing Theme Colors
Edit `frontend/admin/src/index.css` and modify CSS variables:
```css
:root {
  --primary-500: #6366f1;  /* Your brand color */
  --accent-500: #ec4899;   /* Accent color */
  /* ... */
}
```

### Adding New AI Providers
1. Create provider handler in `apps/ai_chatbot/integrations/`
2. Update `ChatbotService` in `chatbot_service.py`
3. Add to AI_PROVIDER_CHOICES in models

### Adding New API Providers
1. Create integration in `apps/api_integrations/providers/`
2. Extend `BaseAPIManager`
3. Add to database via admin or shell
4. Update frontend provider list

## 📧 Support

For issues or questions, please check the documentation or create an issue.

## 📄 License

MIT License

---

**Happy Coding! 🎉**
