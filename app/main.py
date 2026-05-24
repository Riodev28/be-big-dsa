from fastapi import FastAPI
from .features.temporal_complexity.router import router as temporal_router
from .core import setup_middlewares

app = FastAPI(title="BigDSA", version="1.0.0")

API_PREFIX = "/api"
ANALYZE_PREFIX = "/analyze"

setup_middlewares(app)

app.include_router(temporal_router, prefix=f"{API_PREFIX}{ANALYZE_PREFIX}")

@app.get("/health")
def health():
    return {"status": "ok"}
