from operator import itemgetter

import chainlit as cl
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable.config import RunnableConfig
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser

from rag_llm import RagLLm
from vector_store import VectorStore

vector_store = VectorStore()
retriever = vector_store.load_store()
rag_llm = RagLLm(retriever)

template_question = """Answer the following question based on this context:

        {context}

        Question: {question}
        """


@cl.on_chat_start
async def on_chat_start():
    prompt = ChatPromptTemplate.from_template(template_question)
    final_rag_chain = (
            {"context": rag_llm.retrieval_chain(),
             "question": itemgetter("question")}
            | prompt
            | ChatOllama(model="llama3")
            | StrOutputParser()
    )
    cl.user_session.set("answerer", final_rag_chain)


@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("answerer")
    msg = cl.Message(content="")
    async for chunk in runnable.astream(
            {"question": message.content},
            config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)
    await msg.send()
