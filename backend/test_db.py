#!/usr/bin/env python3

"""
Simple database connection test
اختبار اتصال قاعدة البيانات
"""

import os
import asyncio
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

def test_database_connection():
    """Test database connection and check if tables exist"""
    print("Testing database connection...")
    print(f"Database URL: {settings.DATABASE_URL}")
    
    try:
        # Create engine
        engine = create_engine(settings.DATABASE_URL)
        
        # Test connection
        with engine.connect() as connection:
            print("✅ Database connection successful!")
            
            # Check if users table exists
            if 'sqlite' in settings.DATABASE_URL:
                # SQLite syntax
                result = connection.execute(text("""
                    SELECT name FROM sqlite_master 
                    WHERE type='table' AND name='users';
                """))
            else:
                # PostgreSQL syntax
                result = connection.execute(text("""
                    SELECT table_name 
                    FROM information_schema.tables 
                    WHERE table_schema = 'public' 
                    AND table_name = 'users';
                """))
            
            users_table = result.fetchone()
            if users_table:
                print("✅ Users table exists!")
                
                # Check users count
                result = connection.execute(text("SELECT COUNT(*) FROM users;"))
                count_row = result.fetchone()
                count = count_row[0] if count_row else 0
                print(f"📊 Users count: {count}")
                
                # List users
                result = connection.execute(text("SELECT username, email, role FROM users;"))
                users = result.fetchall()
                print("👥 Users in database:")
                for user in users:
                    print(f"  - {user[0]} ({user[1]}) - {user[2]}")
                    
            else:
                print("❌ Users table does not exist!")
                print("📋 Available tables:")
                if 'sqlite' in settings.DATABASE_URL:
                    # SQLite syntax for listing tables
                    result = connection.execute(text("""
                        SELECT name FROM sqlite_master 
                        WHERE type='table' 
                        ORDER BY name;
                    """))
                else:
                    # PostgreSQL syntax
                    result = connection.execute(text("""
                        SELECT table_name 
                        FROM information_schema.tables 
                        WHERE table_schema = 'public'
                        ORDER BY table_name;
                    """))
                tables = result.fetchall()
                for table in tables:
                    print(f"  - {table[0]}")
            
    except Exception as e:
        print(f"❌ Database connection failed: {e}")

if __name__ == "__main__":
    test_database_connection()