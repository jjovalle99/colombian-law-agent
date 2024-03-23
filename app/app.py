from fastapi import FastAPI
from langchain.agents import create_openai_functions_agent
from langchain_core.runnables import RunnableLambda
from langgraph.prebuilt import ToolExecutor
from langserve import add_routes
import logging

from src.agent_worfklow import AgentWorkflow
from src.prompts import prepare_legal_colombia_agent_prompt
from src.schemas import Input, Output
from src.settings import settings
from src.tools import build_toolbelt

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

agent = create_openai_functions_agent(
    llm=settings.app.LLM_MODEL,
    tools=build_toolbelt(),
    prompt=prepare_legal_colombia_agent_prompt(),
)
tool_executor = ToolExecutor(tools=build_toolbelt())
workflow = AgentWorkflow(agent=agent, tool_executor=tool_executor)
graph_agent = workflow.graph_agent()


app = FastAPI(
    title="Legal-Colombia-Cycle-Agent",
    version="1.0",
    description="Agent with colombian legal sources as tools.",
)


def inp(state: dict):
    return state
    

def out(state: dict):
    return state

chain =  RunnableLambda(inp) | graph_agent | RunnableLambda(out)

add_routes(
    app=app,
    runnable=chain,
    path="/agent",
    input_type=Input,
    # disabled_endpoints=["stream_log"]
    # output_type=Output,
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="app:app", host="localhost", port=8000, reload=True)
