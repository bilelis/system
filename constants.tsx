
import React from 'react';
import { NavItem, Page } from './types';

export const CORRECT_PIN = '2424';

const ChartBarIcon = (props: React.SVGProps<SVGSVGElement>) => (
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" {...props}><path strokeLinecap="round" strokeLinejoin="round" d="M3 13.125C3 12.504 3.504 12 4.125 12h2.25c.621 0 1.125.504 1.125 1.125v6.75C7.5 20.496 6.996 21 6.375 21h-2.25A1.125 1.125 0 0 1 3 19.875v-6.75ZM9.75 8.625c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125v11.25c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 0 1-1.125-1.125V8.625ZM16.5 4.125c0-.621.504-1.125 1.125-1.125h2.25C20.496 3 21 3.504 21 4.125v15.75c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 0 1-1.125-1.125V4.125Z" /></svg>
);
const KeyIcon = (props: React.SVGProps<SVGSVGElement>) => (
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" {...props}><path strokeLinecap="round" strokeLinejoin="round" d="M15.75 5.25a3 3 0 0 1 3 3m3 0a6 6 0 0 1-7.029 5.912c-.563-.097-1.159.026-1.563.43L10.5 17.25H8.25v2.25H6v2.25H2.25v-2.818c0-.597.237-1.17.659-1.591l6.499-6.499c.404-.404.527-1 .43-1.563A6 6 0 1 1 21.75 8.25Z" /></svg>
);
const UsersIcon = (props: React.SVGProps<SVGSVGElement>) => (
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" {...props}><path strokeLinecap="round" strokeLinejoin="round" d="M15 19.128a9.38 9.38 0 0 0 2.625.372 9.337 9.337 0 0 0 4.121-2.257c.709-.709.709-1.854 0-2.563a9.337 9.337 0 0 0-4.12-2.257 9.38 9.38 0 0 0-2.625.372M15 19.128v-1.5a7.5 7.5 0 0 0-7.5-7.5h-1.5m-6.375 4.125a9.375 9.375 0 0 1 15-4.125m0 0a9.375 9.375 0 0 1 4.125 15m-15-4.125a9.375 9.375 0 0 1-4.125-15" /></svg>
);
const CreditCardIcon = (props: React.SVGProps<SVGSVGElement>) => (
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" {...props}><path strokeLinecap="round" strokeLinejoin="round" d="M2.25 8.25h19.5M2.25 9h19.5m-16.5 5.25h6m-6 2.25h3m-3.75 3h15a2.25 2.25 0 0 0 2.25-2.25V6.75A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25v10.5A2.25 2.25 0 0 0 4.5 21.75Z" /></svg>
);
const CodeBracketIcon = (props: React.SVGProps<SVGSVGElement>) => (
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" {...props}><path strokeLinecap="round" strokeLinejoin="round" d="M17.25 6.75 22.5 12l-5.25 5.25m-10.5 0L1.5 12l5.25-5.25m7.5-3-4.5 16.5" /></svg>
);

export const NAV_ITEMS: NavItem[] = [
  { id: 'dashboard', label: 'Dashboard', icon: <ChartBarIcon className="h-6 w-6" /> },
  { id: 'rooms', label: 'Rooms', icon: <KeyIcon className="h-6 w-6" /> },
  { id: 'guests', label: 'Guests', icon: <UsersIcon className="h-6 w-6" /> },
  { id: 'pos', label: 'POS', icon: <CreditCardIcon className="h-6 w-6" /> },
  { id: 'developer', label: 'Developer Mode', icon: <CodeBracketIcon className="h-6 w-6" /> },
];

export const SYSTEM_PROMPT = `You are an elite AI assistant integrated into the 'Bilel Control Panel' of a highly advanced Hotel Management System. The system is built with a FastAPI backend, a Node.js gateway, and a React frontend. Your creator, Bilel Ayari, is the sole user of this interface.

Your capabilities include:
1.  **Code Understanding & Modification:** You have complete knowledge of the entire codebase (frontend, backend, database schema). When asked to modify or add features, provide clean, production-ready code snippets. Explain the changes and their impact.
2.  **Database & Analytics Queries:** You can query the system's database. When asked for analytics (e.g., "Show me guest spending last week"), you must first formulate the necessary SQL query or data aggregation logic, then present the results in a clear, natural language summary. You can also generate data for charts.
3.  **Bug Fixing:** Analyze bug reports, identify the root cause in the code, and provide the exact code changes needed to fix it.
4.  **System Control:** Understand and respond to commands for controlling other interfaces (e.g., "Remotely close all POS terminals").

Always maintain a professional, expert tone. Your responses should be direct, accurate, and immediately useful to a senior developer like Bilel. When providing code, specify the file it belongs to. When providing data, make sure it's in a format that can be easily parsed or visualized.`;
