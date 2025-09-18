import React, { useEffect, useState } from 'react';
import axios from 'axios';

const POSDashboard: React.FC = () => {
  const [items, setItems] = useState<any[]>([]);
  const [order, setOrder] = useState<any[]>([]);
  const [total, setTotal] = useState(0);
  const outletId = localStorage.getItem('outlet_id');
  const outletName = localStorage.getItem('outlet_name');

  useEffect(() => {
    const fetchItems = async () => {
      const res = await axios.get(`${import.meta.env.VITE_API_URL}/pos/items?outlet_id=${outletId}`);
      setItems(res.data);
    };
    fetchItems();
  }, [outletId]);

  const addToOrder = (item: any) => {
    setOrder(prev => {
      const found = prev.find((i: any) => i.id === item.id);
      if (found) {
        return prev.map((i: any) => i.id === item.id ? { ...i, quantity: i.quantity + 1 } : i);
      }
      return [...prev, { ...item, quantity: 1 }];
    });
  };

  useEffect(() => {
    setTotal(order.reduce((sum, i) => sum + i.price * i.quantity, 0));
  }, [order]);

  return (
    <div className="pos-dashboard">
      <h2>{outletName} POS</h2>
      <div className="items-list">
        {items.map(item => (
          <div key={item.id} className="item-card">
            <div>{item.name}</div>
            <div>{item.price} DT</div>
            <button onClick={() => addToOrder(item)}>Add</button>
          </div>
        ))}
      </div>
      <div className="order-summary">
        <h3>Order Summary</h3>
        {order.map(i => (
          <div key={i.id}>{i.name} x {i.quantity} = {i.price * i.quantity} DT</div>
        ))}
        <div>Total: {total} DT</div>
        <button>Generate Invoice PDF</button>
      </div>
    </div>
  );
};

export default POSDashboard;
