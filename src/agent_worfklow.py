from langchain_core.agents import AgentFinish
from langgraph.graph import END, StateGraph
from pydantic import BaseModel

from src.agent_state import AgentState


class AgentWorkflow(BaseModel):
    agent: object
    tool_executor: object

    def graph_agent(self):
        """
        This function creates a state graph for the agent workflow.
        """
        workflow = StateGraph(AgentState)
        workflow.add_node(key="Colombian Law Agent", action=self.run_agent)
        workflow.add_node(key="Tools", action=self.execute_tools)
        workflow.set_entry_point(key="Colombian Law Agent")
        workflow.add_conditional_edges(
            start_key="Colombian Law Agent",
            condition=self.should_continue,
            conditional_edge_mapping={"continue": "Tools", "end": END},
        )

        workflow.add_edge(start_key="Tools", end_key="Colombian Law Agent")
        return workflow.compile()

    async def run_agent(self, data):
        """
        This function runs the agent and returns the agent outcome.
        """
        agent_outcome = await self.agent.ainvoke(input=data)
        return {"agent_outcome": agent_outcome}

    async def execute_tools(self, data):
        """
        This function executes the tools and appends the output.
        """
        agent_action = data["agent_outcome"]
        output = await self.tool_executor.ainvoke(input=agent_action)
        return {"intermediate_steps": [(agent_action, str(output))]}

    def should_continue(self, data):
        """
        This function checks if the agent should continue or end.
        """
        if isinstance(data["agent_outcome"], AgentFinish):
            return "end"
        else:
            return "continue"
