from abc import ABC, abstractmethod

from typing import List


from app.types.comment_type import CommentType


class TimedCommentsServiceType(ABC):
    title: str

    def __init__(self, title: str):
        self.title = title

    @abstractmethod
    def get_by_video_id(self, video_id: str) -> List[CommentType]:
        pass
