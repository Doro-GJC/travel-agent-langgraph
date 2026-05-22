from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.plan import router as plan_router
from app.core.config import settings
from app.core.middleware import register_middleware

app = FastAPI(title=settings.app_name)

register_middleware(app)

app.include_router(health_router, prefix="/api", tags=["health"])
app.include_router(plan_router, prefix="/api", tags=["plan"])


@app.get("/")
def read_root():
    return {"message": "Travel Agent backend is running"}