#!/bin/bash
# Hotel Management System - Complete Setup Script (Linux/Mac)

echo "🏨 Hotel Management System - Complete Setup"
echo "========================================="

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📋 Creating .env file from template..."
    cp .env.template .env
    echo "✅ .env file created. You may want to update API keys later."
fi

# Stop any existing containers
echo "🛑 Stopping existing containers..."
docker-compose -f devops/docker-compose.yml down

# Build and start all services
echo "🔨 Building and starting all services..."
docker-compose -f devops/docker-compose.yml up --build -d

# Wait for services to start
echo "⏳ Waiting for services to start..."
sleep 30

# Check service health
echo "🔍 Checking service health..."

echo "Database:"
docker-compose -f devops/docker-compose.yml exec postgres pg_isready -U postgres

echo "Backend:"
if curl -f http://localhost:8000/health > /dev/null 2>&1; then
    echo "✅ Backend is healthy"
else
    echo "❌ Backend not ready"
fi

echo "Gateway:"
if curl -f http://localhost:3001/health > /dev/null 2>&1; then
    echo "✅ Gateway is healthy"
else
    echo "❌ Gateway not ready"
fi

echo "Frontend:"
if curl -f http://localhost:5173 > /dev/null 2>&1; then
    echo "✅ Frontend is healthy"
else
    echo "❌ Frontend not ready"
fi

echo ""
echo "🎉 Hotel Management System is starting up!"
echo "🌐 Access points:"
echo "   Frontend: http://localhost:5173"
echo "   API Docs: http://localhost:8000/docs"
echo "   Gateway:  http://localhost:3001"
echo ""
echo "🔐 Default login: admin / admin123"
echo "📝 View logs: docker-compose -f devops/docker-compose.yml logs -f"
echo "🛑 Stop system: docker-compose -f devops/docker-compose.yml down"
echo ""
echo "✨ Happy hotel managing!"