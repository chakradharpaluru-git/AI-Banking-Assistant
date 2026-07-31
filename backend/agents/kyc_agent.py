from backend.agents.state import AgentState


def kyc_agent(state: AgentState) -> AgentState:


    response = """
For KYC verification, customers generally need:

1. PAN Card
2. Identity Proof
3. Address Proof
4. Passport size photograph

Accepted identity documents may include:
- Aadhaar Card
- Passport
- Driving License
- Voter ID

Please ensure your documents are valid and updated.
"""


    state["response"] = response

    state["final_answer"] = response


    return state
def kyc_agent(state):


    answer = """
KYC documents required:

1. Aadhaar Card
2. PAN Card
3. Address Proof
4. Identity Proof
5. Passport size photograph
"""


    state["response"]=answer


    return state
