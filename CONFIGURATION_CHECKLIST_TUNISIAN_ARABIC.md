# 🔧 Configuration Checklist - نظام إدارة الفندق

## 🚨 **خطوات ضرورية للمطور (Developer Critical Actions)**

### 1️⃣ **إعداد قاعدة البيانات (Database Setup)**
```bash
# بدء PostgreSQL Database
docker run --name hotel-postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=hotel_management -p 5432:5432 -d postgres:14-alpine

# تشغيل الـ Migrations
cd database
psql -h localhost -U postgres -d hotel_management -f migrations/001_initial_schema.sql
psql -h localhost -U postgres -d hotel_management -f migrations/002_pos_schema.sql
psql -h localhost -U postgres -d hotel_management -f seeds/001_sample_data.sql
```

### 2️⃣ **إعداد المتغيرات البيئية (Environment Variables)**
```bash
# إنشاء ملف .env في Backend
cd backend
cp ../.env.template .env

# إنشاء ملف .env في Frontend  
cd ../frontend
cp ../.env.template .env

# تحديث المفاتيح في .env:
POSTGRES_PASSWORD=your_secure_password
JWT_SECRET_KEY=your_super_secure_jwt_secret_minimum_32_characters
GEMINI_API_KEY=your_gemini_api_key_from_google_ai_studio
```

### 3️⃣ **تشغيل الـ Backend (FastAPI Server)**
```bash
cd backend

# تفعيل البيئة الافتراضية
.venv\Scripts\activate

# تثبيت Dependencies
pip install -r requirements.txt

# بدء الـ Server
python main.py
# يجب أن يعمل على: http://localhost:8000
```

### 4️⃣ **تشغيل الـ Frontend (React App)**
```bash
cd frontend

# تثبيت Dependencies
npm install

# بدء الـ Development Server
npm run dev
# يجب أن يعمل على: http://localhost:5173
```

### 5️⃣ **تشغيل الـ Gateway (Node.js)**
```bash
cd gateway

# تثبيت Dependencies
npm install

# بدء الـ Gateway
node src/index.js
# يجب أن يعمل على: http://localhost:3001
```

## ✅ **اختبار النظام (System Verification)**

### تحقق من الخدمات:
- **Frontend**: http://localhost:5173 ← يجب أن تظهر صفحة تسجيل الدخول
- **Backend API Docs**: http://localhost:8000/docs ← يجب أن تظهر Swagger UI
- **Gateway**: http://localhost:3001 ← يجب أن يرد بـ JSON response

### تجريب تسجيل الدخول:
- **Username**: `admin`
- **Password**: `admin123`
- **يجب أن يدخل للـ Dashboard بنجاح**

## 🚨 **مشاكل شائعة وحلولها (Common Issues)**

### مشكلة: Database Connection Failed
```bash
# تأكد من تشغيل PostgreSQL
docker ps | grep postgres

# إذا لم يعمل، شغل Database مرة أخرى
docker run --name hotel-postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=hotel_management -p 5432:5432 -d postgres:14-alpine
```

### مشكلة: Port Already in Use
```bash
# تحقق من العمليات التي تستخدم البورت
netstat -ano | findstr :5173
netstat -ano | findstr :8000
netstat -ano | findstr :3001

# إيقاف العملية
taskkill /PID [رقم_العملية] /F
```

### مشكلة: JWT Authentication Failed
```bash
# تأكد من أن JWT_SECRET_KEY نفس الرقم في Backend و Gateway
# يجب أن يكون على الأقل 32 حرف
```

## 🎯 **الخطوات النهائية (Final Steps)**

1. **تأكد من تشغيل جميع الخدمات الأربع:**
   - ✅ PostgreSQL Database (Port 5432)
   - ✅ Backend API (Port 8000) 
   - ✅ API Gateway (Port 3001)
   - ✅ Frontend React (Port 5173)

2. **اختبر تسجيل الدخول والتنقل في النظام**

3. **تحقق من أن جميع صفحات النظام تعمل:**
   - Dashboard
   - Room Management
   - Guest Management  
   - POS System
   - Billing

## 🏆 **النظام جاهز للعرض! (System Ready for Demo!)**

عند اكتمال جميع الخطوات أعلاه، النظام سيكون جاهز 100% للعرض والاستخدام.