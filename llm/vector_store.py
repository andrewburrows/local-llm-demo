from langchain_community.document_loaders import DirectoryLoader, UnstructuredPDFLoader
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_community.embeddings.sentence_transformer import (SentenceTransformerEmbeddings, )
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_text_splitters import CharacterTextSplitter


class VectorStore:

    def __init__(self, sentence_transformer_model="all-MiniLM-L6-v2"):
        self.sentence_transformer = SentenceTransformerEmbeddings(model_name=sentence_transformer_model)
        self.text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

    def load_store(self) -> VectorStoreRetriever:
        split_documents: list[
            Document] = self.split_markdown_documents() + self.split_feature_documents() + self.split_pdf_documents() + self.split_api_docs()
        vectorstore = Chroma.from_documents(documents=split_documents,
                                            embedding=self.sentence_transformer,
                                            persist_directory="./db5")
        return vectorstore.as_retriever()

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
        documents: list[Document] = DirectoryLoader("./documents/markdown", glob="**/*.md", show_progress=True,
                                                    loader_cls=UnstructuredMarkdownLoader).load()
        return self.text_splitter.split_documents(documents)

    def split_pdf_documents(self) -> list[Document]:
        documents: list[Document] = DirectoryLoader('./documents/pdf', glob="**/*.pdf", show_progress=True,
                                                    loader_cls=UnstructuredPDFLoader).load()
        return self.text_splitter.split_documents(documents)
