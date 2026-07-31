from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.db import get_db
from backend.models import User

from backend.schemas.auth_schema import (
    RegisterRequest,
    LoginRequest
)

from backend.utils.security import (
    hash_password,
    verify_password,
    create_token
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# =====================================================
# Register
# =====================================================

@router.post("/register")
def register(
    user: RegisterRequest,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = User(
        full_name=user.name,
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully"
    }


# =====================================================
# Login
# =====================================================

@router.post("/login")
def login(
    user: LoginRequest,
    db: Session = Depends(get_db)
):

    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if db_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(
        user.password,
        db_user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_token(
        {
            "email": db_user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
