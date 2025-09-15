import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { useThemeContext } from '../../theme/ThemeProvider';
import { useAppDispatch, useAppSelector } from '../../store/hooks';
import { logout } from '../../store/slices/authSlice';

import {
  AppBar,
  Toolbar,
  Typography,
  IconButton,
  Menu,
  MenuItem,
  Box,
  Button,
  Avatar,
  Tooltip,
} from '@mui/material';

import {
  Menu as MenuIcon,
  Brightness4 as DarkModeIcon,
  Brightness7 as LightModeIcon,
  Translate as TranslateIcon,
  AccountCircle,
  Logout as LogoutIcon,
  Settings as SettingsIcon,
} from '@mui/icons-material';

interface NavbarProps {
  toggleSidebar: () => void;
}

const Navbar: React.FC<NavbarProps> = ({ toggleSidebar }) => {
  const { t, i18n } = useTranslation();
  const { mode, toggleColorMode } = useThemeContext();
  const navigate = useNavigate();
  const dispatch = useAppDispatch();
  const { user, isAuthenticated } = useAppSelector((state) => state.auth);

  // User menu state
  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);
  const [langAnchorEl, setLangAnchorEl] = useState<null | HTMLElement>(null);

  // Handle user menu open/close
  const handleMenuOpen = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorEl(event.currentTarget);
  };

  const handleMenuClose = () => {
    setAnchorEl(null);
  };

  // Handle language menu open/close
  const handleLangMenuOpen = (event: React.MouseEvent<HTMLElement>) => {
    setLangAnchorEl(event.currentTarget);
  };

  const handleLangMenuClose = () => {
    setLangAnchorEl(null);
  };

  // Change language
  const changeLanguage = (lng: string) => {
    i18n.changeLanguage(lng);
    localStorage.setItem('language', lng);
    handleLangMenuClose();
    // Force RTL/LTR based on language
    document.dir = lng === 'ar' ? 'rtl' : 'ltr';
  };

  // Handle logout
  const handleLogout = () => {
    dispatch(logout());
    navigate('/login');
    handleMenuClose();
  };

  // Handle profile navigation
  const handleProfile = () => {
    navigate('/profile');
    handleMenuClose();
  };

  // Handle settings navigation
  const handleSettings = () => {
    navigate('/settings');
    handleMenuClose();
  };

  return (
    <AppBar position="fixed" sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }}>
      <Toolbar>
        <IconButton
          color="inherit"
          aria-label="open drawer"
          edge="start"
          onClick={toggleSidebar}
          sx={{ mr: 2 }}
        >
          <MenuIcon />
        </IconButton>

        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          {t('app.title')}
        </Typography>

        {/* Theme toggle */}
        <Tooltip title={mode === 'dark' ? t('settings.lightMode') : t('settings.darkMode')}>
          <IconButton color="inherit" onClick={toggleColorMode} sx={{ ml: 1 }}>
            {mode === 'dark' ? <LightModeIcon /> : <DarkModeIcon />}
          </IconButton>
        </Tooltip>

        {/* Language selector */}
        <Tooltip title={t('settings.language')}>
          <IconButton
            color="inherit"
            onClick={handleLangMenuOpen}
            sx={{ ml: 1 }}
            aria-controls="language-menu"
            aria-haspopup="true"
          >
            <TranslateIcon />
          </IconButton>
        </Tooltip>
        <Menu
          id="language-menu"
          anchorEl={langAnchorEl}
          open={Boolean(langAnchorEl)}
          onClose={handleLangMenuClose}
          keepMounted
        >
          <MenuItem onClick={() => changeLanguage('en')} selected={i18n.language === 'en'}>
            English
          </MenuItem>
          <MenuItem onClick={() => changeLanguage('ar')} selected={i18n.language === 'ar'}>
            العربية
          </MenuItem>
        </Menu>

        {isAuthenticated ? (
          <>
            {/* User menu */}
            <Box sx={{ ml: 2 }}>
              <Tooltip title={user?.name || t('nav.profile')}>
                <IconButton
                  onClick={handleMenuOpen}
                  color="inherit"
                  aria-controls="user-menu"
                  aria-haspopup="true"
                >
                  <Avatar sx={{ width: 32, height: 32 }}>
                    {user?.name?.charAt(0) || 'U'}
                  </Avatar>
                </IconButton>
              </Tooltip>
              <Menu
                id="user-menu"
                anchorEl={anchorEl}
                open={Boolean(anchorEl)}
                onClose={handleMenuClose}
                keepMounted
              >
                <MenuItem onClick={handleProfile}>
                  <AccountCircle sx={{ mr: 1 }} />
                  {t('nav.profile')}
                </MenuItem>
                <MenuItem onClick={handleSettings}>
                  <SettingsIcon sx={{ mr: 1 }} />
                  {t('nav.settings')}
                </MenuItem>
                <MenuItem onClick={handleLogout}>
                  <LogoutIcon sx={{ mr: 1 }} />
                  {t('auth.logout')}
                </MenuItem>
              </Menu>
            </Box>
          </>
        ) : (
          <Button color="inherit" onClick={() => navigate('/login')}>
            {t('auth.login')}
          </Button>
        )}
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;