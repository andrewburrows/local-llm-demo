# Setup
``yaml
rag-function: "reciprocal_rank_fusion"
llm-query-template: |-
Answer the following question based on this context:

{context}

Question: {question}
multi-query-request-template: |-
You are a helpful assistant that generates multiple sub-questions related to an input question.
The goal is to break down the input into a set of sub-problems / sub-questions that can be answers in isolation.
Generate multiple search queries related to: {question}

You must only generate 3 queries. No more than 3 is allowed.

Example:
The three queries are (3 queries):
1. This is the first query.
2. This is the second query.
3. This is the third query.

The three queries are (3 queries):
``

# Questions
# What is the error code A_100?
    According to the context, the error code A_100 corresponds to the error message "Authentication token is missing".

## Analysis
 Correct. Better if it doesn't refer to the context, but that's a prompting improvement.

# What is the full list of Authentication error codes along with the error message?
   Based on the provided context, the full list of Authentication error codes is:

    A_100
    A_101
    A_102
    A_103
    These codes are mentioned in the page content of the two documents.

## Analysis
    Incorrect. Missing many error codes.

# What are the downstreams of Purchase Gateway?
    Based on the provided context, we can infer that the downstream services of Purchase Gateway are:
    
    Authentication Server (to validate the user's JWT)
    Purchase Orchestrator Service
    Third Party Payment Transaction Service (for initiating actual payments and returning order status)
    These services are mentioned in the second document as the next steps after the Purchase Gateway validates the user's JWT and submits the request product to the Purchase Orchestrator.

## Analysis
    Somewhat correct. The Third-Party Payment Trasnaction Service is a downstream of Purchase Orchestrrator Service.


# What fields are included in the request to Purchase Orchestrator?
    Based on the provided context, I can answer your question.
    
    The fields that are included in the request to Purchase Orchestrator are:
    
    page_content: This field contains the text content of a document or feature description related to the Purchase Orchestrator service.
    metadata: This field includes metadata information about the source of the content, such as the file path or location where the content is stored.
    These fields are part of the constructor object that represents a Document in the schema.

## Analysis
    Incorrect. Non-sense answer.