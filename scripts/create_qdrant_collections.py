import argparse
import asyncio
import glob
import json
import os
import re
from typing import List

from dotenv import load_dotenv
from langchain.schema import Document
from langchain_community.vectorstores import Qdrant
from langchain_openai.embeddings import OpenAIEmbeddings
from qdrant_client import QdrantClient, AsyncQdrantClient, models
from langchain_text_splitters import CharacterTextSplitter
from tiktoken import encoding_for_model

# Load environment variables
load_dotenv()

# Define model dimensions for easy reference and validation
MODEL_DIMENSIONS = {
    "text-embedding-3-small": 1536,
    "text-embedding-3-large": 3072,
}


def parse_arguments() -> argparse.Namespace:
    """
    Parse command line arguments.

    Returns:
        argparse.Namespace: Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(description="Upload chunks of text data to Qdrant.")
    parser.add_argument("--folder", type=str, required=True, help="The folder containing the text data.")
    parser.add_argument("--doc_name", type=str, required=True, help="The name of the document.")
    parser.add_argument(
        "--collection_name", type=str, required=True, help="The name of the collection to create in Qdrant."
    )
    parser.add_argument(
        "--llm",
        type=str,
        required=True,
        help="LLM name for tiktoken encoding. ",
    )
    parser.add_argument(
        "--embedding_model",
        type=str,
        required=True,
        choices=list(MODEL_DIMENSIONS.keys()),
        help="The name of the embedding model to use.",
    )
    return parser.parse_args()


def load_documents(folder: str, doc_name: str, metadata_file: str = "metadata.json") -> List[Document]:
    """
    Prepare documents from text files and metadata.

    Args:
        folder (str): Folder containing text files and metadata.
        doc_name (str): Name of the document.
        metadata_file (str): Filename of the metadata JSON file.

    Returns:
        List[Document]: List of Document objects ready for embedding and storage.
    """
    with open(os.path.join(folder, metadata_file), "r") as f:
        metadata = json.load(f)

    file_list = sorted(glob.glob(f"{folder}/*.txt"), key=lambda x: int(re.search(r"\d+", x).group()))

    docs = []
    for file in file_list:
        with open(file, "r") as f:
            content = f.read()
            file_name = os.path.basename(file)
            docs.append(Document(page_content=content, metadata={"source": doc_name, "url": metadata.get(file_name)}))
    return docs


def prepare_documents(documents: List[Document], model_name: str) -> List[Document]:
    """
    Split documents into chunks.
    Args:
        documents (List[Document]): List of Document objects.
        model_name (str): Name of the model to use for encoding.
    """
    text_splitter = CharacterTextSplitter(
        separator="\n\n\n",
        chunk_size=100,
        chunk_overlap=0,
        keep_separator=False,
        length_function=lambda x: len(encoding_for_model(model_name=model_name).encode(x)),
        is_separator_regex=False,
    )

    return text_splitter.split_documents(documents=documents)


async def main(collection_name: str, llm: str, embedding_model: str, folder: str, doc_name: str) -> None:
    """
    Main function to process documents and upload them to Qdrant.

    Args:
        collection_name (str): Name of the collection in Qdrant.
        llm (str): LLM name for tiktoken encoding.
        embedding_model (str): Embedding model to use for document vectors.
        folder (str): Folder containing text data.
        doc_name (str): Name of the document.
    """
    client = AsyncQdrantClient(url=os.getenv("QDRANT__URL"), api_key=os.getenv("QDRANT__API_KEY"), prefer_grpc=True)

    if not await client.collection_exists(collection_name=collection_name):
        await client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(size=MODEL_DIMENSIONS[embedding_model], distance=models.Distance.COSINE),
        )

    documents = load_documents(folder=folder, doc_name=doc_name)
    documents = prepare_documents(documents=documents, model_name=llm)
    embeddings = OpenAIEmbeddings(model=embedding_model)

    vector_store = Qdrant(
        client=QdrantClient(url=os.getenv("QDRANT__URL"), api_key=os.getenv("QDRANT__API_KEY"), prefer_grpc=True),
        async_client=client,
        collection_name=collection_name,
        embeddings=embeddings,
    )

    await vector_store.aadd_documents(documents=documents)


if __name__ == "__main__":
    args = parse_arguments()
    asyncio.run(
        main(
            collection_name=args.collection_name,
            embedding_model=args.embedding_model,
            llm=args.llm,
            folder=args.folder,
            doc_name=args.doc_name,
        )
    )
