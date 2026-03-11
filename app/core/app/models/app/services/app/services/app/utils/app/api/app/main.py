from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="AI Adaptive Diagnostic Engine",
    description="Adaptive GRE diagnostic system",
    version="1.0"
)

app.include_router(router)


@app.get("/")
def health_check():
    return {"status": "running"}
