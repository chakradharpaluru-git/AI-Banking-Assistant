from fastapi import APIRouter
from pydantic import BaseModel

from backend.agents.graph import run_agent

router = APIRouter(
    prefix="/agents",
    tags=["AI Agents"]
)


class AgentRequest(BaseModel):
    message: str


class AgentResponse(BaseModel):
    agent: str
    response: str


@router.post("/query", response_model=AgentResponse)
def query_agent(data: AgentRequest):

    result = run_agent(data.message)

    return {
        "agent": result["agent_name"],
        "response": result["response"]
    }
