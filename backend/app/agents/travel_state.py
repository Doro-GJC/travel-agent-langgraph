from typing import TypedDict, List, Dict, Any


class TravelState(TypedDict, total=False):
    origin: str
    destination: str
    start_date: str
    days: int
    budget: float
    preferences: List[str]

    user_profile: Dict[str, Any]
    retrieved_context: str
    itinerary: List[Dict[str, Any]]
    budget_estimate: Dict[str, Any]
    tips: List[str]
    final_answer: Dict[str, Any]