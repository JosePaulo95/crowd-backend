from typing import TypedDict, Optional


class CommentType(TypedDict, total=False):
    text: str
    timestamp: Optional[str]
