from langchain_community.document_loaders import DirectoryLoader, UnstructuredPDFLoader, UnstructuredFileLoader, \
    UnstructuredMarkdownLoader
from langchain_community.embeddings.sentence_transformer import (SentenceTransformerEmbeddings, )
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter

import os


class VectorStore:

    def __init__(self, sentence_transformer_model="all-MiniLM-L6-v2", persistence_directory="./db_9"):
        self.sentence_transformer = SentenceTransformerEmbeddings(model_name=sentence_transformer_model)
        self.text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        self.persistence_directory = persistence_directory

    def load_store(self) -> Chroma:
        if not os.path.exists(self.persistence_directory):
            split_documents: list[Document] = self.split_documents()

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

    def split_documents(self) -> list[Document]:
        split_documents: list[Document] = []
        split_documents.extend(self.split_api_docs())
        # split_documents.extend(self.split_cassandra_documents())
        split_documents.extend(self.split_high_level_documents())
        split_documents.extend(self.split_feature_documents())
        return split_documents

    def split_api_docs(self) -> list[Document]:
        documents: list[Document] = DirectoryLoader("./documents/api_docs", glob="**/*.md", show_progress=True,
                                                    loader_cls=UnstructuredMarkdownLoader).load()
        return self.text_splitter.split_documents(documents)

    def split_cassandra_documents(self) -> list[Document]:
        documents: list[Document] = DirectoryLoader("./documents/cql", glob="**/*.cql", show_progress=True,
                                                    loader_cls=UnstructuredMarkdownLoader).load()
        return self.text_splitter.split_documents(documents)

    def split_high_level_documents(self) -> list[Document]:
        split_documents: list[Document] = []
        markdown: list[Document] = DirectoryLoader("./documents/high_level_docs", glob="**/*.md", show_progress=True,
                                                   loader_cls=UnstructuredMarkdownLoader).load()
        pdf: list[Document] = DirectoryLoader('./documents/high_level_docs', glob="**/*.pdf", show_progress=True,
                                              loader_cls=UnstructuredPDFLoader).load()
        split_documents.extend(self.text_splitter.split_documents(markdown))
        split_documents.extend(self.text_splitter.split_documents(pdf))
        return split_documents

    def split_feature_documents(self) -> list[Document]:
        documents: list[Document] = DirectoryLoader("./documents/cucumber_feature_files", glob="**/*.md",
                                                    show_progress=True,
                                                    loader_cls=UnstructuredFileLoader).load()
        return self.text_splitter.split_documents(documents)
