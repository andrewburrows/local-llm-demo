from langchain.load import dumps
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.vectorstores import VectorStoreRetriever

from llm.context_retrieval.context_retriever import ContextRetriever, template_multiquery


class ReciprocalRankFusion(ContextRetriever):

    def __init__(self, retriever: VectorStoreRetriever, multi_query_request: str):
        super().__init__(retriever)
        self.multi_query_request = multi_query_request

    def query_context_chain(self):
        prompt_rag_fusion = ChatPromptTemplate.from_template(self.multi_query_request)

        def print_queries(queries: list[str]):
            print("QUERIES GENERATED FOR RAG:")
            for query in queries:
                print(f"{query}")
            return queries

        def remove_empty(queries: list[str]):
            return [query.strip() for query in queries if query.strip()]

        generate_queries = (
                prompt_rag_fusion
                | ChatOllama(model="llama3")
                | StrOutputParser()
                | (lambda x: x.split("\n"))
                | remove_empty
                | print_queries
        )
        return generate_queries | self.retriever.map() | self._reciprocal_rank_fusion

    def _reciprocal_rank_fusion(self, retrieved_documents: list[list[Document]], base_rank=60):
        fused_ranked_scores = {}
        for documents in retrieved_documents:
            for rank, doc in enumerate(documents):
                document_as_json = dumps(doc)
                if document_as_json not in fused_ranked_scores:
                    fused_ranked_scores[document_as_json] = 0
                fused_ranked_scores[document_as_json] += 1 / (rank + base_rank)
        sorted_ranked_results = [(doc, score) for doc, score in sorted(fused_ranked_scores.items(),
                                                                       key=lambda x: x[1],
                                                                       reverse=True)]
        if len(sorted_ranked_results) > 2:
            return [doc for doc, _ in sorted_ranked_results[:2]]
        else:
            return [doc for doc, _ in sorted_ranked_results]
