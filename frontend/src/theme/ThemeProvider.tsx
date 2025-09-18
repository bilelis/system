import React, { createContext, useState, useMemo, useContext, ReactNode } from 'react';
import { ThemeProvider as MuiThemeProvider } from '@mui/material';
import CssBaseline from '@mui/material/CssBaseline';
import { createAppTheme } from './theme';

// Use string literal type instead of PaletteMode
type PaletteMode = 'light' | 'dark';

// Create theme context
interface ThemeContextType {
  mode: PaletteMode;
  toggleColorMode: () => void;
}

const ThemeContext = createContext<ThemeContextType>({
  mode: 'light',
  toggleColorMode: () => {},
});

// Custom hook to use the theme context
export const useThemeContext = () => useContext(ThemeContext);

interface ThemeProviderProps {
  children: ReactNode;
}

// Theme provider component
export const ThemeProvider: React.FC<ThemeProviderProps> = ({ children }) => {
  // Get the preferred color scheme from local storage or default to 'light'
  const storedMode = localStorage.getItem('themeMode') as PaletteMode | null;
  const [mode, setMode] = useState<PaletteMode>(storedMode || 'light');

  // Toggle between light and dark modes
  const toggleColorMode = () => {
    const newMode = mode === 'light' ? 'dark' : 'light';
    setMode(newMode);
    localStorage.setItem('themeMode', newMode);
  };

  // Create the theme based on the current mode
  const theme = useMemo(() => createAppTheme(mode), [mode]);

  // Context value
  const contextValue = useMemo(
    () => ({
      mode,
      toggleColorMode,
    }),
    [mode]
  );

  return (
    <ThemeContext.Provider value={contextValue}>
      <MuiThemeProvider theme={theme}>
        <CssBaseline /> {/* Normalize CSS */}
        {children}
      </MuiThemeProvider>
    </ThemeContext.Provider>
  );
};