from app.services.service_interface import TimedCommentsService


class YoutubeTimedCommentsService(TimedCommentsService):
    def __init__(self):
        super().__init__("youtube-service")

    def get_by_video_id(self, video_id: str):
        return f"Fetching Youtube timed comments for video {video_id}"
