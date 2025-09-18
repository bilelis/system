# Clean Hotel Management System Project Structure

## Essential Components Only

### Backend (Python FastAPI)
```
backend/
├── main.py                 # Application entry point
├── requirements.txt        # Minimal dependencies
├── .env                    # Environment variables
├── app/
│   ├── core/
│   │   ├── config.py       # Configuration settings
│   │   └── security.py     # Security utilities (JWT, password hashing)
│   ├── db/
│   │   └── session.py      # Database session management
│   ├── models/
│   │   ├── user.py         # User model
│   │   ├── room.py         # Room model
│   │   ├── guest.py        # Guest model
│   │   └── order.py        # Order model
│   ├── schemas/
│   │   ├── auth.py         # Authentication schemas
│   │   ├── user.py         # User schemas
│   │   ├── room.py         # Room schemas
│   │   ├── guest.py        # Guest schemas
│   │   └── order.py        # Order schemas
│   ├── api/
│   │   ├── deps.py         # Dependencies
│   │   └── v1/
│   │       ├── api.py      # API router
│   │       └── endpoints/
│   │           ├── auth.py # Authentication endpoints
│   │           ├── rooms.py # Room management endpoints
│   │           ├── guests.py # Guest management endpoints
│   │           ├── orders.py # Order management endpoints
│   │           └── simple_auth.py # Simplified authentication endpoints
│   └── services/
│       └── analytics.py    # Analytics service
└── init_db.py              # Database initialization script
```

### Frontend (React + TypeScript)
```
frontend/
├── index.html              # Main HTML file
├── package.json            # Dependencies and scripts
├── tsconfig.json           # TypeScript configuration
├── vite.config.ts          # Vite configuration
├── public/
│   └── favicon.ico         # Favicon
└── src/
    ├── main.tsx            # Application entry point
    ├── App.tsx             # Main application component
    ├── index.css           # Global styles
    ├── services/
    │   ├── api.ts          # API service
    │   └── simpleAuthService.ts # Simplified authentication service
    ├── store/
    │   ├── index.ts        # Store configuration
    │   └── slices/
    │       └── authSlice.ts # Authentication state management
    ├── pages/
    │   ├── Login.tsx       # Login page
    │   └── Dashboard.tsx   # Dashboard page
    ├── components/
    │   └── ProtectedRoute.tsx # Protected route component
    └── hooks/
        └── useAuth.ts      # Authentication hook
```

### Database
```
database/
├── init.sql                # Database initialization script
└── sample_data.sql         # Sample data
```

### Documentation
```
docs/
├── README.md               # Project overview
├── SETUP.md                # Setup instructions
└── API_DOCS.md             # API documentation
```

### Scripts
```
scripts/
├── start-backend.sh        # Start backend server
├── start-frontend.sh       # Start frontend development server
└── init-database.sh        # Initialize database
```

## Removed Components

### Unnecessary Files and Directories
- All test files and testing directories
- All documentation files except essential ones
- All configuration files for unused services
- All sample data files not needed for basic operation
- All cache and temporary files
- All duplicate files
- All unused components and libraries

### Unnecessary Dependencies
- Removed PySpark and other heavy libraries
- Removed unused frontend libraries
- Removed development dependencies not needed for production
- Removed Supabase dependencies (using local SQLite instead)
- Removed OpenAI dependencies (not essential for core functionality)

### Simplified Architecture
- Single backend API instead of microservices
- Single frontend application instead of multiple
- SQLite database instead of PostgreSQL for simplicity
- Removed gateway service (handled by backend CORS)
- Removed complex authentication (using simplified JWT)