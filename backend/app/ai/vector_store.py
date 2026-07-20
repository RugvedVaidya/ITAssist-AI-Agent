from langchain_chroma import Chroma

from app.ai.embeddings import embeddings

vector_store = Chroma(
    collection_name="knowledge_base",
    embedding_function=embeddings,
    persist_directory="./chroma_db",
)