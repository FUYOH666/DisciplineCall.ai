"""
DisciplineCall.ai - Personal AI Discipline Coach
Main FastAPI application entry point
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging
import os

# Import routers and services
from backend.api.auth import router as auth_router
from backend.api.users import router as users_router
from backend.api.calls import router as calls_router
from backend.api.metrics import router as metrics_router


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("disciplinecall")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events"""
    logger.info("🚀 DisciplineCall.ai starting up...")
    
    # TODO: Initialize database connections
    # TODO: Initialize AI engines
    # TODO: Initialize call services
    # TODO: Start background task scheduler
    
    yield
    
    logger.info("📞 DisciplineCall.ai shutting down...")
    
    # TODO: Clean up resources
    # TODO: Close database connections
    # TODO: Stop background tasks


# Create FastAPI application
app = FastAPI(
    title="DisciplineCall.ai API",
    description="Personal AI Discipline Coach - Proactive voice calls for building habits and achieving goals",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health check endpoint
@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "DisciplineCall.ai API is running! 🗣️",
        "version": "0.1.0",
        "status": "active",
        "features": [
            "AI-powered voice coaching",
            "Proactive daily calls",
            "Multi-platform support",
            "Cloud & local deployment"
        ]
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "disciplinecall-api",
        "timestamp": "2024-01-01T00:00:00Z"
    }


# Include API routers
app.include_router(auth_router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(users_router, prefix="/api/v1/users", tags=["Users"])
app.include_router(calls_router, prefix="/api/v1/calls", tags=["Calls"])
app.include_router(metrics_router, prefix="/api/v1/metrics", tags=["Metrics"])


if __name__ == "__main__":
    import uvicorn
    
    # Create necessary directories
    os.makedirs("logs", exist_ok=True)
    os.makedirs("audio_cache", exist_ok=True)
    os.makedirs("user_data", exist_ok=True)
    
    # Run the application
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
