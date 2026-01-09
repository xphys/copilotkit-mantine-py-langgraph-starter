from agent.main import AgentState, graph

__all__ = ["graph", "AgentState"]


if __name__ == "__main__":
    # This allows running `python backend/agent.py` for quick checks.
    # The actual orchestration of `graph` (e.g. streaming, invoking)
    # should be handled by the frameworks/tools that import this module.
    print("Agent graph is ready:", graph)