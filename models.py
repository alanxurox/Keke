from typing import List
from datetime import datetime
from pydantic import BaseModel, Field


class MessageRecord(BaseModel):
    """A message record in the group chat.

    Attributes:
        sender: The ID of the message sender
        message: The content of the message
        timestamp: When the message was sent
        receivers: List of agent IDs mentioned in the message, must be "human" or "system" or a valid agent ID
        readers: List of agent IDs that have read the message
    """
    sender: str
    message: str
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())
    receivers: List[str] = Field(default_factory=list)
    readers: List[str] = Field(default_factory=list)

    class Config:
        arbitrary_types_allowed = True
