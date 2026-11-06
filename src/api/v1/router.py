from fastapi import APIRouter

from src.api.v1.endpoints import documents, search

v1_router = APIRouter()

v1_router.include_router(
    documents.documents,
    tags=["Documents"]
)

v1_router.include_router(
    search.search,
    tags=["Search"]
)