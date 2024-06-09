from langchain_community.document_loaders import DirectoryLoader, UnstructuredPDFLoader, UnstructuredFileLoader, \
    UnstructuredMarkdownLoader
from langchain_community.embeddings.sentence_transformer import (SentenceTransformerEmbeddings, )
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter

import os


class VectorStore:

    def __init__(self, sentence_transformer_model="all-MiniLM-L6-v2", persistence_directory="./db_7"):
        self.sentence_transformer = SentenceTransformerEmbeddings(model_name=sentence_transformer_model)
        self.text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        self.persistence_directory = persistence_directory

    def load_store(self) -> Chroma:

        if not os.path.exists(self.persistence_directory):
            split_documents: list[Document] = self.split_api_docs()
            
            return Chroma.from_documents(
                documents=split_documents,
                embedding=self.sentence_transformer,
                persist_directory=self.persistence_directory,
            )
        else:
            return Chroma(
                embedding_function=self.sentence_transformer,
                persist_directory=self.persistence_directory,
            )

    def split_api_docs(self) -> list[Document]:
        documents: list[Document] = DirectoryLoader("./documents/api-docs", glob="**/*.md", show_progress=True,
                                                    loader_cls=UnstructuredMarkdownLoader).load()
        return self.text_splitter.split_documents(documents)

    def split_cassandra_documents(self) -> list[Document]:
        documents: list[Document] = DirectoryLoader("./documents/cql", glob="**/*.cql", show_progress=True,
                                                    loader_cls=UnstructuredMarkdownLoader).load()
        return self.text_splitter.split_documents(documents)

    def split_markdown_documents(self) -> list[Document]:
        documents: list[Document] = DirectoryLoader("./documents/markdown", glob="**/*.md", show_progress=True,
                                                    loader_cls=UnstructuredMarkdownLoader).load()
        return self.text_splitter.split_documents(documents)

    def split_feature_documents(self) -> list[Document]:
        documents: list[Document] = DirectoryLoader("./documents/features", glob="**/*.md", show_progress=True,
                                                    loader_cls=UnstructuredFileLoader).load()
        return self.text_splitter.split_documents(documents)

    def split_pdf_documents(self) -> list[Document]:
        documents: list[Document] = DirectoryLoader('./documents/pdf', glob="**/*.pdf", show_progress=True,
                                                    loader_cls=UnstructuredPDFLoader).load()
        return self.text_splitter.split_documents(documents)
