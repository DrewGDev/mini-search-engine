
from fastapi import APIRouter, Depends, HTTPException

from src.domain.index_service import IndexService, get_index_service
from src.schemas.documents import DocumentCreateRequest, DocumentResponse

documents = APIRouter()

@documents.post("/documents", response_model=DocumentResponse, status_code=201)
async def create_document(request: DocumentCreateRequest, index_service: IndexService = Depends(get_index_service)):
    try:
        doc_id = await index_service.add_document(
            text=request.text
        )

        return DocumentResponse(
            id=doc_id,
            text=request.text
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    
@documents.get("/documents", status_code=200)
async def get_documents(index_service: IndexService = Depends(get_index_service)):
    try:
        documents = await index_service.get_all_documents()
        
        return documents
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )