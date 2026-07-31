from fastapi import APIRouter

from backend.schemas.complaint_schema import (
    ComplaintRequest,
    ComplaintResponse
)

from backend.services.complaint_service import classify_complaint

router = APIRouter(
    prefix="/complaint",
    tags=["Complaint Classification"]
)

@router.post(
    "/classify",
    response_model=ComplaintResponse
)
def classify(request: ComplaintRequest):

    category = classify_complaint(request.text)

    return ComplaintResponse(
        category=category
    )
