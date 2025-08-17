"""Authentication API endpoints"""

from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
async def login():
    return {"message": "Login endpoint - to be implemented"}

@router.post("/register") 
async def register():
    return {"message": "Register endpoint - to be implemented"}
