from enum import Enum
from typing import List

from langchain.retrievers.document_compressors import CohereRerank
from langchain_openai.chat_models import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
from pydantic_settings import BaseSettings


class CollectionName(Enum):
    CODIGO_CIVIL = "codigo_civil"
    CODIGO_PROCEDIMENTAL_LABORAL = "codigo_procedimental_laboral"
    CODIGO_PENAL = "codigo_penal"
    CODIGO_SUSTANTIVO_DEL_TRABAJO = "codigo_sustantivo_trabajo"
    CODIGO_GENERAL_DEL_PROCESO = "codigo_general_del_proceso"
    CODE_COMERICO = "codigo_comercio"
    CONSTITUCION = "constitucion"


class EnvironmentSettings(BaseSettings):
    LANGCHAIN_TRACING_V2: str
    LANGCHAIN_PROJECT: str
    LANGCHAIN_API_KEY: str
    BROWSERLESS_API_KEY: str
    QDRANT__URL: str
    QDRANT__API_KEY: str
    OPENAI_API_KEY: str
    COHERE_API_KEY: str
    TAVILY_API_KEY: str

    class Config:
        env_file = ".env"


class AppSettings(BaseSettings):
    COLLECTION_NAMES: List[CollectionName] = list(CollectionName)

    @property
    def LLM_MODEL(self) -> ChatOpenAI:
        return ChatOpenAI(model="gpt-4-turbo-preview", temperature=0)

    @property
    def EMBEDDING_MODEL(self) -> OpenAIEmbeddings:
        return OpenAIEmbeddings(model="text-embedding-3-large")

    @property
    def RERANKER_MODEL(self) -> CohereRerank:
        return CohereRerank(model="rerank-multilingual-v2.0", top_n=5)


class Settings(BaseSettings):
    env: EnvironmentSettings = EnvironmentSettings()
    app: AppSettings = AppSettings()

    @property
    def qdrant_args(self):
        return {
            "url": self.env.QDRANT__URL,
            "api_key": self.env.QDRANT__API_KEY,
            "prefer_grpc": True,
        }


settings = Settings()
