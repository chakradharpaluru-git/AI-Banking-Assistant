from backend.agents.state import AgentState


def investment_agent(state: AgentState) -> AgentState:
    """
    Investment Agent:
    Provides basic investment suggestions.
    """

    query = state["query"].lower()


    # Default investment advice

    response = """
Based on your savings and risk profile, you can consider:

1. Fixed Deposits (FD)
   - Low risk
   - Stable returns
   - Suitable for conservative investors

2. Mutual Funds
   - Medium risk
   - Better long-term growth potential
   - Choose funds based on your risk capacity

3. Government Bonds
   - Low risk
   - Government-backed investment option

Before investing, consider:
- Your financial goals
- Investment duration
- Risk tolerance
- Emergency fund requirements

For personalized investment advice, your income,
expenses, and risk profile should be analyzed.
"""


    # Store response

    state["response"] = response

    state["final_answer"] = response


    return state
