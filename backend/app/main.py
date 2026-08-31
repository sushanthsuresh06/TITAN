from fastapi import FastAPI

from backend.app.api.health import router as health_router
from backend.app.core.config import APP_NAME, APP_VERSION
from backend.app.core.logging import setup_logging

setup_logging()

app = FastAPI(
    title=APP_NAME,
    description="Multi-Vendor DVR/NVR Forensic Analysis System",
    version=APP_VERSION
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "project": APP_NAME,
        "status": "Backend running",
        "version": APP_VERSION
    }