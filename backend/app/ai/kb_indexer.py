from langchain_core.documents import Document

from sqlalchemy.orm import Session

from app.models.knowledge_base import KnowledgeBase

from app.ai.vector_store import vector_store


class KnowledgeBaseIndexer:

    @staticmethod
    def index(db: Session):

        vector_store.delete_collection()

        vector_store.__init__(
            collection_name="knowledge_base",
            embedding_function=vector_store._embedding_function,
            persist_directory="./chroma_db",
        )

        articles = db.query(KnowledgeBase).all()

        docs = []

        for article in articles:

            docs.append(
                Document(
                    page_content=article.content,
                    metadata={
                        "id": str(article.id),
                        "title": article.title,
                        "category": str(article.category_id),
                    },
                )
            )

        vector_store.add_documents(docs)

        return len(docs)