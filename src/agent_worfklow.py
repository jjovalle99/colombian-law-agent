from langchain_core.agents import AgentFinish
from langgraph.graph import END, StateGraph

from src.agent_state import AgentState


def graph_agent():
    """
    This function creates a state graph for the agent workflow.
    """
    workflow = StateGraph(AgentState)
    workflow.add_node(key="agent", action=run_agent)
    workflow.add_node(key="action", action=execute_tools)
    workflow.set_entry_point(key="agent")
    workflow.add_conditional_edges(
        start_key="agent", condition=should_continue, conditional_edge_mapping={"continue": "action", "end": END}
    )

    workflow.add_edge(start_key="action", end_key="agent")
    return workflow.compile()


async def run_agent(data):
    """
    This function runs the agent and returns the agent outcome.
    """
    global agent
    agent_outcome = await agent.ainvoke(input=data)
    return {"agent_outcome": agent_outcome}


async def execute_tools(data):
    """
    This function executes the tools and appends the output.
    """
    global tool_executor
    agent_action = data["agent_outcome"]
    output = await tool_executor.ainvoke(input=agent_action)
    return {"intermediate_steps": [(agent_action, str(output))]}


def should_continue(data):
    """
    This function checks if the agent should continue or end.
    """
    if isinstance(data["agent_outcome"], AgentFinish):
        return "end"
    else:
        return "continue"
