from fastapi import APIRouter

from app.schemas.plan import PlanRequest, PlanResponse
from app.services.plan_service import generate_plan

router = APIRouter()


@router.post("/plan", response_model=PlanResponse, summary="Create a travel plan")
def create_plan(request: PlanRequest) -> PlanResponse:
    return generate_plan(request)
