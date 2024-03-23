from typing import Dict

from langchain.retrievers import ContextualCompressionRetriever
from langchain_community.vectorstores import Qdrant
from langchain_core.vectorstores import VectorStoreRetriever
from qdrant_client import AsyncQdrantClient, QdrantClient

from src.settings import CollectionName, settings


def create_qdrant_instance(collection_name: str) -> Qdrant:
    """
    Create a Qdrant VectorStore instance with the given collection name.
    """
    return Qdrant(
        collection_name=collection_name,
        client=QdrantClient(**settings.qdrant_args),
        async_client=AsyncQdrantClient(**settings.qdrant_args),
        embeddings=settings.app.EMBEDDING_MODEL,
    )


def create_retriever(collection_name: CollectionName) -> VectorStoreRetriever:
    """
    Create a VectorStoreRetriever instance for the given collection name.
    """
    qdrant = create_qdrant_instance(collection_name.value)
    return qdrant.as_retriever(search_kwargs={"k": 20})


def create_contextual_compression_retriever(retriever: VectorStoreRetriever) -> ContextualCompressionRetriever:
    """
    Create a ContextualCompressionRetriever instance with the given retriever.
    """
    return ContextualCompressionRetriever(
        base_compressor=settings.app.RERANKER_MODEL,
        base_retriever=retriever,
    )


def initialize_contextual_compression_retrievers() -> Dict[str, ContextualCompressionRetriever]:
    """
    Initialize and return a dictionary of ContextualCompressionRetriever instances for each collection.
    """
    contextual_compression_retrievers = {}

    for collection_name in CollectionName:
        retriever = create_retriever(collection_name)
        contextual_compression_retriever = create_contextual_compression_retriever(retriever)
        contextual_compression_retrievers[collection_name.value] = contextual_compression_retriever

    return contextual_compression_retrievers
