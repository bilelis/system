
import React from 'react';
import { NAV_ITEMS } from '../constants';
import { Page } from '../types';

interface PlaceholderPageProps {
  title: string;
  icon: Page;
}

const PlaceholderPage: React.FC<PlaceholderPageProps> = ({ title, icon }) => {
  const navItem = NAV_ITEMS.find(item => item.id === icon);

  return (
    <div className="flex flex-col items-center justify-center h-full text-center text-gray-500">
      <div className="w-24 h-24 text-indigo-500">
        {navItem ? React.cloneElement(navItem.icon, { className: "w-24 h-24" }) : null}
      </div>
      <h1 className="mt-8 text-4xl font-bold text-gray-300">{title}</h1>
      <p className="mt-2 text-lg">This interface is under development.</p>
      <p className="mt-4 max-w-md">
        You can use the AI Assistant in Developer Mode to build out the UI and connect the backend endpoints for this section.
      </p>
    </div>
  );
};

export default PlaceholderPage;
