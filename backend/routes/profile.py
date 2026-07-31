from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.dependencies import get_current_user
from backend.database.db import get_db


router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)



@router.get("/")
def get_profile(

    current_user = Depends(get_current_user),

    db: Session = Depends(get_db)

):


    return {


        "name": current_user.full_name,


        "email": current_user.email,


        "account_type":
        "Savings Account",


        "account_status":
        "Active",


        "credit_score":
        "N/A",


        "customer_segment":
        "N/A"


    }
