from langchain.load import dumps
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain.retrievers import ContextualCompressionRetriever
from langchain_core.vectorstores import VectorStoreRetriever

from llm.context_retrieval.context_retriever import ContextRetriever, template_multiquery


class SimpleRetriever(ContextRetriever):

    def __init__(self, retriever: ContextualCompressionRetriever):
        super().__init__(retriever)
        print(self.retriever)

    def query_context_chain(self):
        def generate_response(input):
            print(f"Generate_response. input:{input}")

            print(self.retriever)
            question = input['question']
            print(question)
            documents = self.retriever.invoke(input['question'])
            for document in documents:
                print(document.page_content)
            response = [document.page_content for document in documents]
            return response[:2]

        return generate_response
