import re

from typing import List, Dict

from app.types.comment_type import CommentType


def enhance_timestamps(comments: List[CommentType]) -> List[CommentType]:
    formatted_comments = []
    for comment in comments:
        text = comment.get("text", "")

        match = re.search(r"(\d+:\d+)", text)

        timestamp = match.group(1) if match else None

        formatted_comments.append({"text": text, "timestamp": timestamp})

    return formatted_comments


def filter_with_timestamps(comments: List[CommentType]) -> List[CommentType]:
    return [comment for comment in comments if comment.get("timestamp") is not None]
