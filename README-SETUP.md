# Hotel Management System v2 Enhanced

## 🚀 Quick Start Guide

### Prerequisites
- Node.js (v14+)
- Python 3.11+
- PostgreSQL
- Git

### 🎯 One-Click Setup
Simply run the startup script:
```bash
# Windows
start-system.bat

# Manual setup alternative below
```

### 🏨 System Access Points

#### For Bilel Ayari (Owner)
- **Bilel Control Panel**: http://localhost:5173/bilel-control
- **Access Code**: `1234`
- **Features**: Full system control, AI assistant, developer mode, analytics

#### For Staff
- **Reception**: http://localhost:5173/reception
- **POS System**: http://localhost:5173/pos
- **Dashboard**: http://localhost:5173/dashboard

### 🔧 Manual Setup (Alternative)

#### Backend Setup
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
python main.py
```

#### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

#### Gateway Setup
```bash
cd gateway
npm install
npm start
```

### 🗄️ Database Setup
1. Create PostgreSQL database named `hotel_management`
2. Update `.env` file with your database credentials
3. Run migrations:
```sql
-- Execute files in order:
-- database/migrations/001_initial_schema.sql
-- database/migrations/002_pos_schema.sql
-- database/seeds/001_sample_data.sql
```

### 🤖 AI Integration
1. Get OpenAI API key
2. Update `.env` file:
```
OPENAI_API_KEY=your-openai-api-key-here
```

### 📊 System Features

#### ✅ Completed Features
- **Bilel Control Panel** with 4-digit authentication
- **Full POS System** with menu items and payment processing
- **AI Chatbot** integration (placeholder working, needs API key)
- **Real-time Dashboard** with KPIs
- **Multi-language Support** (English/Arabic)
- **Room Management System**
- **Guest Management**
- **Order Processing**
- **Analytics Dashboard**
- **Developer Mode** for code editing
- **Security Logging**

#### 🔮 System Architecture
```
Frontend (React + TypeScript + Material-UI)
    ↓
Gateway (Node.js + JWT)
    ↓
Backend (FastAPI + Python)
    ↓
Database (PostgreSQL)
```

### 🎨 Technology Stack
- **Frontend**: React 19, TypeScript, Material-UI, Redux Toolkit
- **Backend**: FastAPI, SQLAlchemy, Pydantic
- **Database**: PostgreSQL
- **Gateway**: Node.js, Express, JWT
- **AI**: OpenAI Integration
- **DevOps**: Docker Compose ready

### 🛡️ Security Features
- JWT-based authentication
- Role-based access control
- Special 4-digit access for Bilel Control Panel
- Protected routes
- Action logging

### 📱 Responsive Design
- Mobile-friendly interface
- Tablet optimization
- Desktop full features

### 🔧 Development Commands

#### Frontend
```bash
npm run dev        # Start development server
npm run build      # Build for production
npm run preview    # Preview production build
npm run lint       # Run linting
```

#### Backend
```bash
python main.py     # Start development server
# Backend runs on http://localhost:8000
# API docs: http://localhost:8000/docs
```

### 🐛 Troubleshooting

#### Common Issues
1. **Port conflicts**: Change ports in configuration files
2. **Database connection**: Verify PostgreSQL is running and credentials are correct
3. **Dependencies**: Run `npm install` or `pip install -r requirements.txt`

#### Default Credentials
- **Database**: postgres/password@localhost:5432/hotel_management
- **Bilel Control Panel**: Access code `1234`

### 📈 Performance
- Fast React development with Vite
- Optimized database queries
- Lazy loading components
- Material-UI theme optimization

### 🔄 API Endpoints
- `GET /api/v1/health` - System health check
- `POST /api/v1/auth/login` - User authentication
- `GET /api/v1/analytics/*` - Analytics endpoints
- `GET /api/v1/rooms/*` - Room management
- `GET /api/v1/guests/*` - Guest management
- `GET /api/v1/orders/*` - Order processing
- `GET /api/v1/pos/*` - POS system endpoints

### 💡 Tips for Bilel
1. Use the **Developer Mode** in your control panel for live code editing
2. The **AI Assistant** can help with system modifications
3. **Analytics Dashboard** provides real-time insights
4. All staff actions are logged in the **Security** tab
5. You can remotely control all system modules

### 🚀 Next Steps
1. Configure your OpenAI API key for full AI functionality
2. Set up your actual database credentials
3. Customize the system colors and branding
4. Add your specific menu items and room configurations

---

**Created for Bilel Ayari** - Hotel Management System v2 Enhanced
*Your complete hotel management solution with AI integration*