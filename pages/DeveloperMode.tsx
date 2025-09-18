
import React from 'react';
import Chatbot from '../components/Chatbot';

const fakeFileStructure = [
  { name: 'backend (FastAPI)', children: ['main.py', 'routers/', 'models.py'] },
  { name: 'gateway (Node.js)', children: ['server.js', 'routes/', 'package.json'] },
  { name: 'frontend (React)', children: ['App.tsx', 'components/', 'pages/'] },
  { name: 'database', children: ['schema.sql', 'migrations/'] },
  { name: '.dockerignore', children: [] },
  { name: 'docker-compose.yml', children: [] },
];

const fakeCode = `
// FILE: frontend/pages/Dashboard.tsx

import React from 'react';
import { BarChart, Bar, ResponsiveContainer } from 'recharts';
import KpiCard from '../components/KPI';
import { kpiData, arprData } from '../data/mockData';

const Dashboard: React.FC = () => {
  // TODO: Add AI-powered anomaly detection widget
  return (
    <div className="space-y-8">
      <h1 className="text-3xl font-bold">Welcome back, Bilel Ayari</h1>
      
      {/* KPIs */}
      <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
        {kpiData.map((kpi, index) => (
          <KpiCard key={index} data={kpi} />
        ))}
      </div>
    </div>
  );
};

export default Dashboard;
`;


const DeveloperMode: React.FC = () => {
  return (
    <div className="h-full flex flex-col space-y-6">
      <div>
        <h1 className="text-3xl font-bold">Developer Mode</h1>
        <p className="text-gray-400 mt-1">Direct access to system architecture and AI-assisted development.</p>
      </div>
      <div className="flex-1 grid grid-cols-1 lg:grid-cols-3 gap-6 h-[calc(100%-68px)]">
        {/* Code & File Structure */}
        <div className="lg:col-span-2 flex flex-col gap-6 h-full">
          <div className="flex flex-col bg-gray-800/50 border border-gray-700/50 rounded-xl overflow-hidden h-full">
            <div className="p-4 border-b border-gray-700/50">
              <h3 className="font-semibold text-white">Code Editor</h3>
            </div>
            {/* Fake File Explorer */}
            <div className="flex h-full">
              <div className="w-1/3 bg-gray-950/50 p-4 border-r border-gray-700/50">
                <h4 className="font-medium text-sm text-gray-300 mb-2">File Explorer</h4>
                <ul>
                  {fakeFileStructure.map(item => (
                    <li key={item.name} className="text-sm text-gray-400 py-1">
                      {item.children.length > 0 ? '📁' : '📄'} {item.name}
                    </li>
                  ))}
                </ul>
              </div>
              {/* Fake Code Editor */}
              <div className="w-2/3 p-4 font-mono text-sm bg-gray-900 overflow-auto">
                <pre className="text-gray-300"><code>{fakeCode}</code></pre>
              </div>
            </div>
          </div>
        </div>
        
        {/* AI Chatbot */}
        <div className="lg:col-span-1 h-full">
          <Chatbot />
        </div>
      </div>
    </div>
  );
};

export default DeveloperMode;
