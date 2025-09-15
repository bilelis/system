import React, { useEffect, useState } from 'react';
import { useTranslation } from 'react-i18next';
import { Grid, Typography, Paper, Box, CircularProgress } from '@mui/material';
import api from '../services/api';

// Types for analytics data
interface AnalyticsData {
  revenue_today: number;
  occupancy_rate: number;
  pending_check_ins: number;
  pending_check_outs: number;
  popular_items: Array<{ name: string; count: number }>;
  aiInsight: string;
}

const Dashboard: React.FC = () => {
  const { t } = useTranslation();
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [data, setData] = useState<AnalyticsData | null>(null);

  // Fetch dashboard data
  useEffect(() => {
    const fetchDashboardData = async () => {
      try {
        setLoading(true);
        const response = await api.get('/analytics/dashboard');
        setData(response.data);
        setError(null);
      } catch (err: any) {
        setError(err.response?.data?.message || 'Failed to load dashboard data');
      } finally {
        setLoading(false);
      }
    };

    fetchDashboardData();
  }, []);

  // Analytics card component
  const AnalyticsCard = ({ title, value, unit = '' }: { title: string; value: any; unit?: string }) => (
    <Paper
      elevation={2}
      sx={{
        p: 3,
        height: '100%',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        textAlign: 'center',
        borderRadius: 2,
      }}
    >
      <Typography variant="h6" color="text.secondary" gutterBottom>
        {title}
      </Typography>
      <Typography variant="h4" component="div">
        {value}
        {unit && (
          <Typography variant="subtitle1" component="span">
            {unit}
          </Typography>
        )}
      </Typography>
    </Paper>
  );

  // AI Insight card
  const AiInsightCard = ({ insight }: { insight: string }) => (
    <Paper
      elevation={2}
      sx={{
        p: 3,
        height: '100%',
        display: 'flex',
        flexDirection: 'column',
        borderRadius: 2,
      }}
    >
      <Typography variant="h6" color="text.secondary" gutterBottom>
        {t('analytics.aiInsights')}
      </Typography>
      <Typography variant="body1" component="div" sx={{ mt: 2 }}>
        {insight}
      </Typography>
    </Paper>
  );

  // Popular items card
  const PopularItemsCard = ({ items }: { items: Array<{ name: string; count: number }> }) => (
    <Paper
      elevation={2}
      sx={{
        p: 3,
        height: '100%',
        display: 'flex',
        flexDirection: 'column',
        borderRadius: 2,
      }}
    >
      <Typography variant="h6" color="text.secondary" gutterBottom>
        {t('dashboard.popularItems')}
      </Typography>
      <Box sx={{ mt: 2 }}>
        {items.map((item, index) => (
          <Box
            key={index}
            sx={{
              display: 'flex',
              justifyContent: 'space-between',
              mb: 1,
              pb: 1,
              borderBottom: index < items.length - 1 ? '1px solid #eee' : 'none',
            }}
          >
            <Typography variant="body1">{item.name}</Typography>
            <Typography variant="body1" fontWeight="bold">
              {item.count}
            </Typography>
          </Box>
        ))}
      </Box>
    </Paper>
  );

  // Loading state
  if (loading) {
    return (
      <Box
        sx={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          height: '50vh',
        }}
      >
        <CircularProgress />
      </Box>
    );
  }

  // Error state
  if (error) {
    return (
      <Box
        sx={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          height: '50vh',
        }}
      >
        <Typography color="error">{error}</Typography>
      </Box>
    );
  }

  // Mock data for development (remove in production)
  const mockData: AnalyticsData = data || {
    revenue_today: 12580,
    occupancy_rate: 78,
    pending_check_ins: 5,
    pending_check_outs: 3,
    popular_items: [
      { name: 'Deluxe Room', count: 12 },
      { name: 'Breakfast Buffet', count: 8 },
      { name: 'Spa Package', count: 6 },
      { name: 'Airport Transfer', count: 4 },
      { name: 'Executive Suite', count: 3 },
    ],
    aiInsight:
      'Revenue is up 15% compared to last week. Occupancy rate is stable at 78%. Consider promoting the Executive Suite which has lower bookings than other room types.',
  };

  return (
    <Box sx={{ flexGrow: 1 }}>
      <Typography variant="h4" gutterBottom>
        {t('dashboard.welcome')}
      </Typography>

      <Grid container spacing={3} sx={{ mb: 4 }}>
        {/* Revenue Today */}
        <Grid item xs={12} sm={6} md={3}>
          <AnalyticsCard
            title={t('dashboard.revenueToday')}
            value={new Intl.NumberFormat('en-US', {
              style: 'currency',
              currency: 'USD',
              minimumFractionDigits: 0,
            }).format(mockData.revenue_today)}
          />
        </Grid>

        {/* Occupancy Rate */}
        <Grid item xs={12} sm={6} md={3}>
          <AnalyticsCard title={t('dashboard.occupancyRate')} value={mockData.occupancy_rate} unit="%" />
        </Grid>

        {/* Pending Check-ins */}
        <Grid item xs={12} sm={6} md={3}>
          <AnalyticsCard title={t('dashboard.pendingCheckIns')} value={mockData.pending_check_ins} />
        </Grid>

        {/* Pending Check-outs */}
        <Grid item xs={12} sm={6} md={3}>
          <AnalyticsCard title={t('dashboard.pendingCheckOuts')} value={mockData.pending_check_outs} />
        </Grid>
      </Grid>

      <Grid container spacing={3}>
        {/* AI Insights */}
        <Grid item xs={12} md={8}>
          <AiInsightCard insight={mockData.aiInsight} />
        </Grid>

        {/* Popular Items */}
        <Grid item xs={12} md={4}>
          <PopularItemsCard items={mockData.popular_items} />
        </Grid>
      </Grid>
    </Box>
  );
};

export default Dashboard;