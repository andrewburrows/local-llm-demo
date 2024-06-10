Evaluation on the various RAG implementations.

Queries:

# What is the error code A_100?
To test ability to extract the correct chunk of a cucumber feature file.


# What is the full list of Authentication error codes?
To test ability to extract multiple chunks of cucumber feature files.
Note that the A_ codes in [general-system-failures](documents/cucumber_feature_files/general-system-failures.md) have been modified to expand out the variables <variable> form the Scenario outline.
The other error codes (such as R_) have been left unexpanded.
This is to test RAG with different datasets variations.

# What are the downstreams of Purchase Gateway?
To test ability to answer question with a term that doesn't appear in the dataset (downstream). However the actual
data does exist.

# What fields are included in the request to Purchase Orchestrator?
To test ability to parse api-docs on a general question.

# What is the size of the sun?
Completely unrelated question to test ability to answer questions unrelated to the documents.

# What is the full list of User Management Flow error codes?
To test the ability of respond to a question about data that doesn't exist in the dataset.