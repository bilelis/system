# Clean Hotel Management System

This is a clean, minimal implementation of a hotel management system with only the essential components needed for the system to function properly.

## Project Structure

```
clean/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── endpoints/
│   │   │       │   ├── auth.py
│   │   │       │   ├── users.py
│   │   │       │   ├── rooms.py
│   │   │       │   ├── guests.py
│   │   │       │   └── orders.py
│   │   │       └── api.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   ├── db/
│   │   │   └── session.py
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── room.py
│   │   │   ├── guest.py
│   │   │   └── order.py
│   │   └── schemas/
│   │       ├── auth.py
│   │       ├── user.py
│   │       ├── room.py
│   │       ├── guest.py
│   │       └── order.py
│   ├── main.py
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── app.js
├── ACCESS_GUIDE.md
└── README.md
```

## Backend

The backend is built with:
- FastAPI for the API framework
- SQLAlchemy for ORM
- SQLite for the database
- Pydantic for data validation
- JWT for authentication

### API Endpoints

- **Auth**: `/api/v1/auth/` - Login and user management
- **Rooms**: `/api/v1/rooms/` - Room management
- **Guests**: `/api/v1/guests/` - Guest management
- **Orders**: `/api/v1/orders/` - Order management

## Frontend

The frontend is a simple HTML/CSS/JavaScript implementation that interacts with the backend API.

## Access Guide

For detailed instructions on how to access all system components, please refer to [ACCESS_GUIDE.md](file:///c%3A/Users/LOQ/Desktop/v2%20enahnce/clean/ACCESS_GUIDE.md).

## Setup

1. Install backend dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```

2. Start the backend server:
   ```bash
   cd backend
   python main.py
   ```

3. Open `frontend/index.html` in a web browser to access the frontend.

## Key Features

- User authentication with JWT tokens
- Room management (CRUD operations)
- Guest management (CRUD operations)
- Order management (CRUD operations)
- Simple dashboard with statistics
- Clean, minimal codebase with no unnecessary dependencies

## Removed Components

This clean version removes:
- Supabase/PostgreSQL dependencies (replaced with SQLite)
- OpenAI integration
- PySpark dependencies
- Redundant files and code
- Unused libraries and packages
- Complex frontend frameworks (replaced with simple HTML/CSS/JS)

The system maintains all core functionality while being significantly simpler and easier to set up.