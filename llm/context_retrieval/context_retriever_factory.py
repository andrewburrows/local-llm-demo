
from langchain_core.vectorstores import VectorStoreRetriever
from llm.context_retrieval.context_retriever import ContextRetriever
from llm.context_retrieval.context_retrievers.cosine_similarity_rerank import CosineSimilarityRerank
from llm.context_retrieval.context_retrievers.reciprocal_rank_fusion import ReciprocalRankFusion


class ContextRetrieverFactory:
    def __init__(self, config: dict):
        self.config = config
            
    def create_context_retriever(self, retriever: VectorStoreRetriever) -> ContextRetriever:
        rag_function = self.config['rag-function']
        context_retrievers = {
            "reciprocal_rank_fusion": ReciprocalRankFusion(retriever, self.config['multi-query-request-template']),
            "cosine_similarity_rerank": CosineSimilarityRerank(retriever, self.config['multi-query-request-template'])
        }
        return context_retrievers.get(rag_function)