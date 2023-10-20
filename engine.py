import os
from llama_index import SimpleDirectoryReader, StorageContext, VectorStoreIndex, load_index_from_storage
import openai


openai.api_key="your_api_key"

# Embedding
# check if index exist
if not os.path.exists("index_data"):
    # Step 1: Read the data

    documents = SimpleDirectoryReader("data").load_data()
    
    # step 2: Create an index from the document (Vector Embedding)
    index = VectorStoreIndex.from_documents(documents)
    
    # step 3: Save the index
    index.storage_context.persist("index_data")



# load the index
storage_context = StorageContext.from_defaults(persist_dir="index_data")

index = load_index_from_storage(storage_context)

# create the engine with the index
query_engine = index.as_query_engine(streaming=True)


# define a function which will take the prompt from user and use the engine to return the output
def get_response(prompt):
    response = query_engine.query(prompt)
    return response