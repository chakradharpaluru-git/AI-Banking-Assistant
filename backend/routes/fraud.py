from fastapi import APIRouter

from backend.schemas.fraud_schema import (
    FraudRequest,
    FraudResponse
)

from backend.services.fraud_service import (
    predict_fraud
)

router = APIRouter(
    prefix="/fraud",
    tags=["Fraud Detection"]
)


@router.post(
    "/predict",
    response_model=FraudResponse
)
def predict(request: FraudRequest):

    result = predict_fraud(
        request.model_dump()
    )

    return FraudResponse(
        prediction=result
    )
