import React, { useEffect, useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid } from 'recharts';
import axios from 'axios';

function Dashboard() {
  const [metrics, setMetrics] = useState([]);

  useEffect(() => {
    axios.post('/api/ai/query', { query: "Show sales metrics" })
      .then(res => setMetrics([{ name: "Sales", value: res.data.result.totalSales || 0 }]))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Sales Overview</h2>
      <BarChart width={600} height={300} data={metrics}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="value" fill="#82ca9d" />
      </BarChart>
    </div>
  );
}

export default Dashboard;
