from langchain_community.document_loaders import DirectoryLoader, UnstructuredPDFLoader, UnstructuredFileLoader, \
    UnstructuredMarkdownLoader
from langchain_community.embeddings.sentence_transformer import (SentenceTransformerEmbeddings, )
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter
from ragatouille import RAGPretrainedModel
from langchain.retrievers import ContextualCompressionRetriever
from ragatouille import RAGPretrainedModel

import os


class VectorStore:

    def __init__(self, sentence_transformer_model="all-MiniLM-L6-v2", persistence_directory="./db_9"):
        self.sentence_transformer = SentenceTransformerEmbeddings(model_name=sentence_transformer_model)
        self.text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        self.persistence_directory = persistence_directory

    def load_store(self) -> ContextualCompressionRetriever:
        index_name = "Combined-Docs"
        index_path = f".ragatouille/colbert/indexes/{index_name}"
        if not os.path.exists(index_path):
            RAG = RAGPretrainedModel.from_pretrained("colbert-ir/colbertv2.0")
            documents = DirectoryLoader("./documents/high_level_docs", glob="**/*.md", show_progress=True,
                                        loader_cls=UnstructuredMarkdownLoader).load()
            apidocs = DirectoryLoader("./documents/api_docs", glob="**/*.md", show_progress=True,
                                      loader_cls=UnstructuredMarkdownLoader).load()
            features = DirectoryLoader("./documents/cucumber_feature_files", glob="**/*.md", show_progress=True,
                                       loader_cls=UnstructuredMarkdownLoader).load()
            pdf_docs = DirectoryLoader('./documents/high_level_docs', glob="**/*.pdf", show_progress=True,
                                       loader_cls=UnstructuredPDFLoader).load()
            all_documents = []
            # Extract the text from the loaded documents
            documents_text = [doc.page_content for doc in documents]
            apidocs_text = [doc.page_content for doc in apidocs]
            features_text = [doc.page_content for doc in features]
            pdf_docs_text = [doc.page_content for doc in pdf_docs]
            all_documents.extend(documents_text)
            all_documents.extend(apidocs_text)
            all_documents.extend(features_text)
            all_documents.extend(pdf_docs_text)
            RAG.index(
                collection=all_documents,
                index_name=index_name,
                max_document_length=512,
                split_documents=True,
            )
        else:
            RAG = RAGPretrainedModel.from_index(index_path)

        retriever = RAG.as_langchain_retriever()
        compression_retriever = ContextualCompressionRetriever(
            base_compressor=RAG.as_langchain_document_compressor(), base_retriever=retriever
        )
        return compression_retriever

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
