from pydantic import BaseModel


class LoanRequest(BaseModel):

    gender: int

    married: int

    education: int

    self_employed: int

    applicant_income: float

    coapplicant_income: float

    loan_amount: float

    loan_amount_term: float

    credit_history: int

    dependents_1: int

    dependents_2: int

    dependents_3_plus: int

    property_area_semiurban: int

    property_area_urban: int


class LoanResponse(BaseModel):

    prediction: str
