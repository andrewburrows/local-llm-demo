from langchain.prompts import ChatPromptTemplate
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.schema import Document
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.vectorstores import VectorStoreRetriever
import numpy as np
from langchain_community.embeddings import OllamaEmbeddings

from llm.context_retrieval.context_retriever import ContextRetriever
from operator import itemgetter

"""
Re-rank multi-query retrieved documents based on the cosine similarity with the original input.
"""


class CosineSimilarityRerank(ContextRetriever):
    def __init__(self, retriever: VectorStoreRetriever, multi_query_request: str):
        super().__init__(retriever)
        self.multi_query_request = multi_query_request
        self.embeddings = OllamaEmbeddings(model="llama3")  # Initialize the embeddings model

    def query_context_chain(self):
        prompt_rag_fusion = ChatPromptTemplate.from_template(self.multi_query_request)

        def print_queries(queries: list[str]):
            print("-----| QUERIES GENERATED FOR RAG |-----")
            for query in queries:
                print(f"{query}")
            return queries

        def extract_question(prompt: ChatPromptTemplate) -> str:
            question_placeholder = "{question}"
            template = prompt.messages[0].prompt.template
            start_index = template.find(question_placeholder)
            if start_index != -1:
                end_index = start_index + len(question_placeholder)
                return template[start_index:end_index]
            return ""

        question = extract_question(prompt_rag_fusion)

        def remove_empty(queries: list[str]):
            return [query.strip() for query in queries if query.strip()]

        generate_queries = (
                prompt_rag_fusion
                | ChatOllama(model="llama3")
                | StrOutputParser()
                | (lambda x: x.split("\n"))
                | remove_empty
        )

        def deduplicate(documents: list[(Document, float)]) -> list[(Document, float)]:
            unique_docs = {}
            deduplicated_docs = []

            for doc, score in documents:
                content = doc.page_content
                if content not in unique_docs:
                    unique_docs[content] = (doc, score)
                    deduplicated_docs.append((doc, score))
                else:
                    existing_doc, existing_score = unique_docs[content]
                    if score > existing_score:
                        unique_docs[content] = (doc, score)
                        deduplicated_docs = [(d, s) for d, s in deduplicated_docs if d != existing_doc] + [(doc, score)]

            return deduplicated_docs

        def generate_responses(queries: list[str]) -> list[(Document, float)]:
            documents = []
            question_embedding = self.embeddings.embed_query(question)  # Embed the original question
            for query in queries:
                docs_with_scores = self.retriever.similarity_search_with_relevance_scores(query=query, k=4)
                print(f"\nDocuments retrieved for '{query}'")
                for doc, score in docs_with_scores:
                    print(f"score: {score}, doc: {doc}")
                for doc, score in docs_with_scores:
                    doc_embedding = self.embeddings.embed_query(doc.page_content)  # Embed the document content
                    relevance_score = np.dot(question_embedding, doc_embedding)  # Calculate the semantic similarity
                    documents.append((doc, relevance_score))

            return documents

        return generate_queries | print_queries | generate_responses | deduplicate | self._reciprocal_rank_fusion

    def _reciprocal_rank_fusion(self, retrieved_documents: list[(Document, float)]):
        sorted_documents = sorted(retrieved_documents, key=lambda document: document[1])
        print(f"-----| Documents retrieved |-----")
        for document, score in retrieved_documents:
            print(f"{score}: {document}")
        if len(sorted_documents) > 6:
            response = [page_content for page_content, _ in sorted_documents[:6]]
        else:
            response = [page_content for page_content, _ in sorted_documents]
        print(f"-----| Filtered ranked results |-----")
        print(response)
        return response
