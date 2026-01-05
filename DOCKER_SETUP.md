# 🐳 Docker Installation & Setup Guide

## 📦 Step 1: Install Docker Desktop

### Windows:
1. **Download Docker Desktop:**
   - Visit: https://www.docker.com/products/docker-desktop/
   - Download for Windows

2. **Install Docker Desktop:**
   - Run the installer
   - Follow the installation wizard
   - **Restart your computer** when prompted

3. **Verify Installation:**
   Open PowerShell or CMD and run:
   ```bash
   docker --version
   docker-compose --version
   ```

### Alternative: Use Docker Directly (Advanced)
```bash
# Pull Node.js image
docker pull node:24-alpine

# Pull Python image
docker pull python:3.11-slim
```

---

## 🚀 Step 2: Run the Platform with Docker

### Option A: Using Docker Compose (EASIEST - RECOMMENDED)

**Single command to start everything:**

```bash
cd C:\Users\pc\OneDrive\Desktop\WEBSITE ECOMERCE
docker-compose up --build
```

**Ye command:**
- ✅ Backend (Django) container banayega
- ✅ Admin Dashboard (React) container banayega
- ✅ Customer Store (React) container banayega
- ✅ Sab kuch automatically start ho jayega!

**Access:**
- Backend API: http://localhost:8000
- Admin Dashboard: http://localhost:5173
- Customer Store: http://localhost:3000
- Django Admin: http://localhost:8000/admin

### Option B: Individual Containers (Manual Control)

**Backend only:**
```bash
docker build -f Dockerfile.backend -t ecommerce-backend .
docker run -p 8000:8000 ecommerce-backend
```

**Admin Dashboard only:**
```bash
docker build -f Dockerfile.admin -t ecommerce-admin .
docker run -p 5173:5173 ecommerce-admin
```

**Customer Store only:**
```bash
docker build -f Dockerfile.store -t ecommerce-store .
docker run -p 3000:3000 ecommerce-store
```

---

## 🎯 Step 3: First Time Setup

### Create Admin User (one-time):

```bash
# Access backend container
docker-compose exec backend python manage.py createsuperuser

# Enter username, email, password when prompted
```

### Load API Providers (one-time):

```bash
docker-compose exec backend python manage.py load_api_providers
```

---

## 🛠️ Useful Docker Commands

### Start all services:
```bash
docker-compose up
```

### Start in background (detached mode):
```bash
docker-compose up -d
```

### Stop all services:
```bash
docker-compose down
```

### View logs:
```bash
# All services
docker-compose logs

# Specific service
docker-compose logs backend
docker-compose logs admin
docker-compose logs store
```

### Rebuild containers (after code changes):
```bash
docker-compose up --build
```

### Access container shell:
```bash
# Backend
docker-compose exec backend sh

# Admin
docker-compose exec admin sh

# Store
docker-compose exec store sh
```

### Remove all containers and volumes:
```bash
docker-compose down -v
```

---

## 🔧 Troubleshooting

### Problem: Port already in use
**Solution:** Stop the service using that port
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID_NUMBER> /F

# Or change port in docker-compose.yml
ports:
  - "8001:8000"  # Use 8001 on host
```

### Problem: Container won't start
**Solution:** Check logs
```bash
docker-compose logs backend
```

### Problem: Permission denied
**Solution:** Run PowerShell/CMD as Administrator

### Problem: Docker Desktop not running
**Solution:** 
- Start Docker Desktop from Start Menu
- Wait for it to fully start (green icon in system tray)

### Problem: Out of disk space
**Solution:** Clean up Docker
```bash
docker system prune -a
```

---

## 📊 Docker Benefits

### ✅ No Installation Needed:
- ❌ Python install nahi karna
- ❌ Node.js install nahi karna
- ❌ Dependencies manually install nahi karne
- ✅ Sirf Docker install karo, baaki sab automatic!

### ✅ Consistent Environment:
- Same setup on any computer
- No "works on my machine" problems
- Easy to share with team

### ✅ Easy Deployment:
- Same containers production mein deploy ho jayenge
- No configuration changes needed

---

## 🎯 Production Deployment

### Deploy to Cloud (Future):

**Option 1: Docker Hub**
```bash
docker tag ecommerce-backend your-username/ecommerce-backend
docker push your-username/ecommerce-backend
```

**Option 2: Cloud Platforms**
- AWS ECS
- Google Cloud Run
- Azure Container Instances
- DigitalOcean App Platform

---

## 📝 Quick Reference

### Development Workflow:

1. **Start:** `docker-compose up`
2. **Make changes** in code
3. **Restart:** `docker-compose restart backend` (or admin/store)
4. **Rebuild (if needed):** `docker-compose up --build`
5. **Stop:** `docker-compose down`

### Environment Variables:

Edit `docker-compose.yml` to change:
- Database settings
- API URLs
- Debug mode
- Secret keys

---

## 🆚 Docker vs Manual Installation

| Feature | Docker | Manual |
|---------|--------|--------|
| **Setup Time** | 5 minutes | 30+ minutes |
| **Dependencies** | Automatic | Manual install |
| **Consistency** | Same everywhere | May vary |
| **Cleanup** | One command | Complex |
| **Updates** | Easy rebuild | Reinstall all |
| **Learning Curve** | Medium | Easy |

---

## ✅ Summary

**Kya karna hai:**

1. **Install Docker Desktop** from docker.com
2. **Restart computer**
3. **Run:** `docker-compose up --build`
4. **Wait** 2-3 minutes for containers to build
5. **Access** http://localhost:8000/admin
6. **Done!** 🎉

**Sabse easy hai Docker!** Python, Node.js kuch install nahi karna! 🚀

---

## 🎓 Learn More

- Docker Documentation: https://docs.docker.com/
- Docker Compose: https://docs.docker.com/compose/
- Our Project Structure: See PROJECT_STRUCTURE.md

---

**Questions? Check the logs:**
```bash
docker-compose logs -f
```

This shows real-time logs from all services! 📋
