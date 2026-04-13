from pydantic import BaseModel, Field, field_validator, model_validator
from typing import List
from datetime import date


# 请求参数
class PlanRequest(BaseModel):
    origin: str = Field(..., min_length=1, max_length=50, description="Departure city")
    destination: str = Field(..., min_length=1, max_length=50, description="Destination city")
    start_date: date = Field(..., description="Trip start date")
    days: int = Field(..., gt=0, le=30, description="Number of travel days")
    budget: float = Field(..., ge=0, description="Total budget")
    preferences: List[str] = Field(default_factory=list, max_length=10, description="Travel preferences")

    @field_validator("origin", "destination")
    @classmethod
    def validate_city(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("must not be empty")
        return value

    @field_validator("preferences")
    @classmethod
    def validate_preferences(cls, value: List[str]) -> List[str]:
        cleaned = []
        for item in value:
            item = item.strip()
            if item:
                cleaned.append(item)

        if len(cleaned) > 10:
            raise ValueError("preferences cannot contain more than 10 items")

        return cleaned

    @field_validator("start_date")
    @classmethod
    def validate_start_date(cls, value: date) -> date:
        if value < date.today():
            raise ValueError("start_date must not be in the past")
        return value

    @model_validator(mode="after")
    def validate_origin_destination(self):
        if self.origin == self.destination:
            raise ValueError("origin and destination must be different")
        return self


# 响应参数
class PlanResponse(BaseModel):
    destination: str = Field(..., min_length=1, max_length=50)
    itinerary_summary: str = Field(..., min_length=1, max_length=500)
    estimated_budget: float = Field(..., ge=0)
    suggestions: List[str] = Field(default_factory=list, max_length=10)
