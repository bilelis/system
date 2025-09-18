#!/usr/bin/env python3

"""
Initialize SQLite database with schema and test users
إعداد قاعدة البيانات SQLite مع البيانات التجريبية
"""

import sqlite3
import os
import uuid
from passlib.context import CryptContext

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_tables():
    """Create database tables"""
    
    # Database file path
    db_path = "hotel_management.db"
    
    # Connect to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("📊 Creating database tables...")
    
    # Create users table (if not exists)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL,
            full_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Create other essential tables (if not exists)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS guests (
            id TEXT PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT,
            phone TEXT,
            nationality TEXT,
            passport_no TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rooms (
            id TEXT PRIMARY KEY,
            room_number TEXT UNIQUE NOT NULL,
            room_type TEXT NOT NULL,
            floor INTEGER NOT NULL,
            status TEXT DEFAULT 'available',
            rate_per_night DECIMAL(10,2) NOT NULL,
            capacity INTEGER NOT NULL,
            features TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    print("✅ Tables created successfully!")
    
    # Insert test users (only if they don't exist)
    print("👥 Creating test users...")
    
    # Hash the password
    password_hash = pwd_context.hash("password123")
    
    test_users = [
        (str(uuid.uuid4()), "admin", password_hash, "admin", "Hotel Administrator", "admin@hotel.com"),
        (str(uuid.uuid4()), "reception1", password_hash, "receptionist", "John Smith", "reception@hotel.com"),
        (str(uuid.uuid4()), "cashier1", password_hash, "cashier", "Sarah Johnson", "cashier@hotel.com"),
    ]
    
    # Check if users exist before inserting
    for user in test_users:
        cursor.execute("SELECT id FROM users WHERE username = ?", (user[1],))
        if not cursor.fetchone():
            cursor.execute("""
                INSERT INTO users (id, username, password_hash, role, full_name, email)
                VALUES (?, ?, ?, ?, ?, ?)
            """, user)
    
    # Insert test rooms (only if they don't exist)
    test_rooms = [
        (str(uuid.uuid4()), "101", "Standard", 1, "available", 100.00, 2, '{"wifi": true, "tv": true}'),
        (str(uuid.uuid4()), "102", "Standard", 1, "available", 100.00, 2, '{"wifi": true, "tv": true}'),
        (str(uuid.uuid4()), "201", "Deluxe", 2, "available", 150.00, 2, '{"wifi": true, "tv": true, "balcony": true}'),
    ]
    
    # Check if rooms exist before inserting
    for room in test_rooms:
        cursor.execute("SELECT id FROM rooms WHERE room_number = ?", (room[1],))
        if not cursor.fetchone():
            cursor.execute("""
                INSERT INTO rooms (id, room_number, room_type, floor, status, rate_per_night, capacity, features)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, room)
    
    # Commit and close
    conn.commit()
    conn.close()
    
    print("✅ Database initialized successfully!")
    print("\n📋 Test Credentials:")
    print("👤 Admin: username='admin', password='password123'")
    print("👤 Receptionist: username='reception1', password='password123'")
    print("👤 Cashier: username='cashier1', password='password123'")

if __name__ == "__main__":
    create_tables()