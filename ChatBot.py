from IPython.display import Markdown, display
from llama_index import GPTListIndex, readers, QuestionAnswerPrompt, StorageContext, load_index_from_storage

##Chatbot interation function
def ask_spooky():

    # rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir='index.json')

    # load index
    index = load_index_from_storage(storage_context)
    
    while True: 
        query_str = input("say something:")
        
        QA_PROMPT_TMPL = (
        "You are Spooky, a storyteller bot with a penchant for horror tales. Your primary objective is to narrate personalized horror stories, utilizing the information provided by users. As the storyteller, your role is to present each tale as a well-known story you've encountered before, employing a formal language and a third-person perspective. Your task includes adapting the plot and details of the story to make it relevant and relatable to the user's situation. Furthermore, you should be ready to respond to any questions the user may have regarding the stories you share.\n"
        "---------------------\n"
        "{context_str}"
        "\n---------------------\n"
        "Given this information, please answer the question: {query_str}\n"
        )   

        QA_PROMPT = QuestionAnswerPrompt(QA_PROMPT_TMPL)

        query_engine = index.as_query_engine(text_qa_template=QA_PROMPT)
        
        response = query_engine.query(query_str)
        
        display(Markdown(f"Bot says: <b>{response}</b>"))
        

if __name__ == '__main__':
    ask_spooky()