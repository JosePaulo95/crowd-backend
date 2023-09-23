from app.repositories.contexts_repository import contexts_repository
from typing import Dict

from app.types.context_type import ContextType


def get_all_contexts_repository() -> Dict[str, str]:
    repo = contexts_repository()
    return {key: value["timed_comments_service"].title for key, value in repo.items()}


def get_context_repository(context_id) -> ContextType:
    repo = contexts_repository()
    return repo[context_id]
