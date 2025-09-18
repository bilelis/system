@echo off
echo Starting Hotel Management System...
echo.

echo [1/3] Starting Backend Server...
start "Backend" cmd /k "cd backend && python -m venv .venv && .venv\Scripts\activate && pip install -r requirements.txt && python main.py"

echo [2/3] Starting Frontend Development Server...
start "Frontend" cmd /k "cd frontend && npm install && npm run dev"

echo [3/3] Starting Gateway Service...
start "Gateway" cmd /k "cd gateway && npm install && npm start"

echo.
echo ====================================
echo  Hotel Management System Started!
echo ====================================
echo.
echo Frontend: http://localhost:5173
echo Backend API: http://localhost:8000
echo Gateway: http://localhost:3001
echo.
echo Bilel Control Panel: http://localhost:5173/bilel-control
echo Access Code: 1234
echo.
echo Press any key to exit this window...
pause > nul