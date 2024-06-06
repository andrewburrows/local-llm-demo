import asyncio
import chainlit as cl
from langchain_community.document_loaders import DirectoryLoader, UnstructuredPDFLoader
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_community.embeddings.sentence_transformer import (SentenceTransformerEmbeddings, )
from langchain_community.vectorstores import Chroma
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


@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("answerer", rag_llm)


@cl.on_message
async def on_message(message: cl.Message):
    answerer = cl.user_session.get("answerer")
    msg = cl.Message(content="")

    async def generate_chunks(question):
        response = answerer.generate_answer(question)
        yield response

    async for chunk in generate_chunks(message.content):
        await msg.stream_token(chunk)
        await asyncio.sleep(0.01)
    await msg.send()
