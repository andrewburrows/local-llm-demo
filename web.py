from operator import itemgetter

import chainlit as cl
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable.config import RunnableConfig
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.vectorstores import VectorStoreRetriever

from llm.config_loader import load_yaml
from llm.context_retrieval.context_retriever_factory import ContextRetrieverFactory
from llm.vector_store import VectorStore


config: dict = load_yaml('llm-config.yml')
vector_store = VectorStore()
retriever = vector_store.load_store()
context_retriever = ContextRetrieverFactory(config).create_context_retriever(retriever)

@cl.on_chat_start
async def on_chat_start():
    prompt = ChatPromptTemplate.from_template(config['llm-query-template'])
    final_rag_chain = (
            {"context": context_retriever.query_context_chain(),
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
