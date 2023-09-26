from app.types.timed_comments_service_type import TimedCommentsServiceType

from typing import TypedDict


class ContextType(TypedDict):
    platform: str
    comments_service: TimedCommentsServiceType
