from langchain.load import dumps, loads
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.vectorstores import VectorStoreRetriever

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

template_question = """Answer the following question based on this context:

{context}

Question: {question}
"""


class RagLLm:

    def __init__(self, retriever: VectorStoreRetriever):
        self.prompt_rag_fusion = ChatPromptTemplate.from_template(template_multiquery)
        self.prompt_question = ChatPromptTemplate.from_template(template_question)
        self.retriever = retriever

    def generate_answer(self, question):
        max_attempts = 3
        response = ''
        attempt = 0
        while not response and attempt < max_attempts:
            llm_response: AIMessage = ChatOllama(model="llama3").invoke(
                self.prompt_question.format(context=(self._generate_queries | self.retriever.map() | self._reciprocal_rank_fusion)
                                            .invoke({"question": question}), question=question))
            response = StrOutputParser().parse(text=llm_response.content)
            attempt += 1
        return response

    def _generate_queries(self, question):
        max_attempts = 5
        generated_queries = []
        attempt = 0
        while len(generated_queries) <= 3 and attempt < max_attempts:
            llm_response: AIMessage = ChatOllama(model="llama3").invoke(
                self.prompt_rag_fusion.format(question=question))
            generated_queries = StrOutputParser().parse(text=llm_response.content).split("\n")
            generate_queries = list(filter(lambda item: item.strip(), generated_queries))
            attempt += 1
        return generate_queries

    def _reciprocal_rank_fusion(self, results: list[list], k=60):
        fused_scores = {}
        for docs in results:
            for rank, doc in enumerate(docs):
                doc_str = dumps(doc)
                if doc_str not in fused_scores:
                    fused_scores[doc_str] = 0
                previous_score = fused_scores[doc_str]
                fused_scores[doc_str] += 1 / (rank + k)
        reranked_results = [
            (loads(doc), score)
            for doc, score in sorted(fused_scores.items(), key=lambda x: x[1], reverse=True)
        ]
        return reranked_results
