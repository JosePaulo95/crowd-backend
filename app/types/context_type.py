from app.services.service_interface import TimedCommentsService

from typing import TypedDict


class ContextType(TypedDict):
    timed_comments_service: TimedCommentsService
