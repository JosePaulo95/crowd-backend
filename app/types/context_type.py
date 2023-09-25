from app.types.timed_comments_service_type import TimedCommentsServiceType

from typing import TypedDict


class ContextType(TypedDict):
    timed_comments_service: TimedCommentsServiceType
