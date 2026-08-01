from fastapi import FastAPI


# =====================================================
# FastAPI App
# =====================================================

app = FastAPI(
    title="AI Banking Assistant API",
    version="1.0.0",
    description="AI Banking Assistant using ML, RAG and LangGraph"
)


# =====================================================
# Home
# =====================================================

@app.get("/")
def home():

    return {
        "message": "AI Banking Assistant Running",
        "status": "active"
    }



# =====================================================
# Load Routers Safely
# =====================================================

try:

    from backend.routes import auth
    app.include_router(auth.router)
    print("✅ Auth Router Loaded")


except Exception as e:

    print("❌ Auth Router Error:", e)



try:

    from backend.routes import loan
    app.include_router(loan.router)
    print("✅ Loan Router Loaded")


except Exception as e:

    print("❌ Loan Router Error:", e)



try:

    from backend.routes import fraud
    app.include_router(fraud.router)
    print("✅ Fraud Router Loaded")


except Exception as e:

    print("❌ Fraud Router Error:", e)



try:

    from backend.routes import credit
    app.include_router(credit.router)
    print("✅ Credit Router Loaded")


except Exception as e:

    print("❌ Credit Router Error:", e)



try:

    from backend.routes import segmentation
    app.include_router(segmentation.router)
    print("✅ Segmentation Router Loaded")


except Exception as e:

    print("❌ Segmentation Router Error:", e)



try:

    from backend.routes import complaint
    app.include_router(complaint.router)
    print("✅ Complaint Router Loaded")


except Exception as e:

    print("❌ Complaint Router Error:", e)



try:

    from backend.routes import chatbot
    app.include_router(chatbot.router)
    print("✅ Chatbot Router Loaded")


except Exception as e:

    print("❌ Chatbot Router Error:", e)



try:

    from backend.routes import profile
    app.include_router(profile.router)
    print("✅ Profile Router Loaded")


except Exception as e:

    print("❌ Profile Router Error:", e)



try:

    from backend.routes import agents
    app.include_router(agents.router)
    print("✅ Agents Router Loaded")


except Exception as e:

    print("❌ Agents Router Error:", e)