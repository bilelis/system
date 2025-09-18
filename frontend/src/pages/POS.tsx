import React, { useState } from 'react';
import {
  Box,
  Container,
  Typography,
  Card,
  CardContent,
  Button,
  List,
  ListItem,
  ListItemText,
  ListItemSecondaryAction,
  IconButton,
  Chip,
  Divider,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions
} from '@mui/material';
import {
  Add,
  Remove,
  ShoppingCart,
  Payment,
  Receipt
} from '@mui/icons-material';

interface MenuItem {
  id: string;
  name: string;
  price: number;
  category: string;
}

interface OrderItem {
  item: MenuItem;
  quantity: number;
}

const POS: React.FC = () => {
  const [selectedItems, setSelectedItems] = useState<OrderItem[]>([]);
  const [showPayment, setShowPayment] = useState(false);
  
  const menuItems: MenuItem[] = [
    { id: '1', name: 'Coca Cola', price: 3.00, category: 'Drinks' },
    { id: '2', name: 'Whisky', price: 15.00, category: 'Drinks' },
    { id: '3', name: 'Kaftaji', price: 8.00, category: 'Food' },
    { id: '4', name: 'Ojja', price: 10.00, category: 'Food' },
    { id: '5', name: 'Chapati Poulet', price: 7.00, category: 'Food' },
    { id: '6', name: 'Chapati Viande', price: 9.00, category: 'Food' }
  ];

  const addItem = (item: MenuItem) => {
    setSelectedItems(prev => {
      const existing = prev.find(orderItem => orderItem.item.id === item.id);
      if (existing) {
        return prev.map(orderItem => 
          orderItem.item.id === item.id 
            ? { ...orderItem, quantity: orderItem.quantity + 1 }
            : orderItem
        );
      }
      return [...prev, { item, quantity: 1 }];
    });
  };

  const removeItem = (itemId: string) => {
    setSelectedItems(prev => 
      prev.reduce((acc, orderItem) => {
        if (orderItem.item.id === itemId) {
          if (orderItem.quantity > 1) {
            acc.push({ ...orderItem, quantity: orderItem.quantity - 1 });
          }
        } else {
          acc.push(orderItem);
        }
        return acc;
      }, [] as OrderItem[])
    );
  };

  const getTotalAmount = () => {
    return selectedItems.reduce((total, orderItem) => 
      total + (orderItem.item.price * orderItem.quantity), 0
    );
  };

  const processPayment = () => {
    alert('Payment processed successfully!');
    setSelectedItems([]);
    setShowPayment(false);
  };

  return (
    <Container maxWidth="xl" sx={{ mt: 2 }}>
      <Typography variant="h4" gutterBottom>
        Point of Sale System
      </Typography>
      
      <Box sx={{ display: 'flex', gap: 3, height: 'calc(100vh - 150px)' }}>
        {/* Menu Items */}
        <Card sx={{ flex: 2, overflow: 'auto' }}>
          <CardContent>
            <Typography variant="h6" gutterBottom>Menu Items</Typography>
            <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 2 }}>
              {menuItems.map(item => (
                <Card 
                  key={item.id} 
                  sx={{ 
                    minWidth: 200, 
                    cursor: 'pointer',
                    '&:hover': { bgcolor: 'action.hover' }
                  }}
                  onClick={() => addItem(item)}
                >
                  <CardContent>
                    <Typography variant="h6">{item.name}</Typography>
                    <Typography variant="body2" color="text.secondary">
                      {item.category}
                    </Typography>
                    <Typography variant="h6" color="primary">
                      €{item.price.toFixed(2)}
                    </Typography>
                  </CardContent>
                </Card>
              ))}
            </Box>
          </CardContent>
        </Card>

        {/* Order Summary */}
        <Card sx={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
          <CardContent sx={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
            <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
              <ShoppingCart sx={{ mr: 1 }} />
              <Typography variant="h6">Current Order</Typography>
            </Box>
            
            <List sx={{ flex: 1, overflow: 'auto' }}>
              {selectedItems.map((orderItem, index) => (
                <React.Fragment key={`${orderItem.item.id}-${index}`}>
                  <ListItem>
                    <ListItemText
                      primary={orderItem.item.name}
                      secondary={`€${orderItem.item.price.toFixed(2)} x ${orderItem.quantity}`}
                    />
                    <ListItemSecondaryAction>
                      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                        <IconButton 
                          size="small" 
                          onClick={() => removeItem(orderItem.item.id)}
                        >
                          <Remove />
                        </IconButton>
                        <Chip label={orderItem.quantity} size="small" />
                        <IconButton 
                          size="small" 
                          onClick={() => addItem(orderItem.item)}
                        >
                          <Add />
                        </IconButton>
                      </Box>
                    </ListItemSecondaryAction>
                  </ListItem>
                  <Divider />
                </React.Fragment>
              ))}
            </List>
            
            {selectedItems.length > 0 && (
              <Box sx={{ mt: 2 }}>
                <Typography variant="h5" sx={{ mb: 2 }}>
                  Total: €{getTotalAmount().toFixed(2)}
                </Typography>
                <Button 
                  fullWidth 
                  variant="contained" 
                  size="large"
                  startIcon={<Payment />}
                  onClick={() => setShowPayment(true)}
                >
                  Process Payment
                </Button>
              </Box>
            )}
          </CardContent>
        </Card>
      </Box>

      {/* Payment Dialog */}
      <Dialog open={showPayment} onClose={() => setShowPayment(false)}>
        <DialogTitle>
          <Box sx={{ display: 'flex', alignItems: 'center' }}>
            <Receipt sx={{ mr: 1 }} />
            Process Payment
          </Box>
        </DialogTitle>
        <DialogContent>
          <Typography variant="h6" sx={{ mb: 2 }}>
            Total Amount: €{getTotalAmount().toFixed(2)}
          </Typography>
          <List>
            {selectedItems.map((orderItem, index) => (
              <ListItem key={index}>
                <ListItemText
                  primary={`${orderItem.item.name} x ${orderItem.quantity}`}
                  secondary={`€${(orderItem.item.price * orderItem.quantity).toFixed(2)}`}
                />
              </ListItem>
            ))}
          </List>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setShowPayment(false)}>Cancel</Button>
          <Button variant="contained" onClick={processPayment}>
            Confirm Payment
          </Button>
        </DialogActions>
      </Dialog>
    </Container>
  );
};

export default POS;
