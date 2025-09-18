import axios from 'axios';

const API_BASE_URL = 'http://localhost:8005/api/v1';

// Simple auth service that bypasses the complex Redux setup
class SimpleAuthService {
  async login(username: string, password: string) {
    try {
      const response = await axios.post(`${API_BASE_URL}/simple-auth/simple-login`, {
        username,
        password
      });
      
      // Store token in localStorage
      localStorage.setItem('simple_token', response.data.access_token);
      
      return {
        success: true,
        token: response.data.access_token,
        user: response.data.user,
        error: null
      };
    } catch (error: any) {
      return {
        success: false,
        token: null,
        user: null,
        error: error.response?.data?.detail || 'Login failed'
      };
    }
  }
  
  async getUserInfo() {
    try {
      const token = localStorage.getItem('simple_token');
      if (!token) {
        throw new Error('No token found');
      }
      
      const response = await axios.get(`${API_BASE_URL}/simple-auth/simple-user?token=${token}`);
      return {
        success: true,
        user: response.data,
        error: null
      };
    } catch (error: any) {
      return {
        success: false,
        user: null,
        error: error.response?.data?.detail || 'Failed to get user info'
      };
    }
  }
  
  logout() {
    localStorage.removeItem('simple_token');
  }
  
  isAuthenticated() {
    return !!localStorage.getItem('simple_token');
  }
}

const simpleAuthService = new SimpleAuthService();
export default simpleAuthService;