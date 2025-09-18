import { useEffect } from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { Provider } from 'react-redux';
import { CssBaseline } from '@mui/material';
import './App.css';

// Theme Provider
import { ThemeProvider } from './theme/ThemeProvider';

// Store
import { store } from './store';
import { getCurrentUser } from './store/slices/authSlice';

// i18n
import './i18n/i18n';

// Components
import Layout from './components/layout/Layout';
import ProtectedRoute from './components/auth/ProtectedRoute';

// Pages
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import Billing from './pages/Billing';
import BilelControlPanel from './pages/BilelControlPanel';
import Reception from './pages/Reception';
import POS from './pages/POS';
import POSLogin from './pages/POSLogin';
import POSDashboard from './pages/POSDashboard';
import Debug from './pages/Debug';

function App() {
  useEffect(() => {
    // Check if user is already logged in
    store.dispatch(getCurrentUser());
  }, []);

  // Temporary debug mode - remove after testing
  const debugMode = false;
  
  if (debugMode) {
    return (
      <Provider store={store}>
        <ThemeProvider>
          <CssBaseline />
          <Debug />
        </ThemeProvider>
      </Provider>
    );
  }

  return (
    <Provider store={store}>
      <ThemeProvider>
        <CssBaseline />
        <BrowserRouter>
          <Routes>
            <Route path="/login" element={<Login />} />
            <Route path="/pos-login" element={<POSLogin />} />
            <Route path="/bilel-control" element={<BilelControlPanel />} />
            <Route path="/debug" element={<Debug />} />
            
            {/* Protected Routes */}
            <Route element={<ProtectedRoute />}>
              <Route element={<Layout />}>
                <Route path="/dashboard" element={<Dashboard />} />
                <Route path="/billing" element={<Billing />} />
                <Route path="/reception" element={<Reception />} />
                <Route path="/pos" element={<POS />} />
                <Route path="/pos-dashboard" element={<POSDashboard />} />
              </Route>
            </Route>
            
            {/* Redirect to login for now */}
            <Route path="/" element={<Navigate to="/login" replace />} />
            <Route path="*" element={<Navigate to="/login" replace />} />
          </Routes>
        </BrowserRouter>
      </ThemeProvider>
    </Provider>
  );
}

export default App;
