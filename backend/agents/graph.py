from langgraph.graph import StateGraph, END


from backend.agents.state import AgentState

from backend.agents.supervisor_agent import supervisor_agent

from backend.agents.loan_agent import loan_agent
from backend.agents.fraud_agent import fraud_agent
from backend.agents.credit_agent import credit_agent
from backend.agents.investment_agent import investment_agent
from backend.agents.support_agent import support_agent
from backend.agents.kyc_agent import kyc_agent
from backend.agents.policy_rag_agent import policy_rag_agent



# --------------------------------------------------
# Execute Selected Agent
# --------------------------------------------------

def execute_agent(state: AgentState):

    agent = state["agent_name"]


    if agent == "loan_agent":
        return loan_agent(state)


    elif agent == "fraud_agent":
        return fraud_agent(state)


    elif agent == "credit_agent":
        return credit_agent(state)


    elif agent == "investment_agent":
        return investment_agent(state)


    elif agent == "support_agent":
        return support_agent(state)


    elif agent == "kyc_agent":
        return kyc_agent(state)


    elif agent == "policy_rag_agent":
        return policy_rag_agent(state)


    else:

        state["response"] = (
            "Sorry, I couldn't determine the correct banking agent."
        )

        return state




# --------------------------------------------------
# Build LangGraph Workflow
# --------------------------------------------------

workflow = StateGraph(AgentState)



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



# --------------------------------------------------
# Router
# --------------------------------------------------

def router(state: AgentState):

    if state["agent_name"] in [

        "loan_agent",
        "fraud_agent",
        "credit_agent",
        "investment_agent",
        "support_agent",
        "kyc_agent",
        "policy_rag_agent"

    ]:

        return "executor"


    return END




workflow.add_conditional_edges(

    "supervisor",

    router,

    {

        "executor": "executor",

        END: END

    }

)



workflow.add_edge(

    "executor",

    END

)



graph = workflow.compile()




# --------------------------------------------------
# Public Function
# --------------------------------------------------

def run_agent(message: str):


    state = {

        "query": message,

        "agent_name": None,

        "response": ""

    }


    result = graph.invoke(state)


    return result