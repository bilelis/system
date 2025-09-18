import React from 'react';
import { Box, Typography, Button } from '@mui/material';

const Debug: React.FC = () => {
  console.log('Debug component rendering...');
  
  return (
    <Box 
      sx={{ 
        p: 4, 
        textAlign: 'center',
        backgroundColor: 'background.paper',
        minHeight: '100vh',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center'
      }}
    >
      <Typography variant="h3" gutterBottom color="primary">
        🎉 Frontend is Working!
      </Typography>
      <Typography variant="h5" gutterBottom>
        Hotel Management System
      </Typography>
      <Typography variant="body1" sx={{ mb: 3 }}>
        by Bilel Ayari
      </Typography>
      
      <Box sx={{ mt: 2 }}>
        <Button 
          variant="contained" 
          color="primary" 
          onClick={() => window.location.href = '/login'}
          sx={{ mr: 2 }}
        >
          Go to Login
        </Button>
        <Button 
          variant="outlined" 
          color="secondary"
          onClick={() => window.location.href = '/dashboard'}
        >
          Go to Dashboard
        </Button>
      </Box>
      
      <Box sx={{ mt: 4, p: 2, backgroundColor: 'grey.100', borderRadius: 1 }}>
        <Typography variant="h6">System Status:</Typography>
        <Typography>✅ React: Working</Typography>
        <Typography>✅ Material-UI: Working</Typography>
        <Typography>✅ TypeScript: Working</Typography>
        <Typography>✅ Vite: Working</Typography>
      </Box>
    </Box>
  );
};

export default Debug;