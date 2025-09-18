
import React, { useState, useCallback } from 'react';
import LoginPage from './pages/Login';
import Dashboard from './pages/Dashboard';
import DeveloperMode from './pages/DeveloperMode';
import PlaceholderPage from './pages/PlaceholderPage';
import Sidebar from './components/Sidebar';
import { Page } from './types';
import { CORRECT_PIN } from './constants';

const App: React.FC = () => {
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);
  const [activePage, setActivePage] = useState<Page>('dashboard');

  const handleLogin = useCallback((pin: string) => {
    if (pin === CORRECT_PIN) {
      setIsAuthenticated(true);
      return true;
    }
    return false;
  }, []);

  const handleLogout = useCallback(() => {
    setIsAuthenticated(false);
    setActivePage('dashboard');
  }, []);

  const renderPage = () => {
    switch (activePage) {
      case 'dashboard':
        return <Dashboard />;
      case 'developer':
        return <DeveloperMode />;
      case 'rooms':
        return <PlaceholderPage title="Room Management" icon="rooms" />;
      case 'guests':
        return <PlaceholderPage title="Guest Records" icon="guests" />;
      case 'pos':
        return <PlaceholderPage title="Point of Sale Terminals" icon="pos" />;
      default:
        return <Dashboard />;
    }
  };

  if (!isAuthenticated) {
    return <LoginPage onLogin={handleLogin} />;
  }

  return (
    <div className="flex h-screen bg-gray-900 text-gray-100">
      <Sidebar activePage={activePage} setActivePage={setActivePage} onLogout={handleLogout} />
      <main className="flex-1 p-4 sm:p-6 lg:p-8 overflow-y-auto">
        {renderPage()}
      </main>
    </div>
  );
};

export default App;
