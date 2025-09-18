# Hotel Management System - Supabase Integration Guide

## 🚀 Complete Setup & Deployment Instructions

### Overview
This guide will help you integrate your existing Hotel Management System with Supabase, providing:
- 🔐 Secure authentication with Supabase Auth
- 📊 PostgreSQL database hosted on Supabase
- 🚀 Free deployment options (Vercel + Railway)
- 🔄 Dual authentication modes (traditional + Supabase)
- ⚡ Production-ready configuration

---

## 📋 Prerequisites

### Required Software:
- Node.js v18+
- Python 3.11+
- Git
- Code Editor (VS Code recommended)

### Required Accounts:
- Supabase account (free)
- GitHub account (for deployment)
- Vercel account (free - for frontend)
- Railway account (free - for backend)

---

## 🗄️ Database Setup in Supabase

### Step 1: Create New Project
1. Go to [supabase.com](https://supabase.com)
2. Click "Start your project"
3. Sign in with GitHub
4. Click "New Project"
5. Fill project details:
   - **Name**: `hotel-management-system`
   - **Database Password**: Strong password (save it!)
   - **Region**: Choose closest to your users
6. Click "Create new project"

### Step 2: Setup Database Schema
1. In your project dashboard, go to **SQL Editor**
2. Copy content from `database/supabase_schema.sql`
3. Paste in SQL Editor and click **Run**
4. Wait for completion (2-3 minutes)
5. Copy content from `database/supabase_sample_data.sql`
6. Paste and **Run** to add sample data

### Step 3: Configure Authentication
1. Go to **Authentication** > **Settings**
2. Under **Site URL**, set:
   - Development: `http://localhost:5173`
   - Production: `https://your-domain.com`
3. Under **Redirect URLs**, add:
   ```
   http://localhost:5173/**
   https://your-domain.com/**
   ```
4. Click **Save**

### Step 4: Get API Keys
1. Go to **Settings** > **API**
2. Save these values:
   - **Project URL**: `https://your-project-ref.supabase.co`
   - **anon public**: For frontend
   - **service_role**: For backend (keep secret!)

---

## 🔧 Backend Setup (Python FastAPI)

### Step 1: Install Dependencies
```bash
cd backend
# Activate virtual environment
source .venv/bin/activate  # Mac/Linux
# OR
.venv\Scripts\activate     # Windows

# Install packages
pip install -r requirements.txt
```

### Step 2: Environment Configuration
```bash
# Copy template
cp .env.template .env
```

Edit `.env` with your Supabase credentials:
```env
# Supabase Database
DATABASE_URL=postgresql://postgres:YOUR_DB_PASSWORD@db.YOUR_PROJECT_REF.supabase.co:5432/postgres
SUPABASE_URL=https://YOUR_PROJECT_REF.supabase.co
SUPABASE_ANON_KEY=your_anon_key_here
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key_here

# JWT Configuration
JWT_SECRET_KEY=your-super-secret-key-minimum-32-characters
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# API Keys (optional)
OPENAI_API_KEY=your-openai-key
GEMINI_API_KEY=your-gemini-key

# App Settings
DEBUG=True
ALLOW_ORIGINS=["http://localhost:5173", "http://localhost:3001"]
BILEL_ACCESS_CODE=1234
```

### Step 3: Start Backend Server
```bash
python main.py
```

You should see:
```
INFO: Uvicorn running on http://0.0.0.0:8000
```

### Step 4: Test API
Open browser: `http://localhost:8000/docs`

---

## ⚛️ Frontend Setup (React + Vite)

### Step 1: Install Dependencies
```bash
cd frontend
npm install
```

### Step 2: Environment Configuration
```bash
# Copy template
cp .env.template .env
```

Edit `.env`:
```env
# Backend API
VITE_API_URL=http://localhost:8000/api/v1

# Supabase Configuration
VITE_SUPABASE_URL=https://YOUR_PROJECT_REF.supabase.co
VITE_SUPABASE_ANON_KEY=your_anon_key_here

# Optional AI Integration
VITE_GEMINI_API_KEY=your-gemini-key

# App Configuration
VITE_APP_NAME=Hotel Management System
VITE_ENVIRONMENT=development
```

### Step 3: Start Development Server
```bash
npm run dev
```

You should see:
```
➜  Local:   http://localhost:5173/
```

---

## 🧪 Testing the System

### Authentication Test:
1. Open `http://localhost:5173`
2. Try registering a new account
3. Test login functionality
4. Verify JWT tokens in browser DevTools

### Database Test:
1. In Supabase dashboard, go to **Table Editor**
2. Verify data exists in tables:
   - `users`
   - `rooms` 
   - `guests`
   - `bookings`
   - `orders`

### API Test:
1. Open `http://localhost:8000/docs`
2. Test various endpoints
3. Verify authentication works
4. Test CRUD operations

---

## 🚀 Production Deployment

### Deploy Backend to Railway:

1. Go to [railway.app](https://railway.app)
2. Sign in with GitHub
3. Click "New Project" > "Deploy from GitHub repo"
4. Select your repository
5. Choose `backend` folder
6. Add environment variables:
   ```
   DATABASE_URL=your_supabase_database_url
   SUPABASE_URL=your_supabase_url
   SUPABASE_SERVICE_ROLE_KEY=your_service_role_key
   JWT_SECRET_KEY=your_production_secret_key
   ALLOW_ORIGINS=["https://your-frontend-domain.vercel.app"]
   OPENAI_API_KEY=your_openai_key
   GEMINI_API_KEY=your_gemini_key
   ```
7. Click **Deploy**
8. Get your Railway URL (e.g., `https://backend-production-xxxx.up.railway.app`)

### Deploy Frontend to Vercel:

1. Go to [vercel.com](https://vercel.com)
2. Sign in with GitHub
3. Click "New Project"
4. Select your repository
5. Set **Root Directory**: `frontend`
6. Add environment variables:
   ```
   VITE_API_URL=https://your-backend-url.railway.app/api/v1
   VITE_SUPABASE_URL=your_supabase_url
   VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
   VITE_GEMINI_API_KEY=your_gemini_key
   ```
7. Click **Deploy**
8. Get your Vercel URL (e.g., `https://hotel-management-xxxx.vercel.app`)

### Alternative: Deploy Frontend to Netlify:

1. Go to [netlify.com](https://netlify.com)
2. Build your project: `npm run build`
3. Drag and drop `frontend/dist` folder
4. Or connect GitHub repository
5. Set:
   - **Build command**: `npm run build`
   - **Publish directory**: `dist`
6. Add same environment variables as Vercel

---

## 🔒 Security Configuration

### Row Level Security (RLS)
In Supabase SQL Editor, run:
```sql
-- Enable RLS on all tables
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
ALTER TABLE rooms ENABLE ROW LEVEL SECURITY;
ALTER TABLE guests ENABLE ROW LEVEL SECURITY;
ALTER TABLE bookings ENABLE ROW LEVEL SECURITY;
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;

-- Example policy for users table
CREATE POLICY "Users can read own data" ON users
    FOR SELECT USING (auth.uid() = id::text);

CREATE POLICY "Users can update own data" ON users
    FOR UPDATE USING (auth.uid() = id::text);
```

### Production Security Checklist:
- [ ] Change all default passwords
- [ ] Use environment variables for secrets
- [ ] Enable HTTPS in production
- [ ] Configure CORS properly
- [ ] Set up rate limiting
- [ ] Enable Supabase RLS policies
- [ ] Use strong JWT secret keys
- [ ] Regularly rotate API keys

---

## 🔄 Authentication Modes

Your system now supports dual authentication:

### Mode 1: Traditional JWT (existing)
- Uses your FastAPI backend
- Custom user management
- JWT tokens stored in localStorage

### Mode 2: Supabase Auth (new)
- Uses Supabase authentication
- Built-in user management
- Automatic token refresh
- Email verification
- Password reset

### API Endpoints Available:

**Traditional Auth:**
- `POST /auth/login` - Username/password login
- `POST /auth/register` - Create new user
- `GET /auth/me` - Get current user

**Supabase Auth:**
- `POST /auth/supabase/signup` - Register with email
- `POST /auth/supabase/signin` - Sign in with email
- `POST /auth/supabase/refresh` - Refresh tokens
- `POST /auth/supabase/signout` - Sign out

---

## 🛠️ Development Workflow

### Local Development:
```bash
# Terminal 1: Backend
cd backend
source .venv/bin/activate
python main.py

# Terminal 2: Frontend
cd frontend
npm run dev
```

### Building for Production:
```bash
# Backend: Already production-ready
# Frontend: Build optimized version
cd frontend
npm run build
```

### Database Migrations:
1. Create new SQL files in `database/migrations/`
2. Run in Supabase SQL Editor
3. Update your local schema accordingly

---

## 🐛 Troubleshooting

### Common Issues:

**Database Connection Error:**
```
psycopg2.OperationalError: could not connect to server
```
**Solution:** Check DATABASE_URL in `.env`

**Supabase Auth Error:**
```
SupabaseAuthError: Invalid JWT
```
**Solution:** Verify SUPABASE_ANON_KEY is correct

**CORS Error:**
```
Access to fetch blocked by CORS policy
```
**Solution:** Add frontend URL to ALLOW_ORIGINS

**Import Error:**
```
ModuleNotFoundError: No module named 'supabase'
```
**Solution:** Install requirements: `pip install -r requirements.txt`

**Build Error on Vercel:**
```
Error: Environment variable not found
```
**Solution:** Double-check all environment variables are set

### Debug Tips:
1. Check browser Network tab for API calls
2. Verify environment variables are loaded
3. Check Supabase logs in dashboard
4. Use `console.log()` for frontend debugging
5. Check Railway/Vercel deployment logs

---

## 📊 Monitoring & Analytics

### Supabase Analytics:
- Go to **Analytics** in Supabase dashboard
- Monitor database performance
- Track authentication events
- View API usage

### Application Monitoring:
- Set up error tracking (Sentry)
- Monitor API response times
- Track user engagement
- Set up alerts for failures

---

## 🔄 Backup & Recovery

### Database Backup:
1. In Supabase, go to **Settings** > **Database**
2. Download backups regularly
3. Store in secure location

### Code Backup:
- Use Git for version control
- Push to GitHub regularly
- Tag production releases

---

## 🎯 Next Steps

After successful deployment:

1. **Configure Custom Domain:**
   - Set up DNS
   - Configure SSL certificates
   - Update Supabase redirect URLs

2. **Optimize Performance:**
   - Enable caching
   - Optimize database queries
   - Set up CDN for static assets

3. **Enhanced Security:**
   - Implement rate limiting
   - Add API key management
   - Set up monitoring alerts

4. **User Experience:**
   - Add email templates
   - Implement push notifications
   - Add analytics tracking

5. **Business Features:**
   - Payment integration
   - Reporting dashboard
   - Multi-language support
   - Mobile app

---

## 📞 Support Resources

- **Supabase Documentation:** [docs.supabase.com](https://docs.supabase.com)
- **FastAPI Documentation:** [fastapi.tiangolo.com](https://fastapi.tiangolo.com)
- **React Documentation:** [react.dev](https://react.dev)
- **Vercel Documentation:** [vercel.com/docs](https://vercel.com/docs)
- **Railway Documentation:** [docs.railway.app](https://docs.railway.app)

---

## 🎉 Congratulations!

Your Hotel Management System is now fully integrated with Supabase and ready for production use! You have:

✅ Secure authentication with Supabase Auth  
✅ Scalable PostgreSQL database  
✅ Production-ready deployment  
✅ Free hosting for both frontend and backend  
✅ Comprehensive monitoring and analytics  
✅ Professional documentation  

**Happy hotel managing! 🏨**