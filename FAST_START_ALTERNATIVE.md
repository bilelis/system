# ⚡ FAST START ALTERNATIVE - Hotel Management System

## 🚨 إذا Docker بطيء - البديل السريع (If Docker is Slow - Fast Alternative)

### 🔥 **منهج الـ Manual Setup - أسرع طريقة (Manual Setup - Fastest Way)**

#### 1️⃣ **Database Setup** (5 minutes)
```bash
# Install PostgreSQL locally or use online service
# Alternative: Use SQLite for development (faster)

# Create .env in backend folder:
cd backend
echo "DATABASE_URL=sqlite:///./hotel.db" > .env
echo "JWT_SECRET_KEY=dev_secret_key_minimum_32_characters_required" >> .env
```

#### 2️⃣ **Backend Setup** (2 minutes)
```bash
cd backend

# Activate virtual environment
.venv\Scripts\activate

# Install ONLY essential packages (no PySpark!)
pip install fastapi uvicorn sqlalchemy pydantic python-jose passlib python-multipart bcrypt python-dotenv

# Start backend
python main.py
# ✅ Should run on http://localhost:8000
```

#### 3️⃣ **Frontend Setup** (2 minutes)
```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
# ✅ Should run on http://localhost:5173
```

#### 4️⃣ **Gateway Setup** (1 minute)
```bash
cd gateway

# Install dependencies
npm install

# Start gateway
node src/index.js
# ✅ Should run on http://localhost:3001
```

## 🎯 **للاختبار السريع (Quick Test)**

1. **Open**: http://localhost:5173
2. **Login**: admin / admin123
3. **تأكد من**: Dashboard يعمل بدون مشاكل

## 💡 **نصائح للسرعة (Speed Tips)**

### استخدم SQLite بدلاً من PostgreSQL للتطوير:
```python
# في backend/app/core/config.py
DATABASE_URL = "sqlite:///./hotel.db"
```

### أزل Dependencies الغير ضرورية:
```bash
# في requirements.txt احتفظ فقط بـ:
fastapi==0.104.1
uvicorn==0.24.0
sqlalchemy==2.0.23
pydantic==2.4.2
python-jose==3.3.0
passlib==1.7.4
bcrypt==4.0.1
python-dotenv==1.0.0
```

## 🚀 **نتيجة (Result)**

- ✅ **Backend API**: http://localhost:8000/docs
- ✅ **Frontend**: http://localhost:5173  
- ✅ **Gateway**: http://localhost:3001
- ✅ **قاعدة البيانات**: SQLite (ملف محلي)

**الوقت المتوقع: 10 دقائق بدلاً من ساعة! (Expected time: 10 minutes instead of 1 hour!)**