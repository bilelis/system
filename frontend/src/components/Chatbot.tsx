import React, { useState, useRef, useEffect } from 'react';
import {
  Box,
  Typography,
  TextField,
  IconButton,
  Paper,
  List,
  ListItem,
  CircularProgress,
  Chip
} from '@mui/material';
import { Send, SmartToy } from '@mui/icons-material';

interface ChatMessage {
  role: 'user' | 'assistant';
  text: string;
  timestamp: Date;
}

const Chatbot: React.FC = () => {
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      role: 'assistant',
      text: 'Welcome, Bilel. I am your AI assistant for the Hotel Management System. I can help you with:\n\n• System analytics and insights\n• Code modifications and deployments\n• Database queries and reports\n• Feature additions and bug fixes\n\nHow can I assist you today?',
      timestamp: new Date()
    }
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = async () => {
    if (!input.trim() || isLoading) return;

    const userMessage: ChatMessage = {
      role: 'user',
      text: input.trim(),
      timestamp: new Date()
    };

    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);

    try {
      // Simulate AI response for now
      await new Promise(resolve => setTimeout(resolve, 1000 + Math.random() * 2000));
      
      const responses = [
        'I understand your request. Let me analyze the hotel management system for you.',
        'Based on the current data, I can provide insights on occupancy rates and revenue trends.',
        'I can help you implement that feature. Would you like me to generate the code changes?',
        'System status is optimal. All modules are functioning correctly.',
        'I recommend reviewing the analytics dashboard for detailed performance metrics.',
        'That is an excellent suggestion! I can modify the system to include that functionality.'
      ];
      
      const aiMessage: ChatMessage = {
        role: 'assistant',
        text: responses[Math.floor(Math.random() * responses.length)],
        timestamp: new Date()
      };
      
      setMessages(prev => [...prev, aiMessage]);
    } catch (error) {
      const errorMessage: ChatMessage = {
        role: 'assistant',
        text: 'I apologize, but I encountered an error. Please try again.',
        timestamp: new Date()
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  return (
    <Paper 
      elevation={3} 
      sx={{ 
        height: 600, 
        display: 'flex', 
        flexDirection: 'column',
        bgcolor: 'background.paper'
      }}
    >
      {/* Header */}
      <Box 
        sx={{ 
          p: 2, 
          borderBottom: 1, 
          borderColor: 'divider',
          bgcolor: 'primary.main',
          color: 'primary.contrastText'
        }}
      >
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
          <SmartToy />
          <Typography variant="h6">AI Assistant</Typography>
          <Chip 
            label="Online" 
            size="small" 
            sx={{ 
              ml: 'auto',
              bgcolor: 'success.main',
              color: 'white'
            }} 
          />
        </Box>
        <Typography variant="caption" sx={{ opacity: 0.8 }}>
          Hotel Management System AI Helper
        </Typography>
      </Box>

      {/* Messages */}
      <Box sx={{ flex: 1, overflow: 'auto', p: 1 }}>
        <List>
          {messages.map((message, index) => (
            <ListItem 
              key={index} 
              sx={{ 
                display: 'flex',
                justifyContent: message.role === 'user' ? 'flex-end' : 'flex-start',
                py: 1
              }}
            >
              <Paper 
                elevation={1}
                sx={{
                  p: 2,
                  maxWidth: '80%',
                  bgcolor: message.role === 'user' 
                    ? 'primary.main' 
                    : 'grey.100',
                  color: message.role === 'user' 
                    ? 'primary.contrastText' 
                    : 'text.primary'
                }}
              >
                <Typography variant="body2" sx={{ whiteSpace: 'pre-wrap' }}>
                  {message.text}
                </Typography>
                <Typography 
                  variant="caption" 
                  sx={{ 
                    display: 'block',
                    mt: 1,
                    opacity: 0.7,
                    fontSize: '0.75rem'
                  }}
                >
                  {message.timestamp.toLocaleTimeString()}
                </Typography>
              </Paper>
            </ListItem>
          ))}
          
          {isLoading && (
            <ListItem sx={{ display: 'flex', justifyContent: 'flex-start', py: 1 }}>
              <Paper elevation={1} sx={{ p: 2, bgcolor: 'grey.100' }}>
                <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                  <CircularProgress size={16} />
                  <Typography variant="body2">AI is thinking...</Typography>
                </Box>
              </Paper>
            </ListItem>
          )}
        </List>
        <div ref={messagesEndRef} />
      </Box>

      {/* Input */}
      <Box 
        sx={{ 
          p: 2, 
          borderTop: 1, 
          borderColor: 'divider',
          bgcolor: 'background.default'
        }}
      >
        <Box sx={{ display: 'flex', gap: 1 }}>
          <TextField
            fullWidth
            multiline
            maxRows={3}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Ask me to analyze data, modify features, or help with system management..."
            disabled={isLoading}
            size="small"
          />
          <IconButton 
            onClick={handleSendMessage}
            disabled={isLoading || !input.trim()}
            color="primary"
            sx={{ alignSelf: 'flex-end' }}
          >
            <Send />
          </IconButton>
        </Box>
      </Box>
    </Paper>
  );
};

export default Chatbot;