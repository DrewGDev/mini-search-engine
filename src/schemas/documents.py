from pydantic import BaseModel, ConfigDict, Field


class DocumentCreateRequest(BaseModel):
    """model for document adition request endpoint"""
    text: str = Field(min_length=3)

    model_config = ConfigDict(
        json_schema_extra={
            "text": "The mouse robbed the cat"
        }
    )

class DocumentResponse(BaseModel):
    """generic model for document response endpoints"""
    id: int
    text: str

    model_config = ConfigDict(
        json_schema_extra={
            "id": 2,
            "text": "The cat robbed the mouse cheese"
        }
    )

class DocumentDeleteRequest(BaseModel):
    """model for document deletion request endpoint"""
    id: int

    model_config = ConfigDict(
        json_schema_extra={
            "id": 5
        }
    )