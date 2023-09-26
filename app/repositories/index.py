from app.errors.errors import InvalidPlatformError
from app.repositories.contexts_repository import contexts_repository
from typing import Dict, List, Optional

from app.types.context_type import ContextType


def get_all_contexts_repository() -> List[Dict[str, str]]:
    repo = contexts_repository()  # Assumindo que isso retorna uma lista de ContextType
    return [
        {
            "platform": context["platform"],
            "comment_service": context["comments_service"].title,
        }
        for context in repo
    ]


def get_context_repository(platform: str) -> ContextType:
    repo = contexts_repository()
    for context in repo:
        if context["platform"] == platform:
            return context
    raise InvalidPlatformError(f"Platform {platform} not identified.")
