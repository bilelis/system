import React, { useState } from 'react';
import {
  Box,
  Container,
  Typography,
  TextField,
  Button,
  Card,
  CardContent,
  Tabs,
  Tab,
  Paper,
  List,
  ListItem,
  ListItemText,
  ListItemIcon,
  Switch,
  FormControlLabel,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Alert,
  Chip,
  LinearProgress
} from '@mui/material';
import {
  Dashboard,
  Security,
  Code,
  Analytics,
  Settings,
  People,
  Room,
  Restaurant,
  Assessment,
  Lock,
  CheckCircle,
  Chat
} from '@mui/icons-material';
import { styled } from '@mui/material/styles';
import Chatbot from '../components/Chatbot';

const StyledCard = styled(Card)(({ theme }) => ({
  background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
  color: 'white',
  '& .MuiCardContent-root': {
    color: 'white'
  }
}));

const BilelControlPanel: React.FC = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [accessCode, setAccessCode] = useState('');
  const [activeTab, setActiveTab] = useState(0);
  const [systemStats] = useState({
    totalGuests: 42,
    occupancyRate: 78,
    dailyRevenue: 15240,
    activeOrders: 23,
    systemHealth: 'Excellent'
  });
  const [devMode, setDevMode] = useState(false);
  const [showCodeEditor, setShowCodeEditor] = useState(false);

  const handleLogin = () => {
    if (accessCode === '1234') {
      setIsAuthenticated(true);
      setAccessCode('');
    } else {
      alert('Invalid access code! Contact Bilel Ayari for access.');
    }
  };

  const handleTabChange = (event: React.SyntheticEvent, newValue: number) => {
    setActiveTab(newValue);
  };

  const TabPanel = ({ children, value, index }: { children: React.ReactNode; value: number; index: number }) => (
    <div hidden={value !== index}>
      {value === index && <Box sx={{ p: 3 }}>{children}</Box>}
    </div>
  );

  if (!isAuthenticated) {
    return (
      <Container maxWidth="sm" sx={{ mt: 8 }}>
        <StyledCard>
          <CardContent sx={{ textAlign: 'center', p: 4 }}>
            <Lock sx={{ fontSize: 60, mb: 2 }} />
            <Typography variant="h4" gutterBottom>
              Bilel Control Panel
            </Typography>
            <Typography variant="body1" sx={{ mb: 3, opacity: 0.9 }}>
              Restricted Access - Enter 4-digit code
            </Typography>
            <TextField
              type="password"
              inputProps={{ maxLength: 4, style: { textAlign: 'center', fontSize: '24px' } }}
              value={accessCode}
              onChange={(e) => setAccessCode(e.target.value)}
              placeholder="• • • •"
              sx={{
                mb: 3,
                '& .MuiOutlinedInput-root': {
                  backgroundColor: 'rgba(255,255,255,0.1)',
                  '& fieldset': { borderColor: 'rgba(255,255,255,0.3)' },
                  '&:hover fieldset': { borderColor: 'rgba(255,255,255,0.5)' },
                  '&.Mui-focused fieldset': { borderColor: 'white' }
                },
                '& .MuiInputBase-input': { color: 'white' }
              }}
            />
            <br />
            <Button
              variant="contained"
              onClick={handleLogin}
              sx={{
                backgroundColor: 'rgba(255,255,255,0.2)',
                '&:hover': { backgroundColor: 'rgba(255,255,255,0.3)' }
              }}
            >
              Access Control Panel
            </Button>
          </CardContent>
        </StyledCard>
      </Container>
    );
  }

  return (
    <Container maxWidth="xl" sx={{ mt: 2 }}>
      <Box sx={{ mb: 3 }}>
        <Typography variant="h3" gutterBottom>
          Welcome, Bilel Ayari
        </Typography>
        <Typography variant="subtitle1" color="text.secondary">
          Hotel Management System - Master Control Panel
        </Typography>
      </Box>

      <Box sx={{ borderBottom: 1, borderColor: 'divider', mb: 3 }}>
        <Tabs value={activeTab} onChange={handleTabChange}>
          <Tab icon={<Dashboard />} label="System Overview" />
          <Tab icon={<Analytics />} label="Analytics" />
          <Tab icon={<Settings />} label="System Control" />
          <Tab icon={<Code />} label="Developer Mode" />
          <Tab icon={<Chat />} label="AI Assistant" />
          <Tab icon={<Security />} label="Security" />
        </Tabs>
      </Box>

      <TabPanel value={activeTab} index={0}>
        <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 3, mb: 3 }}>
          <Card sx={{ minWidth: 200, flex: 1 }}>
            <CardContent>
              <Typography variant="h6">Total Guests</Typography>
              <Typography variant="h4" color="primary">{systemStats.totalGuests}</Typography>
            </CardContent>
          </Card>
          <Card sx={{ minWidth: 200, flex: 1 }}>
            <CardContent>
              <Typography variant="h6">Occupancy Rate</Typography>
              <Typography variant="h4" color="success.main">{systemStats.occupancyRate}%</Typography>
              <LinearProgress variant="determinate" value={systemStats.occupancyRate} sx={{ mt: 1 }} />
            </CardContent>
          </Card>
          <Card sx={{ minWidth: 200, flex: 1 }}>
            <CardContent>
              <Typography variant="h6">Daily Revenue</Typography>
              <Typography variant="h4" color="warning.main">€{systemStats.dailyRevenue.toLocaleString()}</Typography>
            </CardContent>
          </Card>
          <Card sx={{ minWidth: 200, flex: 1 }}>
            <CardContent>
              <Typography variant="h6">Active Orders</Typography>
              <Typography variant="h4" color="info.main">{systemStats.activeOrders}</Typography>
            </CardContent>
          </Card>
        </Box>
        
        <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 3 }}>
          <Card sx={{ minWidth: 300, flex: 1 }}>
            <CardContent>
              <Typography variant="h6" gutterBottom>System Health</Typography>
              <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
                <CheckCircle color="success" />
                <Chip label={systemStats.systemHealth} color="success" />
              </Box>
              <List>
                <ListItem>
                  <ListItemIcon><CheckCircle color="success" /></ListItemIcon>
                  <ListItemText primary="Backend API" secondary="Operational" />
                </ListItem>
                <ListItem>
                  <ListItemIcon><CheckCircle color="success" /></ListItemIcon>
                  <ListItemText primary="Database" secondary="Connected" />
                </ListItem>
                <ListItem>
                  <ListItemIcon><CheckCircle color="success" /></ListItemIcon>
                  <ListItemText primary="Frontend" secondary="Responsive" />
                </ListItem>
              </List>
            </CardContent>
          </Card>
          
          <Card sx={{ minWidth: 300, flex: 1 }}>
            <CardContent>
              <Typography variant="h6" gutterBottom>Quick Actions</Typography>
              <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 2 }}>
                <Button variant="outlined" startIcon={<People />} sx={{ flex: '1 1 45%' }}>
                  Manage Users
                </Button>
                <Button variant="outlined" startIcon={<Room />} sx={{ flex: '1 1 45%' }}>
                  Room Status
                </Button>
                <Button variant="outlined" startIcon={<Restaurant />} sx={{ flex: '1 1 45%' }}>
                  POS Control
                </Button>
                <Button variant="outlined" startIcon={<Assessment />} sx={{ flex: '1 1 45%' }}>
                  Generate Report
                </Button>
              </Box>
            </CardContent>
          </Card>
        </Box>
      </TabPanel>

      <TabPanel value={activeTab} index={1}>
        <Typography variant="h5" gutterBottom>Advanced Analytics</Typography>
        <Alert severity="info" sx={{ mb: 3 }}>
          AI-powered analytics and insights will be displayed here
        </Alert>
        <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 3 }}>
          <Card sx={{ minWidth: 300, flex: 1 }}>
            <CardContent>
              <Typography variant="h6">Revenue Analytics</Typography>
              <Typography variant="body2">AI insights on revenue patterns</Typography>
            </CardContent>
          </Card>
          <Card sx={{ minWidth: 300, flex: 1 }}>
            <CardContent>
              <Typography variant="h6">Occupancy Predictions</Typography>
              <Typography variant="body2">ML-based occupancy forecasts</Typography>
            </CardContent>
          </Card>
        </Box>
      </TabPanel>

      <TabPanel value={activeTab} index={2}>
        <Typography variant="h5" gutterBottom>System Control</Typography>
        <Card sx={{ maxWidth: 600 }}>
          <CardContent>
            <Typography variant="h6" gutterBottom>Remote Controls</Typography>
            <List>
              <ListItem>
                <ListItemText primary="Reception Interface" secondary="Enable/Disable reception access" />
                <Switch defaultChecked />
              </ListItem>
              <ListItem>
                <ListItemText primary="POS System" secondary="Control POS terminals" />
                <Switch defaultChecked />
              </ListItem>
              <ListItem>
                <ListItemText primary="Billing Module" secondary="Billing system status" />
                <Switch defaultChecked />
              </ListItem>
            </List>
          </CardContent>
        </Card>
      </TabPanel>

      <TabPanel value={activeTab} index={3}>
        <Typography variant="h5" gutterBottom>Developer Mode</Typography>
        <FormControlLabel
          control={<Switch checked={devMode} onChange={(e) => setDevMode(e.target.checked)} />}
          label="Enable Developer Mode"
        />
        {devMode && (
          <Box sx={{ mt: 2 }}>
            <Alert severity="warning" sx={{ mb: 2 }}>
              Developer Mode Active - You have full system access
            </Alert>
            <Button
              variant="contained"
              startIcon={<Code />}
              onClick={() => setShowCodeEditor(true)}
              sx={{ mr: 2 }}
            >
              Open Code Editor
            </Button>
            <Button variant="outlined" color="warning">
              Deploy Changes
            </Button>
          </Box>
        )}
      </TabPanel>

      <TabPanel value={activeTab} index={4}>
        <Typography variant="h5" gutterBottom>AI Assistant</Typography>
        <Alert severity="info" sx={{ mb: 3 }}>
          Your personal AI assistant with full system access. Ask questions, request code changes, or get analytics insights.
        </Alert>
        <Chatbot />
      </TabPanel>

      <TabPanel value={activeTab} index={5}>
        <Typography variant="h5" gutterBottom>Security & Logs</Typography>
        <Card sx={{ maxWidth: 600 }}>
          <CardContent>
            <Typography variant="h6" gutterBottom>Recent Activity</Typography>
            <List>
              <ListItem>
                <ListItemText 
                  primary="Bilel Ayari logged into control panel" 
                  secondary="Just now" 
                />
              </ListItem>
              <ListItem>
                <ListItemText 
                  primary="System backup completed" 
                  secondary="2 hours ago" 
                />
              </ListItem>
              <ListItem>
                <ListItemText 
                  primary="New guest checked in" 
                  secondary="3 hours ago" 
                />
              </ListItem>
            </List>
          </CardContent>
        </Card>
      </TabPanel>

      <Dialog open={showCodeEditor} onClose={() => setShowCodeEditor(false)} maxWidth="lg" fullWidth>
        <DialogTitle>Code Editor - Developer Mode</DialogTitle>
        <DialogContent>
          <Typography variant="body2" color="text.secondary" gutterBottom>
            Full code editing capabilities - Make changes to any part of the system
          </Typography>
          <Paper sx={{ p: 2, bgcolor: '#1e1e1e', color: 'white', fontFamily: 'monospace' }}>
            <Typography variant="body2">
              // Hotel Management System - Live Code Editor<br />
              // You can edit any component, API endpoint, or database schema<br />
              <br />
              const systemStatus = 'Operational';<br />
              const bilel = 'FullAccess';<br />
              <br />
              // Example: Modify room rates<br />
              rooms.updateRates(newRates);<br />
              <br />
              // Example: Add new feature<br />
              features.add('AIRecommendations');
            </Typography>
          </Paper>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setShowCodeEditor(false)}>Cancel</Button>
          <Button variant="contained" color="primary">Save & Deploy</Button>
        </DialogActions>
      </Dialog>
    </Container>
  );
};

export default BilelControlPanel;