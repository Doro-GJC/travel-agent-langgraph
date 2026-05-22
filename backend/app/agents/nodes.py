from app.agents.travel_state import TravelState


def analyze_request_node(state: TravelState) -> TravelState:
    preferences = state.get("preferences", [])

    state["user_profile"] = {
        "travel_style": "customized",
        "interests": preferences,
        "budget_level": "normal" if state.get("budget", 0) < 10000 else "comfortable",
    }

    return state


def retrieve_context_node(state: TravelState) -> TravelState:
    destination = state["destination"]

    # 这里先用 mock，后面再替换成真正的 RAG
    state["retrieved_context"] = f"""
    {destination} 是一个适合旅行的目的地。
    规划时需要考虑景点分布、交通时间、预算、餐饮、住宿和用户偏好。
    如果用户偏好包含美食、自然风景、历史文化，需要在行程中体现。
    """

    return state


def plan_itinerary_node(state: TravelState) -> TravelState:
    days = state["days"]
    destination = state["destination"]
    preferences = state.get("preferences", [])

    itinerary = []

    for day in range(1, days + 1):
        itinerary.append({
            "day": day,
            "title": f"{destination} 第 {day} 天行程",
            "morning": f"根据偏好 {preferences} 安排上午景点",
            "afternoon": f"游览 {destination} 代表性区域",
            "evening": "晚餐与自由活动",
        })

    state["itinerary"] = itinerary
    return state


def estimate_budget_node(state: TravelState) -> TravelState:
    budget = state["budget"]
    days = state["days"]

    state["budget_estimate"] = {
        "total_budget": budget,
        "daily_average": round(budget / days, 2),
        "transport": round(budget * 0.25, 2),
        "hotel": round(budget * 0.35, 2),
        "food": round(budget * 0.25, 2),
        "tickets_and_other": round(budget * 0.15, 2),
    }

    return state


def generate_tips_node(state: TravelState) -> TravelState:
    destination = state["destination"]

    state["tips"] = [
        f"建议提前查询 {destination} 的天气和交通情况。",
        "热门景点建议提前预约。",
        "每天行程不要安排过满，预留交通和休息时间。",
    ]

    return state


def final_response_node(state: TravelState) -> TravelState:
    state["final_answer"] = {
        "destination": state["destination"],
        "summary": f"已为你生成 {state['destination']} {state['days']} 天旅行计划。",
        "itinerary": state["itinerary"],
        "budget_estimate": state["budget_estimate"],
        "tips": state["tips"],
    }

    return state