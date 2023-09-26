from typing import List


from app.clients.youtube_client import YouTubeClient


from app.types.timed_comments_service_type import TimedCommentsServiceType


from app.types.comment_type import CommentType


class YoutubeTimedCommentsService(TimedCommentsServiceType):
    def __init__(self, token: str):
        super().__init__("youtube-service")

        self.yt_client = YouTubeClient(token)

    def get_by_video_id(self, video_id: str) -> List[CommentType]:
        numeric_comments = self.yt_client.fetch_numeric_comments(video_id)

        return numeric_comments
