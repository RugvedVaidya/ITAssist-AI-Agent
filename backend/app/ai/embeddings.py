from langchain_google_genai import GoogleGenerativeAIEmbeddings

from app.core.config import settings

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    google_api_key=settings.GEMINI_API_KEY,
)