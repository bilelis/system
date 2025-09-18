#!/usr/bin/env python3

"""
Simple test endpoint to check database connectivity
اختبار سهل للتحقق من اتصال قاعدة البيانات
"""

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User

app = FastAPI()

@app.get("/test-db")
def test_database(db: Session = Depends(get_db)):
    """Test database connection and return users"""
    try:
        users = db.query(User).all()
        return {
            "status": "success",
            "users_count": len(users),
            "users": [{"username": u.username, "role": u.role} for u in users]
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("test_endpoint:app", host="0.0.0.0", port=8001, reload=True)