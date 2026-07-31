from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.sql import func

from backend.database.db import Base


# ==============================
# USER TABLE
# ==============================

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String, nullable=False)

    email = Column(
        String,
        unique=True,
        index=True,
        nullable=False
    )

    hashed_password = Column(
        String,
        nullable=False
    )


# ==============================
# PREDICTION HISTORY
# ==============================

class PredictionHistory(Base):
    __tablename__ = "prediction_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_email = Column(
        String,
        nullable=False
    )

    prediction_type = Column(
        String,
        nullable=False
    )

    input_data = Column(
        Text,
        nullable=False
    )

    result = Column(
        Text,
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


# ==============================
# CHAT HISTORY
# ==============================

class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_email = Column(
        String,
        nullable=False
    )

    question = Column(
        Text,
        nullable=False
    )

    answer = Column(
        Text,
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
