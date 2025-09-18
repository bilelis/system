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

function App() {
  useEffect(() => {
    // Check if user is already logged in
    store.dispatch(getCurrentUser());
  }, []);

  return (
    <Provider store={store}>
      <ThemeProvider>
        <CssBaseline />
        <BrowserRouter>
          <Routes>
            <Route path="/login" element={<Login />} />
            <Route path="/pos-login" element={<POSLogin />} />
            <Route path="/bilel-control" element={<BilelControlPanel />} />
            
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
            
            {/* Redirect to dashboard if logged in, otherwise to login */}
            <Route path="/" element={<Navigate to="/dashboard" replace />} />
            <Route path="*" element={<Navigate to="/dashboard" replace />} />
          </Routes>
        </BrowserRouter>
      </ThemeProvider>
    </Provider>
  );
}

export default App;
