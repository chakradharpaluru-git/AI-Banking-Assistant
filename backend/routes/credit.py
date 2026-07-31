from fastapi import APIRouter

from backend.schemas.credit_schema import (
    CreditRequest,
    CreditResponse
)

from backend.services.credit_service import predict_credit

router = APIRouter(
    prefix="/credit",
    tags=["Credit Score"]
)


@router.post(
    "/predict",
    response_model=CreditResponse
)
def predict(request: CreditRequest):

    result = predict_credit(
        request.model_dump()
    )

    return {
        "prediction": result
    }
