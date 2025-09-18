/**
 * Authentication Service with Supabase Integration
 * خدمة المصادقة مع دمج Supabase
 */

import api from './api';
import { supabase } from './supabase';

// Types
interface LoginCredentials {
  email: string;
  password: string;
}

interface RegisterData {
  name: string;
  email: string;
  password: string;
  role?: string;
}

interface User {
  id: number;
  name: string;
  email: string;
  role: string;
}

interface AuthResponse {
  token: string;
  user: User;
}

interface SupabaseSignUpRequest {
  email: string;
  password: string;
  full_name: string;
  role: string;
}

interface SupabaseSignInRequest {
  email: string;
  password: string;
}

class AuthService {
  private useSupabase: boolean;

  constructor() {
    // Check if Supabase is configured
    this.useSupabase = import.meta.env.VITE_SUPABASE_URL && 
                      import.meta.env.VITE_SUPABASE_URL !== 'your-supabase-url';
  }

  // === Traditional API Authentication ===
  
  async login(credentials: LoginCredentials): Promise<AuthResponse> {
    const response = await api.post<AuthResponse>('/auth/login', credentials);
    return response.data;
  }

  async register(data: RegisterData): Promise<AuthResponse> {
    const response = await api.post<AuthResponse>('/auth/register', data);
    return response.data;
  }

  async getCurrentUser(): Promise<User> {
    const response = await api.get<User>('/auth/me');
    return response.data;
  }

  // === Supabase Authentication ===

  async supabaseSignUp(userData: SupabaseSignUpRequest): Promise<any> {
    if (!this.useSupabase) {
      // Fallback to traditional registration via backend
      return await api.post('/auth/supabase/signup', userData);
    }

    const { data, error } = await supabase.auth.signUp({
      email: userData.email,
      password: userData.password,
      options: {
        data: {
          full_name: userData.full_name,
          role: userData.role
        }
      }
    });

    if (error) {
      throw new Error(error.message);
    }

    return {
      user: data.user,
      session: data.session,
      message: 'User registered successfully. Please check your email for verification.'
    };
  }

  async supabaseSignIn(credentials: SupabaseSignInRequest): Promise<any> {
    if (!this.useSupabase) {
      // Fallback to backend Supabase auth
      const response = await api.post('/auth/supabase/signin', credentials);
      
      if (response.data.access_token) {
        localStorage.setItem('supabase_token', response.data.access_token);
        localStorage.setItem('supabase_refresh_token', response.data.refresh_token);
        localStorage.setItem('user_data', JSON.stringify(response.data.user));
      }
      
      return response.data;
    }

    const { data, error } = await supabase.auth.signInWithPassword({
      email: credentials.email,
      password: credentials.password
    });

    if (error) {
      throw new Error(error.message);
    }

    if (data.session) {
      localStorage.setItem('supabase_token', data.session.access_token);
      localStorage.setItem('supabase_refresh_token', data.session.refresh_token);
      localStorage.setItem('user_data', JSON.stringify(data.user));
    }

    return {
      access_token: data.session?.access_token,
      refresh_token: data.session?.refresh_token,
      user: data.user
    };
  }

  async supabaseSignOut(): Promise<void> {
    if (!this.useSupabase) {
      // Fallback to backend signout
      const token = localStorage.getItem('supabase_token');
      if (token) {
        try {
          await api.post('/auth/supabase/signout', { access_token: token });
        } catch (error) {
          console.error('Backend signout failed:', error);
        }
      }
    } else {
      await supabase.auth.signOut();
    }

    // Clear all stored auth data
    localStorage.removeItem('supabase_token');
    localStorage.removeItem('supabase_refresh_token');
    localStorage.removeItem('user_data');
    localStorage.removeItem('token');
  }

  // === Session Management ===

  getCurrentSession(): any {
    const supabaseToken = localStorage.getItem('supabase_token');
    const traditionalToken = localStorage.getItem('token');
    const userData = localStorage.getItem('user_data');

    if (supabaseToken) {
      return {
        type: 'supabase',
        token: supabaseToken,
        user: userData ? JSON.parse(userData) : null
      };
    }

    if (traditionalToken) {
      return {
        type: 'traditional',
        token: traditionalToken
      };
    }

    return null;
  }

  // === Legacy Methods (Updated) ===
  
  async logout(): Promise<void> {
    const session = this.getCurrentSession();
    
    if (session?.type === 'supabase') {
      await this.supabaseSignOut();
    } else {
      // Traditional logout
      await api.post('/auth/logout');
      localStorage.removeItem('token');
    }
  }

  isAuthenticated(): boolean {
    return !!this.getCurrentSession();
  }

  // === Utility Methods ===

  getAuthMode(): 'supabase' | 'traditional' | 'hybrid' {
    if (this.useSupabase) {
      return 'supabase';
    }
    return 'hybrid'; // Support both modes via backend
  }
}

export default new AuthService();