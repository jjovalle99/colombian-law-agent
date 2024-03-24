# Colombian Law Agent

## Stages

### Data Collection & Preparation
Since there were no updated PDFs available for the law sources of interest, I needed to scrape the information from the original sources. For this scraping process, I used Browserless, which was essential for accessing content that only appeared after interactive elements were triggered. This approach was crucial for capturing additional relevant information. Once the HTML files were obtained, I utilized BeautifulSoup to extract and retain only the pertinent text from the HTML documents. Subsequently, DVC, with an S3 bucket set as a remote storage, was employed for version control of the data. Interested in the code? See [link1](link1) and [link2](link2).

### Retrievers (RAGs)
For the retrievers, I employed Qdrant to host a database where the information from each relevant law source was stored in distinct collections. This structure facilitated the creation of a suite of retrievers, each specialized in a different data source. To enhance the retrieval process, I integrated the Cohere Multilingual Reranker with each retriever to improve the results. Once the retriever-reranker setup was finalized, they were adapted into OpenAI functions using LangChain, making them ready for the Agent. Additionally, a Tavily search engine tool was added to the toolkit to address scenarios where the retrievers were insufficient. Interested in the code? See [link1](link1) and [link2](link2).

### App Building
The app-building process began with drafting the entire workflow in a Jupyter Notebook. I developed different types of agents using a combination of LangChain, LangSmith, and Langgraph:
- One-direction Agent
- Cyclic Agent
- Cyclic AgentExecutor (i.e., enabling chat history)

Subsequently, I performed a quick local deployment of the last Agent type mentioned using LangServe to verify if the endpoint would exhibit the expected behavior. Interested in the code? See [link1](link1) and [link2](link2).

### UI
I constructed a basic UI for the endpoint using Streamlit. This UI facilitates simple calls without chat history. However, the Agent endpoint is designed to support chat history for those interested in utilizing it.

### Deployment
I adopted a microservices architecture for the deployment, wherein the UI and the Agent endpoint were deployed independently. These deployments were serverless, executed through the convenient Modal Python package, eliminating the need for Dockerfiles or direct interaction with cloud providers.

## Tech Stack

The following technologies were utilized to build this app:

| Component                      | Stack                                               |
| ------------------------------ | --------------------------------------------------- |
| Data Collection & Preparation  | Browserless, BeautifulSoup, DVC, Amazon S3          |
| Retrievers (RAGs)              | Qdrant Vector Database, Cohere Reranker             |
| App Building                   | LangChain, LangSmith, LangGraph, LangServe, Tavily  |
| UI                             | Streamlit                                           |
| Deployment                     | Modal                                               |



## Deploy Agent Endpoint
```bash
modal deploy app/app.py
```

## Deploy UI
```bash
modal deploy ui/serve_streamlit.py
```

## Create and populate Qdrant Collections
```python
python scripts/create_qdrant_collections.py \
    --collection_name "constitucion" \
    --folder "data/constitucion/text/" \
    --doc_name "Constitución Política de la República de Colombia" \
    --llm "gpt-4-turbo-preview" \
    --embedding_model "text-embedding-3-large" 

python scripts/create_qdrant_collections.py \
    --collection_name "codigo_penal" \
    --folder "data/codigo_penal/text/" \
    --doc_name "Código Penal - LEY 599 DE 2000" \
    --llm "gpt-4-turbo-preview" \
    --embedding_model "text-embedding-3-large" 

python scripts/create_qdrant_collections.py \
    --collection_name "codigo_general_del_proceso" \
    --folder "data/codigo_general_del_proceso/text/" \
    --doc_name "Código General del Proceso - LEY 1564 DE 2012" \
    --llm "gpt-4-turbo-preview" \
    --embedding_model "text-embedding-3-large" 

python scripts/create_qdrant_collections.py \
    --collection_name "codigo_civil" \
    --folder "data/codigo_civil/text/" \
    --doc_name "Código Civil - LEY 84 DE 1873" \
    --llm "gpt-4-turbo-preview" \
    --embedding_model "text-embedding-3-large" 

python scripts/create_qdrant_collections.py \
    --collection_name "codigo_sustantivo_trabajo" \
    --folder "data/codigo_sustantivo_trabajo/text/" \
    --doc_name "Código Sustantivo del Trabajo" \
    --llm "gpt-4-turbo-preview" \
    --embedding_model "text-embedding-3-large"

python scripts/create_qdrant_collections.py \
    --collection_name "codigo_procedimental_laboral" \
    --folder "data/codigo_procedimental_laboral/text/" \
    --doc_name "Codigo Procesal Laboral" \
    --llm "gpt-4-turbo-preview" \
    --embedding_model "text-embedding-3-large" 

python scripts/create_qdrant_collections.py \
    --collection_name "codigo_comercio" \
    --folder "data/codigo_comercio/text/" \
    --doc_name "Código de Comercio" \
    --llm "gpt-4-turbo-preview" \
    --embedding_model "text-embedding-3-large" 
```
