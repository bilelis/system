from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.core.config import settings

class AnalyticsService:
    def __init__(self):
        pass
    
    def get_revenue_today(self, db: Session):
        query = text("""
            SELECT COALESCE(SUM(total_amount), 0) as revenue
            FROM orders
            WHERE DATE(created_at) = CURRENT_DATE
        """)
        result = db.execute(query).first()
        return float(result.revenue) if result else 0.0
    
    def get_occupancy_rate(self, db: Session):
        query = text("""
            SELECT 
                COALESCE(COUNT(CASE WHEN status = 'occupied' THEN 1 END)::float / NULLIF(COUNT(*)::float, 0) * 100, 0) as occupancy_rate
            FROM rooms
        """)
        result = db.execute(query).first()
        return float(result.occupancy_rate) if result else 0.0
    
    def get_top_items(self, db: Session, limit=10):
        query = text(f"""
            SELECT 
                i.name,
                COUNT(*) as order_count,
                SUM(ol.total_price) as total_revenue
            FROM order_lines ol
            JOIN items i ON ol.item_id = i.id
            GROUP BY i.name
            ORDER BY total_revenue DESC
            LIMIT {limit}
        """)
        results = db.execute(query).fetchall()
        return [{
            'name': row.name,
            'order_count': int(row.order_count),
            'total_revenue': float(row.total_revenue)
        } for row in results]
    
    def get_guest_spending(self, db: Session, days=30):
        query = text(f"""
            SELECT 
                g.id,
                g.first_name || ' ' || g.last_name as guest_name,
                COUNT(DISTINCT o.id) as order_count,
                SUM(o.total_amount) as total_spent
            FROM guests g
            JOIN orders o ON g.id = o.guest_id
            WHERE o.created_at >= NOW() - INTERVAL '{days} days'
            GROUP BY g.id, g.first_name, g.last_name
            ORDER BY total_spent DESC
        """)
        results = db.execute(query).fetchall()
        return [{
            'id': str(row.id),
            'guest_name': row.guest_name,
            'order_count': int(row.order_count),
            'total_spent': float(row.total_spent)
        } for row in results]
    
    def get_revenue_split(self, db: Session):
        query = text("""
            SELECT 
                o.name as outlet_name,
                SUM(ord.total_amount) as revenue,
                COUNT(DISTINCT ord.id) as order_count
            FROM outlets o
            JOIN orders ord ON o.id = ord.outlet_id
            WHERE DATE(ord.created_at) = CURRENT_DATE
            GROUP BY o.name
        """)
        results = db.execute(query).fetchall()
        return [{
            'outlet_name': row.outlet_name,
            'revenue': float(row.revenue),
            'order_count': int(row.order_count)
        } for row in results]
    
    def get_arpr(self, db: Session, days=30):  # Average Revenue Per Room
        query = text(f"""
            WITH room_revenue AS (
                SELECT 
                    r.id,
                    r.room_number,
                    COUNT(DISTINCT b.id) as booking_count,
                    SUM(b.total_amount) as total_revenue
                FROM rooms r
                LEFT JOIN bookings b ON r.id = b.room_id
                WHERE b.created_at >= NOW() - INTERVAL '{days} days'
                GROUP BY r.id, r.room_number
            )
            SELECT 
                room_number,
                COALESCE(total_revenue / NULLIF(booking_count, 0), 0) as arpr
            FROM room_revenue
            ORDER BY arpr DESC
        """)
        results = db.execute(query).fetchall()
        return [{
            'room_number': row.room_number,
            'arpr': float(row.arpr)
        } for row in results]
    
    def generate_ai_insights(self, metrics, openai_client):
        try:
            top_item = metrics['top_items'][0] if metrics['top_items'] else {'name': 'N/A', 'total_revenue': 0}
            arpr = metrics['arpr'][0]['arpr'] if metrics['arpr'] else 0
            
            prompt = f"""
            Based on these hotel metrics:
            - Today's Revenue: ${metrics['revenue_today']}
            - Occupancy Rate: {metrics['occupancy_rate']}%
            - Top selling item: {top_item['name']} (${top_item['total_revenue']})
            - Average Revenue Per Room: ${arpr}
            
            Provide 3 short, actionable business insights and recommendations.
            """
            
            response = openai_client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a hotel business analyst providing concise, actionable insights."},
                    {"role": "user", "content": prompt}
                ]
            )
            
            return response.choices[0].message.content.split("\n")
        except Exception as e:
            return [f"AI insights temporarily unavailable: {str(e)}"]