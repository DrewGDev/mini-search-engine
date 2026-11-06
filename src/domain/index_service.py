from typing import Any

from src.domain.term_frequency import get_concordance


class IndexService:
    def __init__(self) -> None:
        self._documents: dict[int, str] = {}
        self._index: dict[int, dict[str, int]] = {}
        self._current_id: int = 1

    async def add_document(self, text: str) -> int:
        doc_id = self._current_id
        self._documents[doc_id] = text
        self._index[doc_id] = await get_concordance(text)

        self._current_id += 1
        return doc_id
    
    async def get_all_documents(self) -> list[dict[str, Any]]:
        return [{"id": doc_id, "text": text} for doc_id, text in self._documents.items()]
    
    async def get_all_indexes(self):
        return self._index

    async def get_document_text(self, doc_id: int) -> str:
        return self._documents[doc_id]
    
_index_service = IndexService()

async def get_index_service() -> IndexService:
    return _index_service