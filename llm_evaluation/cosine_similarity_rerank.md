# Setup
``yaml
rag-function: "cosine_similarity_rerank"
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
    According to the context, the error code A_100 corresponds to an error response with status code 401 and an error message "Authentication token is missing".

## Analysis
    Correct. Better if it doesn't refer to the context, but that's a prompting improvement.

# What is the full list of Authentication error codes along with the error message?
    Based on the provided context, the full list of Authentication error codes is:
    
    A_100 - Error message: "Authentication token is missing"
    A_101 - Error message: "Authentication token has expired"
    A_102 - Error message: "Authentication token is invalid or malformed"
    A_103 - Error message: "Authentication credentials are invalid"
    A_104 - Error message: "User lacks sufficient permissions"
    A_105 - Error message: "Access denied to the requested resource"
    A_106 - Error message: "Authentication rate limit exceeded"
    These error codes are mentioned in the provided context, specifically in the sections titled "Scenario Outline: Authentication Error Codes" and other related scenarios.

## Analysis
    Correct

# What are the downstreams of Purchase Gateway?
    Based on the context, the downstreams of Purchase Gateway are:
    
    Authentication Server (to validate the JWT)
    Purchase Orchestrator Service
    Third-Party Payment Transaction Service (for processing payment transactions)

## Analysis
    Somewhat correct. The Third-Party Payment Trasnaction Service is a downstream of Purchase Orchestrrator Service.

# What fields are included in the request to Purchase Orchestrator?
    Based on the provided context, particularly the API documentation for the Purchase Orchestrator (Purchase Orchestrator API Documentation), the request to initiate a purchase includes:
    
    Products: The products that the customer wants to purchase.
    This information is not explicitly stated in the provided documents, but it can be inferred from the scenario described in the Feature: Purchase Orchestrator document, which mentions initiating a purchase for one or more products.

## Analysis
    Incorrect. It's unable to retrieve the relavent document.
    This may be fixed with:
    1. using RAPTOR to summarise each of the documents as the api-docs do not contain enough
    context to return a similarity match.
    2. Using routing with the below query:
    ``` 
        Where is the most relavent document for the following question:
        {query}
        Given the following folders:
        - api-docs
        - cql-schema
        - cucumber features files
        - high level overview
    ``` 
    I have asked this to the llm and it returns with the correct answer.
    As an experiment I have change the store to only store api-docs; it is able to return related context, however 
    the documents returned does not contain the full context of the request. Therefore we may as need to visit the
    chunking strategy depending on the type of document.
    
