from backend.agents.state import AgentState


def supervisor_agent(state: AgentState):

    query = state["query"].lower()

    if any(word in query for word in [
        "loan",
        "emi",
        "borrow",
        "eligibility"
    ]):
        state["agent_name"] = "loan_agent"

    elif any(word in query for word in [
        "fraud",
        "transaction",
        "scam",
        "stolen"
    ]):
        state["agent_name"] = "fraud_agent"

    elif any(word in query for word in [
        "credit score",
        "cibil",
        "score"
    ]):
        state["agent_name"] = "credit_agent"

    elif any(word in query for word in [
        "investment",
        "mutual fund",
        "stocks"
    ]):
        state["agent_name"] = "investment_agent"

    elif any(word in query for word in [
        "kyc",
        "documents"
    ]):
        state["agent_name"] = "kyc_agent"

    elif any(word in query for word in [
        "rbi",
        "policy",
        "guideline"
    ]):
        state["agent_name"] = "policy_rag_agent"

    else:
        state["agent_name"] = "support_agent"

    return state
