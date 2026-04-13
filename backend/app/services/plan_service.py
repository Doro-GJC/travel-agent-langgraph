from app.schemas.plan import PlanRequest, PlanResponse


def generate_plan(request: PlanRequest) -> PlanResponse:
    summary = (
        f"A {request.days}-day trip from {request.origin} "
        f"to {request.destination} starting on {request.start_date}."
    )

    suggestions = [
        "Visit the city center",
        "Try local food",
        "Reserve a hotel near popular attractions",
    ]

    preferences_lower = [item.lower() for item in request.preferences]

    if "food" in preferences_lower:
        suggestions.append("Explore popular local restaurants")

    if "shopping" in preferences_lower:
        suggestions.append("Visit major shopping districts")

    return PlanResponse(
        destination=request.destination,
        itinerary_summary=summary,
        estimated_budget=request.budget,
        suggestions=suggestions[:10],
    )