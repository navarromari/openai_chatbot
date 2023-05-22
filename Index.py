from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, LLMPredictor, PromptHelper, ServiceContext
from langchain import OpenAI

##Construct index function

def construct_index(directory_path):
    # set maximum input size
    max_input_size = 4096
    # set number of output tokens
    num_outputs = 256
    # set maximum chunk overlap
    max_chunk_overlap = 20
    # set chunk size limit
    chunk_size_limit = 600

    # define LLM
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.3, model_name="text-davinci-003", max_tokens=num_outputs))
    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)
 
    # load documents
    documents = SimpleDirectoryReader(directory_path).load_data()
    
    index = GPTVectorStoreIndex.from_documents(
    documents, service_context=service_context
)

    index.storage_context.persist(persist_dir='index.json')

    return index


##Calling construct_index with reddit data
if __name__ == '__main__':
  construct_index('/content/textdata')