from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.personalized_news_digest.schemas import AgenticPersonalizedNewsDigestSessionCreate, AgenticPersonalizedNewsDigestSessionResponse
from app.domain.personalized_news_digest.service import AgenticPersonalizedNewsDigestService

router = APIRouter(prefix="/api/v1/personalized_news_digest", tags=["Agentic Personalized News Digest Domain"])

@router.post("/sessions", response_model=AgenticPersonalizedNewsDigestSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticPersonalizedNewsDigestSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Personalized News Digest.
    """
    return AgenticPersonalizedNewsDigestService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticPersonalizedNewsDigestSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticPersonalizedNewsDigestService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
