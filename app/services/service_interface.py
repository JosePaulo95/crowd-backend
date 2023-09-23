from abc import ABC, abstractmethod


class TimedCommentsService(ABC):
    title: str

    def __init__(self, title: str):
        self.title = title

    @abstractmethod
    def get_by_video_id(self, video_id: str):
        pass
