from typing import List
from app.clients.youtube_client import YouTubeClient
from app.services.service_interface import TimedCommentsService
from app.types.comment_type import CommentType


class YoutubeTimedCommentsService(TimedCommentsService):
    def __init__(self, token: str):
        super().__init__("youtube-service")
        self.yt_client = YouTubeClient(token)

    def get_by_video_id(self, video_id: str) -> List[CommentType]:
        comments_with_numbers = self.yt_client.fetch_numeric_comments(video_id)
        return comments_with_numbers
