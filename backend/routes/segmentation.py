from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.segmentation_service import predict_segment

router = APIRouter(
    prefix="/customer",
    tags=["Customer Segmentation"]
)


class SegmentationRequest(BaseModel):
    Monthly_Inhand_Salary: float
    Num_Bank_Accounts: int
    Num_Credit_Card: int
    Interest_Rate: float
    Delay_from_due_date: int
    Num_Credit_Inquiries: int
    Credit_Utilization_Ratio: float
    Total_EMI_per_month: float


class SegmentationResponse(BaseModel):
    segment: str


@router.post(
    "/segment",
    response_model=SegmentationResponse
)
def segment_customer(request: SegmentationRequest):

    result = predict_segment(
        request.model_dump()
    )

    return {
        "segment": result
    }
