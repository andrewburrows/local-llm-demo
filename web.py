from operator import itemgetter

import chainlit as cl
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable.config import RunnableConfig
from langchain_community.chat_models import ChatOllama
from langchain_community.document_loaders import DirectoryLoader, UnstructuredPDFLoader
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_community.embeddings.sentence_transformer import (SentenceTransformerEmbeddings, )
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import CharacterTextSplitter

from rag_llm import RagLLm

loader = DirectoryLoader("./documents/markdown", glob="**/*.md", show_progress=True, loader_cls=UnstructuredFileLoader)
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
pdf_loader = DirectoryLoader('./documents/pdf', glob="**/*.pdf", show_progress=True, loader_cls=UnstructuredPDFLoader)
pdf_docs = pdf_loader.load()
pdf_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
split_docs = text_splitter.split_documents(documents) + pdf_splitter.split_documents(pdf_docs)
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(documents=split_docs,
                                    embedding=embedding_function,
                                    persist_directory="./db")
retriever = vectorstore.as_retriever()
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
