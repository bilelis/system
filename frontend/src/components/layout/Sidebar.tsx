import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { useAppSelector } from '../../store/hooks';

import {
  Drawer,
  List,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Divider,
  Box,
  Toolbar,
} from '@mui/material';

import {
  Dashboard as DashboardIcon,
  Hotel as ReceptionIcon,
  ShoppingCart as POSIcon,
  EventNote as BookingIcon,
  BarChart as AnalyticsIcon,
  Person as ProfileIcon,
  Settings as SettingsIcon,
} from '@mui/icons-material';

interface SidebarProps {
  open: boolean;
  drawerWidth: number;
  onClose: () => void;
  variant: 'permanent' | 'persistent' | 'temporary';
}

interface NavItem {
  path: string;
  label: string;
  icon: React.ReactNode;
  roles?: string[];
}

const Sidebar: React.FC<SidebarProps> = ({ open, drawerWidth, onClose, variant }) => {
  const { t } = useTranslation();
  const navigate = useNavigate();
  const location = useLocation();
  const { user } = useAppSelector((state) => state.auth);

  // Navigation items with role-based access control
  const navItems: NavItem[] = [
    {
      path: '/dashboard',
      label: t('nav.dashboard'),
      icon: <DashboardIcon />,
      roles: ['admin', 'manager', 'receptionist', 'staff'],
    },
    {
      path: '/reception',
      label: t('nav.reception'),
      icon: <ReceptionIcon />,
      roles: ['admin', 'manager', 'receptionist'],
    },
    {
      path: '/pos',
      label: t('nav.pos'),
      icon: <POSIcon />,
      roles: ['admin', 'manager', 'staff'],
    },
    {
      path: '/booking',
      label: t('nav.booking'),
      icon: <BookingIcon />,
      roles: ['admin', 'manager', 'receptionist'],
    },
    {
      path: '/analytics',
      label: t('nav.analytics'),
      icon: <AnalyticsIcon />,
      roles: ['admin', 'manager'],
    },
      {
        path: '/billing',
        label: 'Billing',
        icon: <POSIcon />, // You may want to use a different icon
        roles: ['admin', 'manager', 'receptionist'],
      },
  ];

  // User-specific items
  const userItems: NavItem[] = [
    {
      path: '/profile',
      label: t('nav.profile'),
      icon: <ProfileIcon />,
    },
    {
      path: '/settings',
      label: t('nav.settings'),
      icon: <SettingsIcon />,
    },
  ];

  // Handle navigation
  const handleNavigation = (path: string) => {
    navigate(path);
    if (variant === 'temporary') {
      onClose();
    }
  };

  // Filter items based on user role
  const filteredNavItems = navItems.filter(
    (item) => !item.roles || (user && item.roles.includes(user.role))
  );

  const drawerContent = (
    <>
      <Toolbar /> {/* Spacer for AppBar */}
      <Box sx={{ overflow: 'auto' }}>
        <List>
          {filteredNavItems.map((item) => (
            <ListItem key={item.path} disablePadding>
              <ListItemButton
                selected={location.pathname === item.path}
                onClick={() => handleNavigation(item.path)}
              >
                <ListItemIcon>{item.icon}</ListItemIcon>
                <ListItemText primary={item.label} />
              </ListItemButton>
            </ListItem>
          ))}
        </List>
        <Divider />
        <List>
          {userItems.map((item) => (
            <ListItem key={item.path} disablePadding>
              <ListItemButton
                selected={location.pathname === item.path}
                onClick={() => handleNavigation(item.path)}
              >
                <ListItemIcon>{item.icon}</ListItemIcon>
                <ListItemText primary={item.label} />
              </ListItemButton>
            </ListItem>
          ))}
        </List>
      </Box>
    </>
  );

  return (
    <Drawer
      variant={variant}
      open={open}
      onClose={onClose}
      sx={{
        width: drawerWidth,
        flexShrink: 0,
        '& .MuiDrawer-paper': {
          width: drawerWidth,
          boxSizing: 'border-box',
        },
      }}
    >
      {drawerContent}
    </Drawer>
  );
};

export default Sidebar;