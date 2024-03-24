from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain.agents import create_openai_functions_agent
from langgraph.prebuilt import ToolExecutor
from langserve import add_routes

from src.agent_worfklow import AgentWorkflow
from src.prompts import prepare_legal_colombia_agent_prompt
from src.schemas import Input
from src.settings import settings
from src.tools import build_toolbelt

app = FastAPI(
    title="Legal Colombia Cycle Agent",
    version="1.0",
    description="Agent with colombian legal sources as tools.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


agent = create_openai_functions_agent(
    llm=settings.app.LLM_MODEL,
    tools=build_toolbelt(),
    prompt=prepare_legal_colombia_agent_prompt(),
)
tool_executor = ToolExecutor(tools=build_toolbelt())
workflow = AgentWorkflow(agent=agent, tool_executor=tool_executor)
runnable = workflow.graph_agent()

add_routes(
    app=app,
    runnable=runnable,
    path="/agent",
    input_type=Input,
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="local_app:app", host="localhost", port=8000, reload=True)
