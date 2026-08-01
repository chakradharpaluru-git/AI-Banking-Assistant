from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter(
    prefix="/agents",
    tags=["AI Agents"]
)


class AgentRequest(BaseModel):
    message: str



class AgentResponse(BaseModel):
    agent: str
    response: str



@router.post(
    "/query",
    response_model=AgentResponse
)
def query_agent(
    data: AgentRequest
):

    try:

        from backend.agents.graph import run_agent


        result = run_agent(
            data.message
        )


        return {

            "agent": result.get(
                "agent_name",
                "unknown"
            ),

            "response": result.get(
                "response",
                ""
            )

        }


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )