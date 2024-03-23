from typing import List

from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.agents import AgentAction
from langchain_core.messages import BaseMessage


class Input(BaseModel):
    input: str = ""
    chat_history: List[BaseMessage] = Field(default_factory=list)
    intermediate_steps: List[tuple[AgentAction, str]] = Field(default_factory=list)


class Output(BaseModel):
    output: str
