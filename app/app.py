import modal
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

image = modal.Image.debian_slim(python_version="3.11") \
    .poetry_install_from_file(
        poetry_pyproject_toml="pyproject.toml",
        poetry_lockfile="poetry.lock",
        only=["main"]
    )

stub = modal.Stub(
    name="legal-colombia-agent",
    image=image,
    secrets=[modal.Secret.from_name(label="legal-colombia-agent")],
)

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


@stub.function(mounts=[modal.Mount.from_local_python_packages("src")])
@modal.asgi_app()
def serve():
    from langchain.agents import create_openai_functions_agent
    from langgraph.prebuilt import ToolExecutor
    from langserve import add_routes

    from src.agent_worfklow import AgentWorkflow
    from src.prompts import prepare_legal_colombia_agent_prompt
    from src.schemas import Input
    from src.settings import settings
    from src.tools import build_toolbelt

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

    return app
