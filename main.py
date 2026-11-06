from fastapi import FastAPI

from src.api.v1.router import v1_router

app = FastAPI(
    title="MiniSearchEngine",
    description="A mini search engine for study purpose"
)

app.include_router(v1_router, prefix="/api/v1")

@app.get("/", status_code=200)
async def get_health():
    return {
        "api": app.title or "MiniSearchEngine",
        "health": "OK"
        }