
import React, { useState } from 'react';

interface LoginPageProps {
  onLogin: (pin: string) => boolean;
}

const LoginPage: React.FC<LoginPageProps> = ({ onLogin }) => {
  const [pin, setPin] = useState<string>('');
  const [error, setError] = useState<string>('');

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    // Only allow numeric input
    if (/^\d*$/.test(value) && value.length <= 4) {
      setPin(value);
      setError('');
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (pin.length !== 4) {
      setError('PIN must be 4 digits.');
      return;
    }
    const success = onLogin(pin);
    if (!success) {
      setError('Access Denied. Invalid PIN.');
      setPin('');
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-900">
      <div className="w-full max-w-md p-8 space-y-8 bg-gray-800/50 border border-gray-700/50 rounded-2xl shadow-2xl shadow-indigo-600/10">
        <div className="text-center">
          <h1 className="text-3xl font-black text-white">Bilel Control Panel</h1>
          <p className="mt-2 text-gray-400">Private Access Only</p>
        </div>
        <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
          <div className="rounded-md shadow-sm -space-y-px">
            <div>
              <label htmlFor="pin-code" className="sr-only">
                PIN Code
              </label>
              <input
                id="pin-code"
                name="pin"
                type="password"
                autoComplete="off"
                required
                className="appearance-none rounded-lg relative block w-full px-3 py-4 border border-gray-600 bg-gray-900 placeholder-gray-500 text-white text-center text-2xl tracking-[1em] focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
                placeholder="••••"
                value={pin}
                onChange={handleInputChange}
                maxLength={4}
              />
            </div>
          </div>
          {error && <p className="text-red-400 text-center text-sm">{error}</p>}
          <div>
            <button
              type="submit"
              className="group relative w-full flex justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 focus:ring-offset-gray-900 transition-colors"
            >
              Authenticate
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default LoginPage;
