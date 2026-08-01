from langgraph.graph import StateGraph, END

from backend.agents.state import AgentState

from backend.agents.supervisor_agent import supervisor_agent



# ==================================================
# Execute Selected Agent (Lazy Loading)
# ==================================================

def execute_agent(state: AgentState):

    agent = state["agent_name"]


    # -------------------------------
    # Loan Agent
    # -------------------------------

    if agent == "loan_agent":

        from backend.agents.loan_agent import loan_agent

        return loan_agent(state)



    # -------------------------------
    # Fraud Agent
    # -------------------------------

    elif agent == "fraud_agent":

        from backend.agents.fraud_agent import fraud_agent

        return fraud_agent(state)



    # -------------------------------
    # Credit Agent
    # -------------------------------

    elif agent == "credit_agent":

        from backend.agents.credit_agent import credit_agent

        return credit_agent(state)



    # -------------------------------
    # Investment Agent
    # -------------------------------

    elif agent == "investment_agent":

        from backend.agents.investment_agent import investment_agent

        return investment_agent(state)



    # -------------------------------
    # Support Agent
    # -------------------------------

    elif agent == "support_agent":

        from backend.agents.support_agent import support_agent

        return support_agent(state)



    # -------------------------------
    # KYC Agent
    # -------------------------------

    elif agent == "kyc_agent":

        from backend.agents.kyc_agent import kyc_agent

        return kyc_agent(state)



    # -------------------------------
    # Policy RAG Agent
    # -------------------------------

    elif agent == "policy_rag_agent":

        from backend.agents.policy_rag_agent import policy_rag_agent


        answer = policy_rag_agent(
            state["query"]
        )


        state["response"] = answer

        state["final_answer"] = answer


        return state



    else:

        state["response"] = (
            "Sorry, I couldn't determine the correct banking agent."
        )

        state["final_answer"] = (
            state["response"]
        )

        return state




# ==================================================
# Build LangGraph Workflow
# ==================================================

workflow = StateGraph(
    AgentState
)



workflow.add_node(
    "supervisor",
    supervisor_agent
)



workflow.add_node(
    "executor",
    execute_agent
)



workflow.set_entry_point(
    "supervisor"
)




# ==================================================
# Routing Logic
# ==================================================

def router(state: AgentState):


    return "executor"




workflow.add_conditional_edges(

    "supervisor",

    router,

    {

        "executor": "executor"

    }

)



workflow.add_edge(

    "executor",

    END

)




# Compile Graph

graph = workflow.compile()




# ==================================================
# Public Function
# ==================================================

def run_agent(message: str):


    state = {

        "query": message,

        "agent_name": "",

        "response": "",

        "final_answer": ""

    }



    result = graph.invoke(
        state
    )


    return result