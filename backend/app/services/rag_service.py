from sqlalchemy.orm import Session

from app.ai.kb_indexer import KnowledgeBaseIndexer


class RAGService:

    @staticmethod
    def build_index(db: Session):

        return KnowledgeBaseIndexer.index(db)