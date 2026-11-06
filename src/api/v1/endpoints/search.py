from fastapi import APIRouter, Depends, HTTPException

from src.domain.index_service import IndexService, get_index_service
from src.domain.vector_space import VectorCompare
from src.schemas.search import Chunk, SearchRequest, SearchResponse

search = APIRouter()

@search.post("/search", response_model=SearchResponse, status_code=200)
async def vector_search(request: SearchRequest, index_service: IndexService = Depends(get_index_service)):
    """
    Execute the vector search
    """
    try:
        vector_compare: VectorCompare = VectorCompare()

        results = await vector_compare.search(
            query=request.query,
            index=await index_service.get_all_indexes()
        )

        chunks : list[Chunk] = []
        for res in results[:request.limit]:
            chunks.append(
                Chunk(
                    doc_id=res[0],
                    score=res[1],
                    text=await index_service.get_document_text(res[0])
                )
            )

        return SearchResponse(
            chunks=chunks
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )