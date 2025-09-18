import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const POSLogin: React.FC = () => {
  const [code, setCode] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const res = await axios.post(`${import.meta.env.VITE_API_URL}/pos/login`, { code });
      localStorage.setItem('pos_token', res.data.access_token);
      localStorage.setItem('outlet_id', res.data.outlet_id);
      localStorage.setItem('outlet_name', res.data.outlet_name);
      navigate(`/pos/${res.data.outlet_id}`);
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Code incorrect');
    }
  };

  return (
    <div className="pos-login-container">
      <form onSubmit={handleLogin}>
        <h2>POS Login</h2>
        <input type="password" maxLength={4} placeholder="Enter 4-digit code" value={code} onChange={e => setCode(e.target.value)} required />
        {error && <div className="error">{error}</div>}
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default POSLogin;
