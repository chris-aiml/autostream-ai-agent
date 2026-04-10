from typing import TypedDict
from langgraph.graph import StateGraph, END
from intent import detect_intent
from rag import retrieve
from tools import mock_lead_capture

# 🧠 Define state
class AgentState(TypedDict):
    user_input: str
    intent: str
    response: str
    name: str
    email: str
    platform: str


# 🔹 Node 1: Detect Intent
def intent_node(state: AgentState):
    intent = detect_intent(state["user_input"])
    return {**state, "intent": intent}


# 🔹 Node 2: Handle Greeting
def greeting_node(state: AgentState):
    return {**state, "response": "Hey! 👋 How can I help you with AutoStream today?"}


# 🔹 Node 3: RAG Retrieval
def rag_node(state: AgentState):
    context = retrieve(state["user_input"])
    return {**state, "response": f"Here’s what I found:\n{context}"}


# 🔹 Node 4: Lead Capture (simplified)
def lead_node(state: AgentState):
    print("Agent: Awesome! Let's get you started 🚀")

    name = input("Agent: What's your name? ")
    email = input("Agent: Your email? ")
    platform = input("Agent: Which platform do you create content on? ")

    mock_lead_capture(name, email, platform)

    return {
        **state,
        "response": "You're all set! 🎉",
        "name": name,
        "email": email,
        "platform": platform
    }


# 🔀 Router (decides flow)
def router(state: AgentState):
    intent = state["intent"]

    if intent == "greeting":
        return "greeting"

    elif intent == "pricing":
        return "rag"

    elif intent == "high_intent":
        return "lead"

    else:
        return "rag"


# 🚀 Build Graph
graph = StateGraph(AgentState)

graph.add_node("intent", intent_node)
graph.add_node("greeting", greeting_node)
graph.add_node("rag", rag_node)
graph.add_node("lead", lead_node)

# Flow
graph.set_entry_point("intent")

graph.add_conditional_edges(
    "intent",
    router,
    {
        "greeting": "greeting",
        "rag": "rag",
        "lead": "lead"
    }
)

# End points
graph.add_edge("greeting", END)
graph.add_edge("rag", END)
graph.add_edge("lead", END)

# Compile
app = graph.compile()