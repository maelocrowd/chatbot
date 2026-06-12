from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough, RunnableParallel
from langchain_core.documents import Document
import model, context

def make_context_string(dict_with_docs: dict[str, Document]) -> str:
    """
    Takes the contents of each Document object in a dictionary and joins them
    in one string, separated by two newlines
    
    :param dict_with_docs: The dictionary with the context docs under the key
                           "context_docs"
    :type dict_with_docs: dict[str, Document]
    :returns: The combined string
    :rtype: str
    """
    return "\n\n".join(doc.page_content for doc in dict_with_docs["context_docs"])

def answer_and_sources(question: str) -> dict[str, str]:
    """
    Invokes the model with the given question.
    
    :param question: The question to ask.
    :returns: Dictionary with the answer and supporting sources
    """
    result = chain_with_sources.invoke(question)
    response_text = result["answer"].content
    sources = "\n\n".join(f"{doc.metadata['source']}, page {doc.metadata['page']}" for doc in result["context_docs"])
    return {"answer": response_text,
            "sources": sources}

prompt_template = ChatPromptTemplate([
     ("human", "You are an assistant\n"
        "providing answers to questions\n"
        "about the theater. In addition to\n"
        "your training data, you are to\n"
        "use the additional context\n"
        "provided below to provide\n"
        "up-to-date information."),
    ("human", "Question:{question}\nContext:{context}")])

retriever = context.get_vector_store().as_retriever()
question_and_docs = RunnableParallel(
    { "question": RunnablePassthrough(),
      "context_docs": retriever }
)
context = RunnablePassthrough.assign(context=make_context_string)
model = model.get_model()
answer_chain = context | prompt_template | model
chain_with_sources = question_and_docs.assign(answer=answer_chain)