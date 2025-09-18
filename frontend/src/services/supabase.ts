/**
 * Supabase Client Configuration
 * إعدادات عميل Supabase للواجهة الأمامية
 */

import { createClient } from '@supabase/supabase-js';

// Supabase configuration
const supabaseUrl = import.meta.env.VITE_SUPABASE_URL || 'your-supabase-url';
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY || 'your-supabase-anon-key';

// Create Supabase client
export const supabase = createClient(supabaseUrl, supabaseAnonKey, {
  auth: {
    autoRefreshToken: true,
    persistSession: true,
    detectSessionInUrl: true
  }
});

// Database tables type definitions
export interface User {
  id: string;
  username?: string;
  email: string;
  full_name: string;
  role: 'admin' | 'receptionist' | 'cashier';
  created_at: string;
  updated_at: string;
}

export interface Room {
  id: string;
  room_number: string;
  room_type: string;
  floor: number;
  status: 'available' | 'occupied' | 'maintenance' | 'cleaning';
  rate_per_night: number;
  capacity: number;
  features?: any;
  created_at: string;
  updated_at: string;
}

export interface Guest {
  id: string;
  first_name: string;
  last_name: string;
  email?: string;
  phone?: string;
  nationality?: string;
  passport_no?: string;
  created_at: string;
  updated_at: string;
}

export interface Booking {
  id: string;
  guest_id: string;
  room_id: string;
  user_id: string;
  check_in_date: string;
  check_out_date: string;
  total_amount: number;
  status: 'pending' | 'confirmed' | 'checked_in' | 'checked_out' | 'cancelled';
  notes?: string;
  created_at: string;
  updated_at: string;
}

export interface Order {
  id: string;
  guest_id?: string;
  outlet_id: string;
  room_id?: string;
  user_id: string;
  order_number: string;
  status: 'pending' | 'preparing' | 'completed' | 'cancelled';
  total_amount: number;
  notes?: string;
  created_at: string;
  updated_at: string;
}

// Database type definition for TypeScript
export interface Database {
  public: {
    Tables: {
      users: {
        Row: User;
        Insert: Omit<User, 'id' | 'created_at' | 'updated_at'>;
        Update: Partial<Omit<User, 'id' | 'created_at' | 'updated_at'>>;
      };
      rooms: {
        Row: Room;
        Insert: Omit<Room, 'id' | 'created_at' | 'updated_at'>;
        Update: Partial<Omit<Room, 'id' | 'created_at' | 'updated_at'>>;
      };
      guests: {
        Row: Guest;
        Insert: Omit<Guest, 'id' | 'created_at' | 'updated_at'>;
        Update: Partial<Omit<Guest, 'id' | 'created_at' | 'updated_at'>>;
      };
      bookings: {
        Row: Booking;
        Insert: Omit<Booking, 'id' | 'created_at' | 'updated_at'>;
        Update: Partial<Omit<Booking, 'id' | 'created_at' | 'updated_at'>>;
      };
      orders: {
        Row: Order;
        Insert: Omit<Order, 'id' | 'created_at' | 'updated_at'>;
        Update: Partial<Omit<Order, 'id' | 'created_at' | 'updated_at'>>;
      };
    };
  };
}

export default supabase;