from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_active_user
from app.core.permissions import check_permissions
from app.models.user import User, UserRole
from app.services.analytics import AnalyticsService
from app.core.config import settings
import openai

router = APIRouter()
analytics_service = AnalyticsService()

# Configure OpenAI
openai.api_key = settings.OPENAI_API_KEY

@router.get("/dashboard")
@check_permissions([UserRole.admin])
async def get_dashboard_metrics(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> dict:
    try:
        # Get all metrics
        revenue_today = analytics_service.get_revenue_today(db)
        occupancy_rate = analytics_service.get_occupancy_rate(db)
        top_items = analytics_service.get_top_items(db, limit=5)
        revenue_split = analytics_service.get_revenue_split(db)
        arpr = analytics_service.get_arpr(db)
        
        # Compile metrics for AI insights
        metrics = {
            'revenue_today': revenue_today,
            'occupancy_rate': occupancy_rate,
            'top_items': top_items,
            'arpr': arpr[0]['arpr'] if arpr else 0
        }
        
        # Generate AI insights
        ai_insights = analytics_service.generate_ai_insights(metrics, openai)
        
        return {
            "metrics": {
                "revenue_today": revenue_today,
                "occupancy_rate": occupancy_rate,
                "top_items": top_items,
                "revenue_split": revenue_split,
                "arpr": arpr
            },
            "ai_insights": ai_insights
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/guest-spending")
@check_permissions([UserRole.admin, UserRole.receptionist])
async def get_guest_spending(
    days: int = 30,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> List[dict]:
    try:
        return analytics_service.get_guest_spending(db, days)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/revenue-split")
@check_permissions([UserRole.admin])
async def get_revenue_split(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> List[dict]:
    try:
        return analytics_service.get_revenue_split(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))