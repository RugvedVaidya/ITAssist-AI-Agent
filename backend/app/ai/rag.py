from typing import List

from app.ai.llm import client
from app.ai.vector_store import vector_store


class RAGRetriever:

    @staticmethod
    def search(
        query: str,
        k: int = 5,
    ):
        """
        Returns:
        [
            (Document, score),
            (Document, score),
            ...
        ]
        """

        return vector_store.similarity_search_with_score(
            query=query,
            k=k,
        )


class RAGEngine:

    @staticmethod
    def ask(
        question: str,
        k: int = 5,
    ):

        docs = vector_store.similarity_search_with_score(
            query=question,
            k=k,
        )

        if not docs:

            return {
                "answer": "No relevant knowledge base articles were found.",
                "sources": [],
            }

        context = ""

        sources = []

        for document, score in docs:

            context += f"""
Title:
{document.metadata.get("title","Unknown")}

Content:
{document.page_content}

-----------------------------------------
"""

            sources.append(
                {
                    "title": document.metadata.get(
                        "title",
                        "Unknown",
                    ),
                    "score": float(score),
                }
            )

        prompt = f"""
You are an experienced IT Support Engineer.

Answer ONLY using the provided knowledge base.

If the answer cannot be found in the knowledge base,
say that the information is unavailable.

Knowledge Base:

{context}

Question:

{question}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return {
            "answer": response.text,
            "sources": sources,
        }