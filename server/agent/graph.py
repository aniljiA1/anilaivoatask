from langgraph.graph import StateGraph
from agent.tools import (
    log_interaction,
    edit_interaction,
    get_hcp_history,
    suggest_next_action,
    sentiment_analysis,
)

# 🧠 Router (KEEP input)
def router(state):
    msg = state["input"].lower()

    if "edit" in msg:
        next_step = "edit"
    elif "history" in msg:
        next_step = "history"
    elif "suggest" in msg:
        next_step = "suggest"
    elif "sentiment" in msg:
        next_step = "sentiment"
    else:
        next_step = "log"

    return {
        "input": state["input"],   # ✅ keep input
        "next": next_step
    }


builder = StateGraph(dict)

# 🔹 Nodes (IMPORTANT: pass input again)

builder.add_node("router", router)

builder.add_node("log", lambda s: {
    "result": log_interaction({
        "doctor": "Unknown",
        "notes": s["input"]
    })
})

builder.add_node("edit", lambda s: {
    "result": edit_interaction({
        "id": 1,
        "notes": s["input"]
    })
})

builder.add_node("history", lambda s: {
    "result": get_hcp_history({
        "doctor": "Unknown"
    })
})

builder.add_node("suggest", lambda s: {
    "result": suggest_next_action({
        "notes": s["input"]
    })
})

builder.add_node("sentiment", lambda s: {
    "result": sentiment_analysis({
        "text": s["input"]
    })
})

# Entry
builder.set_entry_point("router")

# Routing
builder.add_conditional_edges(
    "router",
    lambda x: x["next"],
    {
        "log": "log",
        "edit": "edit",
        "history": "history",
        "suggest": "suggest",
        "sentiment": "sentiment",
    },
)

graph = builder.compile()