from langgraph.graph import StateGraph, END

from app.agents.travel_state import TravelState
from app.agents.nodes import (
    analyze_request_node,
    retrieve_context_node,
    plan_itinerary_node,
    estimate_budget_node,
    generate_tips_node,
    final_response_node,
)


def build_travel_graph():
    graph = StateGraph(TravelState)

    graph.add_node("analyze_request", analyze_request_node)
    graph.add_node("retrieve_context", retrieve_context_node)
    graph.add_node("plan_itinerary", plan_itinerary_node)
    graph.add_node("estimate_budget", estimate_budget_node)
    graph.add_node("generate_tips", generate_tips_node)
    graph.add_node("final_response", final_response_node)

    graph.set_entry_point("analyze_request")

    graph.add_edge("analyze_request", "retrieve_context")
    graph.add_edge("retrieve_context", "plan_itinerary")
    graph.add_edge("plan_itinerary", "estimate_budget")
    graph.add_edge("estimate_budget", "generate_tips")
    graph.add_edge("generate_tips", "final_response")
    graph.add_edge("final_response", END)

    return graph.compile()


travel_graph = build_travel_graph()