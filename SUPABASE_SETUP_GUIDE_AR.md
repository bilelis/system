# دليل إعداد نظام إدارة الفنادق مع Supabase
# Hotel Management System Supabase Integration Guide

## 🚀 المتطلبات الأساسية

### برامج ضرورية:
- Node.js (v18 أو أحدث)
- Python (v3.11 أو أحدث) 
- Git
- Code Editor (VS Code مُفضل)

### حسابات ضرورية:
- حساب Supabase (مجاني)
- حساب GitHub (للنشر)

---

## 📊 إعداد قاعدة البيانات في Supabase

### خطوة 1: إنشاء مشروع جديد
1. اذهب إلى [supabase.com](https://supabase.com)
2. اضغط "Start your project"
3. سجل دخول بحساب GitHub
4. اضغط "New Project"
5. اختر Organization أو انشئ واحد جديد
6. املأ البيانات:
   - **Project Name**: `hotel-management-system`
   - **Database Password**: اختر كلمة مرور قوية واحفظها
   - **Region**: اختر الأقرب لك (Europe West للمغرب العربي)
7. اضغط "Create new project"

### خطوة 2: إعداد قاعدة البيانات
1. في لوحة التحكم، اذهب إلى **SQL Editor**
2. انسخ محتوى ملف `database/supabase_schema.sql`
3. الصقه في محرر SQL واضغط **Run**
4. انتظر حتى تكتمل العملية (قد تأخذ دقيقتين)
5. انسخ محتوى ملف `database/supabase_sample_data.sql`
6. الصقه في محرر SQL واضغط **Run**

### خطوة 3: ضبط إعدادات المصادقة
1. اذهب إلى **Authentication** > **Settings**
2. تحت **Site URL**, ضع:
   - للتطوير: `http://localhost:5173`
   - للإنتاج: رابط موقعك
3. تحت **Redirect URLs**, أضف:
   ```
   http://localhost:5173/**
   https://your-domain.com/**
   ```
4. اضغط **Save**

### خطوة 4: الحصول على مفاتيح API
1. اذهب إلى **Settings** > **API**
2. احفظ هذه القيم:
   - **Project URL**: `https://your-project-ref.supabase.co`
   - **anon public**: هذا للفرونت إند
   - **service_role**: هذا للباك إند (لا تشاركه!)

---

## 🔧 إعداد Backend (Python FastAPI)

### خطوة 1: تفعيل البيئة الافتراضية
```bash
cd backend
# في Windows:
.venv\Scripts\activate
# في Mac/Linux:
source .venv/bin/activate
```

### خطوة 2: تثبيت المكتبات
```bash
pip install -r requirements.txt
```

### خطوة 3: إعداد متغيرات البيئة
1. انسخ ملف القالب:
```bash
cp .env.template .env
```

2. املأ الملف `.env` بالقيم الصحيحة:
```env
# من Supabase Settings > API
DATABASE_URL=postgresql://postgres:YOUR_DB_PASSWORD@db.YOUR_PROJECT_REF.supabase.co:5432/postgres
SUPABASE_URL=https://YOUR_PROJECT_REF.supabase.co
SUPABASE_ANON_KEY=your_anon_key_here
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key_here

# إعدادات JWT
JWT_SECRET_KEY=your-very-long-secret-key-at-least-32-characters-long
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# مفاتيح AI (اختيارية)
OPENAI_API_KEY=your-openai-key
GEMINI_API_KEY=your-gemini-key

# إعدادات التطبيق
DEBUG=True
ALLOW_ORIGINS=["http://localhost:5173", "http://localhost:3001"]
BILEL_ACCESS_CODE=1234
```

### خطوة 4: تشغيل الخادم
```bash
python main.py
```

يجب أن ترى:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### خطوة 5: اختبار الـ API
افتح المتصفح على: `http://localhost:8000/docs`

---

## ⚛️ إعداد Frontend (React + Vite)

### خطوة 1: تثبيت المكتبات
```bash
cd frontend
npm install
```

### خطوة 2: إعداد متغيرات البيئة
1. انسخ ملف القالب:
```bash
cp .env.template .env
```

2. املأ الملف `.env`:
```env
# رابط الـ Backend
VITE_API_URL=http://localhost:8000/api/v1

# إعدادات Supabase (من Settings > API)
VITE_SUPABASE_URL=https://YOUR_PROJECT_REF.supabase.co
VITE_SUPABASE_ANON_KEY=your_anon_key_here

# AI (اختياري)
VITE_GEMINI_API_KEY=your-gemini-key

# إعدادات التطبيق
VITE_APP_NAME=نظام إدارة الفنادق
VITE_ENVIRONMENT=development
```

### خطوة 3: تشغيل التطبيق
```bash
npm run dev
```

يجب أن ترى:
```
  ➜  Local:   http://localhost:5173/
```

---

## 🧪 اختبار النظام

### اختبار المصادقة:
1. افتح `http://localhost:5173`
2. جرب تسجيل حساب جديد
3. جرب تسجيل الدخول

### اختبار قاعدة البيانات:
1. في Supabase، اذهب لـ **Table Editor**
2. تحقق من وجود البيانات في جداول:
   - `users`
   - `rooms`
   - `guests`
   - `bookings`
   - `orders`

### اختبار الـ API:
1. افتح `http://localhost:8000/docs`
2. جرب endpoints مختلفة
3. تحقق من عمل المصادقة

---

## 🚀 النشر Production

### نشر Backend على Railway:

1. اذهب إلى [railway.app](https://railway.app)
2. سجل دخول بـ GitHub
3. اضغط "New Project" > "Deploy from GitHub repo"
4. اختر repository الخاص بك
5. اختر مجلد `backend`
6. في **Variables**, أضف:
   ```
   DATABASE_URL=your_supabase_database_url
   SUPABASE_URL=your_supabase_url
   SUPABASE_SERVICE_ROLE_KEY=your_service_role_key
   JWT_SECRET_KEY=your_production_secret_key
   ALLOW_ORIGINS=["https://your-frontend-domain.com"]
   ```
7. اضغط **Deploy**

### نشر Frontend على Vercel:

1. اذهب إلى [vercel.com](https://vercel.com)
2. سجل دخول بـ GitHub
3. اضغط "New Project"
4. اختر repository الخاص بك
5. ضع **Root Directory**: `frontend`
6. في **Environment Variables**, أضف:
   ```
   VITE_API_URL=https://your-backend-url.railway.app/api/v1
   VITE_SUPABASE_URL=your_supabase_url
   VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
   ```
7. اضغط **Deploy**

### نشر Frontend على Netlify (بديل):

1. اذهب إلى [netlify.com](https://netlify.com)
2. اسحب مجلد `frontend/dist` بعد تشغيل `npm run build`
3. أو اربط بـ GitHub repository
4. ضع **Build command**: `npm run build`
5. ضع **Publish directory**: `dist`
6. أضف Environment Variables كما هو مذكور أعلاه

---

## 🔒 اعتبارات الأمان

### لقاعدة البيانات:
- استخدم كلمات مرور قوية
- لا تشارك `service_role` key
- فعّل Row Level Security في Supabase

### للـ APIs:
- غيّر `JWT_SECRET_KEY` في الإنتاج
- استخدم HTTPS في الإنتاج
- فعّل rate limiting

### للمتغيرات:
- لا تضع مفاتيح سرية في Frontend
- استخدم ملفات `.env` منفصلة للإنتاج

---

## 🆘 حل المشاكل الشائعة

### خطأ في الاتصال بقاعدة البيانات:
```
psycopg2.OperationalError: could not connect to server
```
**الحل**: تأكد من صحة `DATABASE_URL` في `.env`

### خطأ في Supabase Auth:
```
SupabaseAuthError: Invalid JWT
```
**الحل**: تأكد من صحة `SUPABASE_ANON_KEY`

### خطأ CORS:
```
Access to fetch blocked by CORS policy
```
**الحل**: أضف رابط Frontend في `ALLOW_ORIGINS`

### موقع لا يعمل بعد النشر:
- تحقق من Environment Variables
- تحقق من الـ build logs
- تحقق من Supabase URL settings

---

## 📞 الدعم والمساعدة

- مشاكل Supabase: [docs.supabase.com](https://docs.supabase.com)
- مشاكل Vercel: [vercel.com/docs](https://vercel.com/docs)
- مشاكل Railway: [docs.railway.app](https://docs.railway.app)

---

## 🎯 الخطوات التالية

بعد إكمال الإعداد:
1. اضبط Row Level Security في Supabase
2. أضف monitoring وlogs
3. اعمل backup للبيانات
4. اضبط domain مخصص
5. فعّل CDN للصور

**🎉 مبروك! نظام إدارة الفنادق جاهز للاستخدام**