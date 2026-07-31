# AI Banking Assistant

An AI-powered banking platform built with:

- FastAPI
- PostgreSQL
- Redis (Memurai)
- LangGraph
- ChromaDB
- Machine Learning
- JWT Authentication

## Features

- Loan Eligibility Prediction
- Fraud Detection
- Credit Score Prediction
- Customer Segmentation
- Complaint Classification
- Policy RAG Chatbot
- Multi-Agent Banking Assistant
- Redis Caching
- REST APIs

## Run

```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```
# Models

Trained ML models are not included because of GitHub size limits.

To generate models:

python ml/train_loan.py
python ml/train_fraud.py
python ml/train_credit_score.py