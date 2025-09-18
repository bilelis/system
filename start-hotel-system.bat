@echo off
REM Hotel Management System - One-Click Startup Script (Windows)
echo 🏨 Starting Hotel Management System...
echo =====================================

REM Check if Docker is running
docker info >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker is not running. Please start Docker first.
    pause
    exit /b 1
)

REM Create .env file if it doesn't exist
if not exist .env (
    echo 📋 Creating .env file from template...
    copy .env.template .env
    echo ✅ .env file created. You may want to update API keys later.
)

REM Stop any existing containers
echo 🛑 Stopping existing containers...
docker-compose -f devops/docker-compose.yml down

REM Build and start all services
echo 🔨 Building and starting all services...
docker-compose -f devops/docker-compose.yml up --build -d

REM Wait for services to start
echo ⏳ Waiting for services to start...
timeout /t 30 /nobreak >nul

REM Check service health
echo 🔍 Checking service health...

echo Database:
docker-compose -f devops/docker-compose.yml exec postgres pg_isready -U postgres

echo Backend:
curl -f http://localhost:8000/health >nul 2>&1 && echo ✅ Backend is healthy || echo ❌ Backend not ready

echo Gateway:
curl -f http://localhost:3001/health >nul 2>&1 && echo ✅ Gateway is healthy || echo ❌ Gateway not ready

echo Frontend:
curl -f http://localhost:5173 >nul 2>&1 && echo ✅ Frontend is healthy || echo ❌ Frontend not ready

echo.
echo 🎉 Hotel Management System is starting up!
echo 🌐 Access points:
echo    Frontend: http://localhost:5173
echo    API Docs: http://localhost:8000/docs
echo    Gateway:  http://localhost:3001
echo.
echo 🔐 Default login: admin / admin123
echo 📝 View logs: docker-compose -f devops/docker-compose.yml logs -f
echo 🛑 Stop system: docker-compose -f devops/docker-compose.yml down
echo.
echo ✨ Happy hotel managing!
echo.
echo Opening frontend in your browser...
start http://localhost:5173

pause