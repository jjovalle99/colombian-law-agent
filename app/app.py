from fastapi import FastAPI

from langchain.agents import create_openai_functions_agent
from langgraph.prebuilt import ToolExecutor

from src.agent_worfklow import graph_agent
from src.prompts import prepare_legal_colombia_agent_prompt
from src.settings import settings
from src.tools import build_toolbelt
from langserve import add_routes

agent = create_openai_functions_agent(
    llm=settings.app.LLM_MODEL,
    tools=build_toolbelt(),
    prompt=prepare_legal_colombia_agent_prompt(),
)
tool_executor = ToolExecutor(tools=build_toolbelt())
graph_agent = graph_agent()


app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces",
)

add_routes(
    app=app,
    runnable=graph_agent,
    path="/agent",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="serve:app", host="localhost", port=8000, reload=True)
