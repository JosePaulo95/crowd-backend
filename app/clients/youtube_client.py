from typing import List

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from app.errors.errors import (
    QuotaExceededException,
    NetworkErrorException,
    ExternalServiceFieldException,
)
from app.types.comment_type import CommentType
from app.types.youtube_response_type import YoutubeResponse
from app.types.youtube_response_type import YoutubeResponse
from pydantic import ValidationError as PydanticValidationError


class YouTubeClient:
    def __init__(self, api_key: str):
        self.youtube = build("youtube", "v3", developerKey=api_key)

    def _search_comments(self, video_id: str, search_term: str) -> List[CommentType]:
        try:
            request = self.youtube.commentThreads().list(
                part="snippet", searchTerms=search_term, videoId=video_id
            )

            response = YoutubeResponse(**request.execute())
            # valida que o formato da resposta do youtube ainda é o esperado

            return [
                {"text": item.snippet.topLevelComment.snippet.textOriginal}
                for item in response.items
            ]
        except HttpError as e:
            if e.resp.status == 403:  # TODO testar
                raise QuotaExceededException("YouTube")
            raise
        except PydanticValidationError as e:
            raise ExternalServiceFieldException("Youtube")
        except Exception as e:  # para capturar problemas gerais de conexão
            raise NetworkErrorException("Youtube")

    def fetch_numeric_comments(self, video_id: str) -> List[CommentType]:
        merged_comments: List[CommentType] = []

        for i in range(2):  # 0, 1, 2, ..., 9
            comments = self._search_comments(video_id, str(i))

            merged_comments.extend(comments)

        return merged_comments
