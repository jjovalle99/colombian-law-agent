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



{
  "input": {
    "input": "Que significa la territorialidad en el ambito penal?",
    "chat_history": [],
    "agent_outcome": {
      "tool": "string",
      "tool_input": "string",
      "log": "string",
      "type": "AgentAction"
    },
    "intermediate_steps": []
  },
  "config": {},
  "kwargs": {}
}