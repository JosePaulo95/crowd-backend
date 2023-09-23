from typing import Dict
from app.services.youtube_timed_comments_service import YoutubeTimedCommentsService
from app.types.context_type import ContextType


def contexts_repository() -> Dict[str, ContextType]:
    return {"youtube": {"timed_comments_service": YoutubeTimedCommentsService()}}
