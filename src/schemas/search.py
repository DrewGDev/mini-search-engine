from pydantic import BaseModel, ConfigDict, Field


class SearchRequest(BaseModel):
    """model for search request endpoint"""
    query: str
    limit: int = Field(default=6, ge=1, le=50)

    model_config = ConfigDict(
        json_schema_extra={
            "query": "termo",
            "limit": 6
        }
    )

class Chunk(BaseModel):
    """model for chunk"""
    doc_id: int
    score: float
    text: str

    model_config = ConfigDict(
        json_schema_extra={
            "doc_id": 1,
            "score": 0.85,
            "text": "..."
        }
    )

class SearchResponse(BaseModel):
    """model for search response enpoint"""
    chunks: list[Chunk]