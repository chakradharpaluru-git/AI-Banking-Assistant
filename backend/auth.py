# ==========================================================
# AI Banking Assistant
# Authentication Module
# Register + Login + JWT
# ==========================================================


from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from pydantic import BaseModel, EmailStr

from passlib.context import CryptContext

from jose import jwt

from datetime import datetime, timedelta


from backend.database.db import get_db

from models import User



# ==========================================================
# Router
# ==========================================================


router = APIRouter(

    prefix="/auth",

    tags=["Authentication"]

)



# ==========================================================
# JWT Configuration
# ==========================================================


SECRET_KEY = "secretkey"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60



# ==========================================================
# Password Hashing
# ==========================================================


pwd_context = CryptContext(

    schemes=["bcrypt"],

    deprecated="auto"

)



# ==========================================================
# Schemas
# ==========================================================


class RegisterRequest(BaseModel):

    full_name: str

    email: EmailStr

    password: str





class LoginRequest(BaseModel):

    email: EmailStr

    password: str





# ==========================================================
# Utility Functions
# ==========================================================


def hash_password(password):

    return pwd_context.hash(password)





def verify_password(
        plain_password,
        hashed_password
):

    return pwd_context.verify(

        plain_password,

        hashed_password

    )





def create_access_token(data: dict):


    to_encode = data.copy()


    expire = datetime.utcnow() + timedelta(

        minutes=ACCESS_TOKEN_EXPIRE_MINUTES

    )


    to_encode.update(

        {

            "exp": expire

        }

    )


    token = jwt.encode(

        to_encode,

        SECRET_KEY,

        algorithm=ALGORITHM

    )


    return token





# ==========================================================
# REGISTER API
# ==========================================================


@router.post("/register")
def register(

    user_data: RegisterRequest,

    db: Session = Depends(get_db)

):


    # Check existing user

    existing_user = db.query(User).filter(

        User.email == user_data.email

    ).first()



    if existing_user:


        raise HTTPException(

            status_code=400,

            detail="Email already registered"

        )



    # Create user


    new_user = User(

        full_name=user_data.full_name,

        email=user_data.email,

        hashed_password=hash_password(

            user_data.password

        )

    )



    db.add(new_user)

    db.commit()

    db.refresh(new_user)



    return {


        "message":
        "User registered successfully",


        "user": {


            "id": new_user.id,

            "name": new_user.full_name,

            "email": new_user.email

        }


    }





# ==========================================================
# LOGIN API
# ==========================================================


@router.post("/login")
def login(

    login_data: LoginRequest,

    db: Session = Depends(get_db)

):


    user = db.query(User).filter(

        User.email == login_data.email

    ).first()



    if not user:


        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="Invalid email or password"

        )



    # Verify password


    if not verify_password(

        login_data.password,

        user.hashed_password

    ):


        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="Invalid email or password"

        )



    # Create JWT


    access_token = create_access_token(

        {

            "sub": user.email

        }

    )



    return {


        "message":
        "Login successful",


        "access_token":
        access_token,


        "token_type":
        "bearer",


        "user": {


            "id": user.id,


            "name": user.full_name,


            "email": user.email


        }


    }
