from sqlalchemy.orm import Session

from app.ai.kb_indexer import KnowledgeBaseIndexer
from app.ai.rag import RAGRetriever


class RAGService:

    @staticmethod
    def build_index(db: Session):
        return KnowledgeBaseIndexer.index(db)

    @staticmethod
    def search(
        query: str,
        k: int = 5,
    ):
        return RAGRetriever.search(query, k)