import React from 'react';
import { KpiData } from '../types';

// FIX: Refactored all JSX to React.createElement calls to fix compilation errors.
// JSX syntax is not supported in .ts files, only in .tsx files.
// Using React.createElement is the standard way to create elements without JSX.
const CurrencyDollarIcon = (props: React.SVGProps<SVGSVGElement>) => (
  React.createElement('svg', { xmlns: "http://www.w3.org/2000/svg", fill: "none", viewBox: "0 0 24 24", strokeWidth: 1.5, stroke: "currentColor", ...props },
    React.createElement('path', { strokeLinecap: "round", strokeLinejoin: "round", d: "M12 6v12m-3-2.818.879.659c1.171.879 3.07.879 4.242 0 1.172-.879 1.172-2.303 0-3.182C13.536 12.219 12.768 12 12 12c-.725 0-1.45-.22-2.003-.659-1.106-.879-1.106-2.303 0-3.182s2.9-.879 4.006 0l.415.33M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" })
  )
);
const BuildingOfficeIcon = (props: React.SVGProps<SVGSVGElement>) => (
  React.createElement('svg', { xmlns: "http://www.w3.org/2000/svg", fill: "none", viewBox: "0 0 24 24", strokeWidth: 1.5, stroke: "currentColor", ...props },
    React.createElement('path', { strokeLinecap: "round", strokeLinejoin: "round", d: "M3.75 21h16.5M4.5 3h15M5.25 3v18m13.5-18v18M9 6.75h1.5m-1.5 3h1.5m-1.5 3h1.5m3-6h1.5m-1.5 3h1.5m-1.5 3h1.5M9 21v-3.375c0-.621.504-1.125 1.125-1.125h3.75c.621 0 1.125.504 1.125 1.125V21" })
  )
);
const SparklesIcon = (props: React.SVGProps<SVGSVGElement>) => (
  React.createElement('svg', { xmlns: "http://www.w3.org/2000/svg", fill: "none", viewBox: "0 0 24 24", strokeWidth: 1.5, stroke: "currentColor", ...props },
    React.createElement('path', { strokeLinecap: "round", strokeLinejoin: "round", d: "M9.813 15.904 9 18.75l-.813-2.846a4.5 4.5 0 0 0-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 0 0 3.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 0 0 3.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 0 0-3.09 3.09ZM18.259 8.715 18 9.75l-.259-1.035a3.375 3.375 0 0 0-2.455-2.456L14.25 6l1.036-.259a3.375 3.375 0 0 0 2.455-2.456L18 2.25l.259 1.035a3.375 3.375 0 0 0 2.456 2.456L21.75 6l-1.035.259a3.375 3.375 0 0 0-2.456 2.456Z" })
  )
);
const UserGroupIcon = (props: React.SVGProps<SVGSVGElement>) => (
  React.createElement('svg', { xmlns: "http://www.w3.org/2000/svg", fill: "none", viewBox: "0 0 24 24", strokeWidth: 1.5, stroke: "currentColor", ...props },
    React.createElement('path', { strokeLinecap: "round", strokeLinejoin: "round", d: "M18 18.72a9.094 9.094 0 0 0 3.741-.479 3 3 0 0 0-4.682-2.72m-7.5-2.226A3 3 0 0 1 18 15.72a6 6 0 0 1-3.75 .984m-7.5 0a3 3 0 0 1-3-3m3 3a3 3 0 0 0-3-3m-3.75 0h.008v.015h-.008V12Zm-3.75 0h.008v.015h-.008V12Zm3.75 0h.008v.015h-.008V12Zm3.75 0h.008v.015h-.008V12Zm-3.75 0h.008v.015h-.008V12Zm9.75-3a3.75 3.75 0 1 0 0-7.5 3.75 3.75 0 0 0 0 7.5Zm-12-3a3.75 3.75 0 1 0 0-7.5 3.75 3.75 0 0 0 0 7.5Z" })
  )
);

export const kpiData: KpiData[] = [
  {
    title: "Total Revenue",
    value: "$1.2M",
    change: "+12.5%",
    changeType: "increase",
    icon: React.createElement(CurrencyDollarIcon, { className: "h-8 w-8 text-green-400" }),
  },
  {
    title: "Occupancy Rate",
    value: "92.8%",
    change: "+5.1%",
    changeType: "increase",
    icon: React.createElement(BuildingOfficeIcon, { className: "h-8 w-8 text-blue-400" }),
  },
  {
    title: "Top POS Item",
    value: "Espresso",
    change: "782 units",
    changeType: "increase",
    icon: React.createElement(SparklesIcon, { className: "h-8 w-8 text-yellow-400" }),
  },
  {
    title: "Avg. Guest Spending",
    value: "$432.10",
    change: "-2.3%",
    changeType: "decrease",
    icon: React.createElement(UserGroupIcon, { className: "h-8 w-8 text-purple-400" }),
  },
];

export const revenueSplitData = [
  { name: 'Room Bookings', value: 750000, fill: '#3b82f6' },
  { name: 'Restaurant & Bar', value: 320000, fill: '#8b5cf6' },
  { name: 'Spa & Wellness', value: 95000, fill: '#10b981' },
  { name: 'Other Services', value: 35000, fill: '#f97316' },
];

export const arprData = [
  { name: 'Jan', arpr: 280 },
  { name: 'Feb', arpr: 310 },
  { name: 'Mar', arpr: 300 },
  { name: 'Apr', arpr: 340 },
  { name: 'May', arpr: 360 },
  { name: 'Jun', arpr: 410 },
  { name: 'Jul', arpr: 450 },
];
