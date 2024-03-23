from typing import List

from langchain.tools import Tool
from langchain.tools.retriever import create_retriever_tool
from langchain_community.tools.tavily_search import TavilySearchResults

from src.settings import CollectionName
from src.prompts import TOOL_DESCRIPTIONS
from src.retrievers import initialize_contextual_compression_retrievers


def initialize_tavily_tool() -> TavilySearchResults:
    """
    Initialize and return a TavilySearchResults instance.
    """
    return TavilySearchResults(
        description=TOOL_DESCRIPTIONS.get(TavilySearchResults),
    )


def initialize_retriever_tools() -> List[Tool]:
    """
    Initialize and return a list of Tool instances for each collection.
    """
    # Initialize the contextual compression retrievers for each collection
    collection_retriever_reranker_map = initialize_contextual_compression_retrievers()

    tools = []
    for collection_name in CollectionName:
        name = collection_name.value
        retriever = collection_retriever_reranker_map.get(collection_name.value)
        description = TOOL_DESCRIPTIONS.get(collection_name)

        tool = create_retriever_tool(retriever=retriever, name=name, description=description)
        tools.append(tool)

    return tools


def build_toolbelt():
    """
    Build and return a toolbelt with all the available tools.
    """
    retirever_tools = initialize_retriever_tools()
    tavily_tool = initialize_tavily_tool()

    toolbelt = [tavily_tool] + retirever_tools
    return toolbelt
