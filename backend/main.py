from fastapi import FastAPI

from backend.routes import (
    auth,
    loan,
    fraud,
    credit,
    segmentation,
    complaint,
    chatbot,
    agents,
    profile
)


app = FastAPI(
    title="AI Banking Assistant API",
    version="1.0.0"
)


@app.get("/")
def home():

    return {
        "message": "AI Banking Assistant Running"
    }


# Authentication
app.include_router(
    auth.router
)


# ML APIs

app.include_router(
    loan.router
)

app.include_router(
    fraud.router
)

app.include_router(
    credit.router
)

app.include_router(
    segmentation.router
)


# NLP

app.include_router(
    complaint.router
)


# RAG Chatbot

app.include_router(
    chatbot.router
)


# Profile

app.include_router(
    profile.router
)


# LangGraph Agents

app.include_router(
    agents.router
)