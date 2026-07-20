from pydantic import BaseModel


class TicketAnalysisRequest(BaseModel):
    title: str
    description: str


class TicketAnalysisResponse(BaseModel):

    category: str

    department: str

    priority: str

    summary: str

    suggested_resolution: str