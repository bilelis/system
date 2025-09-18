#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Database Setup Script for Hotel Management System with Supabase
إعداد قاعدة البيانات لنظام إدارة الفنادق مع Supabase

Run this script to automatically create all database tables and sample data.
"""

import os
import sys
from pathlib import Path
from supabase import create_client, Client
from dotenv import load_dotenv

def load_sql_file(filepath):
    """Load SQL file content"""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        return None
    except Exception as e:
        print(f"❌ Error reading file {filepath}: {e}")
        return None

def setup_database():
    """Set up database tables and sample data"""
    print("🚀 Setting up Hotel Management System Database...")
    
    # Load environment variables
    env_path = Path("backend/.env")
    if not env_path.exists():
        print("❌ Backend .env file not found!")
        print("Please ensure backend/.env exists with Supabase credentials")
        return False
    
    load_dotenv(env_path)
    
    # Get Supabase credentials
    url = os.getenv("SUPABASE_URL")
    service_key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    
    if not url or not service_key:
        print("❌ Missing Supabase credentials in .env file")
        print("Required: SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY")
        return False
    
    try:
        # Create Supabase client
        supabase: Client = create_client(url, service_key)
        print("✅ Connected to Supabase")
        
        # Step 1: Create schema and tables
        print("\n📊 Creating database schema...")
        schema_sql = load_sql_file("database/supabase_schema.sql")
        if schema_sql:
            result = supabase.rpc('exec_sql', {'sql': schema_sql})
            print("✅ Database schema created successfully")
        
        # Step 2: Insert sample data
        print("\n📝 Inserting sample data...")
        sample_data_sql = load_sql_file("database/supabase_sample_data.sql")
        if sample_data_sql:
            result = supabase.rpc('exec_sql', {'sql': sample_data_sql})
            print("✅ Sample data inserted successfully")
        
        # Step 3: Verify tables exist
        print("\n🔍 Verifying database setup...")
        tables = [
            'users', 'rooms', 'guests', 'bookings', 
            'outlets', 'items', 'orders', 'order_lines', 'payments'
        ]
        
        for table in tables:
            try:
                result = supabase.table(table).select("*").limit(1).execute()
                print(f"✅ Table '{table}' exists and accessible")
            except Exception as e:
                print(f"⚠️  Issue with table '{table}': {e}")
        
        print("\n🎉 Database setup completed successfully!")
        print("\nNext steps:")
        print("1. Start backend: cd backend && python main.py")
        print("2. Start frontend: cd frontend && npm run dev")
        print("3. Access system: http://localhost:5173")
        
        return True
        
    except Exception as e:
        print(f"❌ Error setting up database: {e}")
        return False

def main():
    """Main function"""
    print("=" * 60)
    print("🏨 Hotel Management System - Database Setup")
    print("نظام إدارة الفنادق - إعداد قاعدة البيانات")
    print("=" * 60)
    
    if setup_database():
        print("\n✅ Setup completed successfully!")
        print("Your hotel management system is ready to use! 🏨")
    else:
        print("\n❌ Setup failed. Please check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()