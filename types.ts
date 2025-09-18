
export type Page = 'dashboard' | 'rooms' | 'guests' | 'pos' | 'developer';

export interface NavItem {
  id: Page;
  label: string;
  icon: JSX.Element;
}

export interface ChatMessage {
  role: 'user' | 'model';
  text: string;
}

export interface KpiData {
    title: string;
    value: string;
    change: string;
    changeType: 'increase' | 'decrease';
    icon: JSX.Element;
}
