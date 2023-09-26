from pydantic import BaseModel, Field
from typing import List


class CommentSnippet(BaseModel):
    textOriginal: str = Field(...)


class TopLevelComment(BaseModel):
    snippet: CommentSnippet = Field(...)


class Snippet(BaseModel):
    topLevelComment: TopLevelComment = Field(...)


class Item(BaseModel):
    snippet: Snippet = Field(...)


class YoutubeResponse(BaseModel):
    items: List[Item] = Field(...)
