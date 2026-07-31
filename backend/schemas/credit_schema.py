from pydantic import BaseModel


class CreditRequest(BaseModel):
    Age: int
    Annual_Income: float
    Monthly_Inhand_Salary: float
    Num_Bank_Accounts: int
    Num_Credit_Card: int
    Interest_Rate: float
    Num_of_Loan: int
    Delay_from_due_date: int
    Num_of_Delayed_Payment: int
    Changed_Credit_Limit: float
    Outstanding_Debt: float
    Credit_Utilization_Ratio: float
    Monthly_Balance: float


class CreditResponse(BaseModel):
    prediction: str
