from typing import TypedDict


class AgentState(TypedDict):

    query: str

    agent_name: str

    response: str
