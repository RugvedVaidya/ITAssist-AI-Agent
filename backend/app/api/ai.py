from fastapi import APIRouter

from app.ai.ticket_analyzer import TicketAnalyzer

from app.schemas.ai import (
    TicketAnalysisRequest,
    TicketAnalysisResponse,
)

router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)


@router.post(
    "/analyze",
    response_model=TicketAnalysisResponse,
)
def analyze_ticket(
    request: TicketAnalysisRequest,
):

    result = TicketAnalyzer.analyze(
        request.title,
        request.description,
    )

    return result