from typing import List

from langchain.pydantic_v1 import BaseModel
from langchain_core.messages import BaseMessage


class Input(BaseModel):
    input: str
    chat_history: List[BaseMessage]
