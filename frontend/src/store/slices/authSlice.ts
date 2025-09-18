import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import type { PayloadAction } from '@reduxjs/toolkit';
import api from '../../services/api';

// Define types
interface User {
  id: number;
  email: string;
  name: string;
  role: string;
}

interface AuthState {
  user: User | null;
  token: string | null;
  isAuthenticated: boolean;
  loading: boolean;
  error: string | null;
}

// Initial state
const initialState: AuthState = {
  user: null,
  token: localStorage.getItem('token'),
  isAuthenticated: !!localStorage.getItem('token'),
  loading: false,
  error: null,
};

// Login thunk
export const login = createAsyncThunk(
  'auth/login',
  async (credentials: { email: string; password: string }, { rejectWithValue }) => {
    try {
      // Send JSON data directly
      const response = await api.post('/auth/login', {
        username: credentials.email, // Backend uses username field for email
        password: credentials.password
      });
      
      const { access_token, token_type, role, user_id } = response.data;
      
      // Store token in localStorage
      localStorage.setItem('token', access_token);
      
      // Create user object from response
      const user = {
        id: parseInt(user_id),
        email: credentials.email,
        name: credentials.email, // We'll get the real name from /me endpoint later
        role: role
      };
      
      return { token: access_token, user };
    } catch (error: any) {
      return rejectWithValue(error.response?.data?.detail || error.response?.data?.message || 'Login failed');
    }
  }
);

// Logout thunk
export const logout = createAsyncThunk('auth/logout', async () => {
  localStorage.removeItem('token');
  return null;
});

// Get current user thunk
export const getCurrentUser = createAsyncThunk(
  'auth/getCurrentUser',
  async (_, { rejectWithValue, getState }) => {
    try {
      const { auth } = getState() as { auth: AuthState };
      
      if (!auth.token) {
        return rejectWithValue('No token found');
      }
      
      const response = await api.get('/auth/me');
      return response.data;
    } catch (error: any) {
      // If token is invalid, logout
      if (error.response?.status === 401) {
        localStorage.removeItem('token');
      }
      return rejectWithValue(error.response?.data?.message || 'Failed to get user');
    }
  }
);

// Auth slice
const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    clearError: (state) => {
      state.error = null;
    },
  },
  extraReducers: (builder) => {
    // Login cases
    builder
      .addCase(login.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(login.fulfilled, (state, action: PayloadAction<{ token: string; user: User }>) => {
        state.loading = false;
        state.isAuthenticated = true;
        state.token = action.payload.token;
        state.user = action.payload.user;
      })
      .addCase(login.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload as string;
      })
      
      // Logout cases
      .addCase(logout.fulfilled, (state) => {
        state.isAuthenticated = false;
        state.token = null;
        state.user = null;
      })
      
      // Get current user cases
      .addCase(getCurrentUser.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(getCurrentUser.fulfilled, (state, action: PayloadAction<User>) => {
        state.loading = false;
        state.user = action.payload;
        state.isAuthenticated = true;
      })
      .addCase(getCurrentUser.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload as string;
        state.isAuthenticated = false;
        state.token = null;
        state.user = null;
      });
  },
});

export const { clearError } = authSlice.actions;
export default authSlice.reducer;