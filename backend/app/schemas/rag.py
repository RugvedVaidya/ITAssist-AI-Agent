from pydantic import BaseModel


class SearchRequest(BaseModel):
    query: str


class Source(BaseModel):
    title: str
    score: float


class SearchResponse(BaseModel):
    sources: list[Source]