from abc import ABC, abstractmethod
from langchain_core.vectorstores import VectorStoreRetriever

from langchain.retrievers import ContextualCompressionRetriever
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


class ContextRetriever(ABC):

    def __init__(self, retriever: ContextualCompressionRetriever):
        self.retriever:ContextualCompressionRetriever = retriever

    @abstractmethod
    def query_context_chain(self):
        pass
