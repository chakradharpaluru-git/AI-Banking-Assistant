from pydantic import BaseModel


class SegmentationRequest(BaseModel):

    income: float
    balance: float
    transactions: int
    credit_score: int



class SegmentationResponse(BaseModel):

    segment: str
