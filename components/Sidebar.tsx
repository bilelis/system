
import React from 'react';
import { Page, NavItem } from '../types';
import { NAV_ITEMS } from '../constants';

interface SidebarProps {
  activePage: Page;
  setActivePage: (page: Page) => void;
  onLogout: () => void;
}

const Sidebar: React.FC<SidebarProps> = ({ activePage, setActivePage, onLogout }) => {
  return (
    <aside className="w-20 md:w-64 bg-gray-950 flex flex-col border-r border-gray-700/50">
      <div className="flex items-center justify-center md:justify-start md:px-6 h-20 border-b border-gray-700/50">
        <div className="w-10 h-10 bg-indigo-600 rounded-full flex items-center justify-center font-black text-xl">
          B
        </div>
        <h1 className="hidden md:block ml-3 text-xl font-bold text-white">Bilel Control Panel</h1>
      </div>
      <nav className="flex-1 px-2 md:px-4 py-4 space-y-2">
        {NAV_ITEMS.map((item: NavItem) => (
          <a
            key={item.id}
            href="#"
            onClick={(e) => {
              e.preventDefault();
              setActivePage(item.id);
            }}
            className={`flex items-center p-3 rounded-lg transition-colors duration-200 ${
              activePage === item.id
                ? 'bg-indigo-600 text-white'
                : 'text-gray-400 hover:bg-gray-800 hover:text-white'
            }`}
          >
            {item.icon}
            <span className="hidden md:block ml-4 font-medium">{item.label}</span>
          </a>
        ))}
      </nav>
      <div className="px-2 md:px-4 py-4 border-t border-gray-700/50">
        <button
          onClick={onLogout}
          className="flex items-center p-3 w-full rounded-lg text-gray-400 hover:bg-gray-800 hover:text-white transition-colors duration-200"
        >
          <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
            <path strokeLinecap="round" strokeLinejoin="round" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
          </svg>
          <span className="hidden md:block ml-4 font-medium">Logout</span>
        </button>
      </div>
    </aside>
  );
};

export default Sidebar;
