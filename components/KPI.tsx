
import React from 'react';
import { KpiData } from '../types';

interface KpiCardProps {
  data: KpiData;
}

const KpiCard: React.FC<KpiCardProps> = ({ data }) => {
  const { title, value, change, changeType, icon } = data;
  const isIncrease = changeType === 'increase';

  return (
    <div className="bg-gray-800/50 border border-gray-700/50 rounded-xl p-6 flex items-start justify-between">
      <div>
        <p className="text-sm font-medium text-gray-400">{title}</p>
        <p className="text-3xl font-bold mt-2">{value}</p>
        <div className={`mt-2 flex items-center text-sm ${isIncrease ? 'text-green-400' : 'text-red-400'}`}>
          {isIncrease ? (
            <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
            </svg>
          ) : (
            <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11 17l-5-5m0 0l5-5m-5 5h12" />
            </svg>
          )}
          <span>{change}</span>
        </div>
      </div>
      <div className="bg-gray-900/50 rounded-full p-3">
        {icon}
      </div>
    </div>
  );
};

export default KpiCard;
