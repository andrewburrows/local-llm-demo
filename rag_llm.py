from langchain.load import dumps
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_core.documents import Document

template_multiquery = """You are a helpful assistant that generates multiple sub-questions related to an input question.
The goal is to break down the input into a set of sub-problems / sub-questions that can be answers in isolation.
Generate multiple search queries related to: {question}

You must only generate 3 queries. No more than 3 is allowed.

Example:
The three queries are (3 queries):
1. This is the first query.
2. This is the second query.
3. This is the third query.

The three queries are (3 queries):"""


class RagLLm:

    def __init__(self, retriever: VectorStoreRetriever):
        self.retriever = retriever

    def retrieval_chain(self):
        prompt_rag_fusion = ChatPromptTemplate.from_template(template_multiquery)
        generate_queries = (
                prompt_rag_fusion
                | ChatOllama(model="llama3")
                | StrOutputParser()
                | (lambda x: x.split("\n"))
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
