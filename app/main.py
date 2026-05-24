from fastapi import FastAPI
from .features.temporal_complexity.router import router as temporal_router

app = FastAPI(title="BigDSA", version="1.0.0")

app.include_router(temporal_router, prefix="/analyze")


@app.get("/health")
def health():
    return {"status": "ok"}
