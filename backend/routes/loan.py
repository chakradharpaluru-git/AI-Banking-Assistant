from fastapi import APIRouter

from backend.schemas.loan_schema import (
    LoanRequest,
    LoanResponse
)

from backend.services.loan_service import predict_loan


router = APIRouter(
    prefix="/loan",
    tags=["Loan Prediction"]
)


@router.post(
    "/predict",
    response_model=LoanResponse
)
def predict(request: LoanRequest):

    result = predict_loan(
        request.dict()
    )

    return {
        "prediction": result
    }
