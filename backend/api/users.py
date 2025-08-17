"""Users API endpoints"""

from fastapi import APIRouter

router = APIRouter()

@router.get("/profile")
async def get_profile():
    return {"message": "User profile endpoint - to be implemented"}

@router.put("/preferences")
async def update_preferences():
    return {"message": "Update preferences endpoint - to be implemented"}
