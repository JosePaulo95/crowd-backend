from typing import Dict, List
from app.services.youtube_timed_comments_service import YoutubeTimedCommentsService
from app.types.context_type import ContextType


def contexts_repository() -> List[ContextType]:
    return [
        {
            "platform": "youtube",
            "comments_service": YoutubeTimedCommentsService(
                "AIzaSyC-aDn5Ud486MMctuBepELtvgiaRUUrJhI"
            ),
        }
    ]
