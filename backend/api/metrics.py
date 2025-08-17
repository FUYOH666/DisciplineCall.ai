"""Metrics API endpoints"""

from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard/{user_id}")
async def get_dashboard(user_id: str):
    return {"message": "Dashboard endpoint - to be implemented"}

@router.post("/track")
async def track_metrics():
    return {"message": "Track metrics endpoint - to be implemented"}
