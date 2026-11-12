#pydantic schema
from datetime import datetime
from enum import Enum
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, StringConstraints

class FlairEnum(str,Enum):
    bug = 'bug'
    feature = 'feature'
    question = 'question'
    docs =  'docs'

class TicketCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    project: str = Field(min_length=1, max_length=60)
    title: str = Field(min_length=1, max_length=120)
    description: str | None = Field(default=None, max_length=2000)
    author: str = Field(min_length=1, max_length=50)
    flair: FlairEnum

class TicketPatch(BaseModel):
    is_resolved: bool


class TicketOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    project: str
    title: str
    description: str | None
    author: str
    flair: FlairEnum
    is_resolved: bool
    created_at: datetime