# 🏨 Hotel Management System - Quick Start Guide

## 🚀 One-Command Setup

This guide will get you running the complete Hotel Management System in less than 5 minutes.

## 📋 Prerequisites

- **Docker** (v20.0+) and **Docker Compose** (v1.29+)
- **Git** (for cloning)
- **4GB+ RAM** available for containers

## ⚡ Quick Start (1 Command)

```bash
# Clone and start everything at once
git clone <repository-url>
cd "v2 enahnce"
docker-compose -f devops/docker-compose.yml up --build
```

## 🌐 Access Points

After startup (2-3 minutes), access:

- 🖥️ **Frontend**: http://localhost:5173
- 🔧 **API Gateway**: http://localhost:3001
- 📊 **Backend API**: http://localhost:8000
- 🗄️ **PostgreSQL**: localhost:5432

## 🔐 Default Login Credentials

| Role | Username | Password | Access |
|------|----------|----------|---------|
| Admin | `admin` | `admin123` | Full system access |
| Receptionist | `reception1` | `reception123` | Guest & Room management |
| Cashier | `cashier1` | `cashier123` | POS & Billing only |

## 🧪 Test the System

1. **Login**: Navigate to http://localhost:5173/login
2. **Dashboard**: View analytics and KPIs
3. **POS System**: Access via http://localhost:5173/pos
4. **Guest Management**: Add/view guests
5. **Room Booking**: Manage room reservations

## 🛠️ Individual Component Setup

### Option 1: Docker Compose (Recommended)
```bash
# Start all services
docker-compose -f devops/docker-compose.yml up --build

# Start in background
docker-compose -f devops/docker-compose.yml up -d --build

# Stop all services
docker-compose -f devops/docker-compose.yml down

# Reset database
docker-compose -f devops/docker-compose.yml down -v
docker-compose -f devops/docker-compose.yml up --build
```

### Option 2: Manual Setup

#### 🗄️ 1. Database Setup
```bash
# Start PostgreSQL container
docker run --name hotel-postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=hotel_management \
  -p 5432:5432 \
  -d postgres:14-alpine

# Run migrations
cd database
psql -h localhost -U postgres -d hotel_management -f migrations/001_initial_schema.sql
psql -h localhost -U postgres -d hotel_management -f migrations/002_pos_schema.sql
psql -h localhost -U postgres -d hotel_management -f seeds/001_sample_data.sql
```

#### 🔧 2. Backend (FastAPI)
```bash
cd backend

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp ../.env.template .env

# Start backend server
python main.py
# Backend will be available at: http://localhost:8000
```

#### 🌐 3. API Gateway (Node.js)
```bash
cd gateway

# Install dependencies
npm install

# Start gateway
npm start
# Gateway will be available at: http://localhost:3001
```

#### 💻 4. Frontend (React + Vite)
```bash
cd frontend

# Install dependencies
npm install

# Copy environment file
cp ../.env.template .env

# Start development server
npm run dev
# Frontend will be available at: http://localhost:5173
```

## 📁 Environment Configuration

Create `.env` files in each directory with these settings:

### Root `.env`
```env
# Database Configuration
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=hotel_management
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

# Authentication
JWT_SECRET_KEY=your_super_secure_secret_key_here
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# API Configuration
BACKEND_URL=http://localhost:8000
GATEWAY_URL=http://localhost:3001
FRONTEND_URL=http://localhost:5173

# External APIs
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
TESTSPRITE_API_KEY=your_testsprite_api_key_here
```

### Frontend `.env`
```env
VITE_API_URL=http://localhost:3001/api
VITE_GEMINI_API_KEY=your_gemini_api_key_here
VITE_TESTSPRITE_API_KEY=your_testsprite_api_key_here
```

### Backend `.env`
```env
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=hotel_management
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

JWT_SECRET_KEY=your_super_secure_secret_key_here
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
TESTSPRITE_API_KEY=your_testsprite_api_key_here

DEBUG=True
ALLOW_ORIGINS=["http://localhost:5173", "http://localhost:3001"]
```

## 🧩 System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Gateway       │    │   Backend       │    │   Database      │
│   (React)       │────│   (Node.js)     │────│   (FastAPI)     │────│   (PostgreSQL)  │
│   Port: 5173    │    │   Port: 3001    │    │   Port: 8000    │    │   Port: 5432    │
└─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🔍 Troubleshooting

### Common Issues

**🐳 Docker Issues**
```bash
# Check running containers
docker ps

# View container logs
docker-compose logs frontend
docker-compose logs backend
docker-compose logs postgres

# Restart a specific service
docker-compose restart backend
```

**📡 Port Conflicts**
```bash
# Check what's using ports
netstat -an | grep :5173
netstat -an | grep :3001
netstat -an | grep :8000
netstat -an | grep :5432

# Kill processes using ports (if needed)
kill -9 $(lsof -ti:5173)
```

**🗄️ Database Connection Issues**
```bash
# Test database connection
docker exec -it hotel-postgres psql -U postgres -d hotel_management -c "SELECT 1;"

# Reset database
docker-compose down -v
docker-compose up --build
```

**🔐 Authentication Issues**
- Verify JWT_SECRET_KEY is the same in backend and gateway
- Check if user exists in database
- Clear browser localStorage and try again

## ✅ Verification Checklist

- [ ] All containers are running (`docker ps`)
- [ ] Frontend loads at http://localhost:5173
- [ ] Can login with admin/admin123
- [ ] Dashboard displays data
- [ ] POS system is accessible
- [ ] API documentation at http://localhost:8000/docs

## 🎯 Next Steps

1. **Customize Configuration**: Update environment variables
2. **Add Sample Data**: Use the seeded data or add your own
3. **Test Features**: Try guest management, room booking, POS
4. **Run Tests**: Execute the automated test suite
5. **Deploy**: Use the Docker setup for production deployment

## 📞 Support

- 📖 **API Documentation**: http://localhost:8000/docs
- 🐛 **Issues**: Check logs with `docker-compose logs`
- 💡 **Features**: Review the main documentation

---

**🚀 Ready to build the future of hotel management!** 

*This system is built with React, FastAPI, PostgreSQL, and Docker for maximum scalability and ease of deployment.*