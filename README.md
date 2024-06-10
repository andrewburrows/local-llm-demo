# local-llm-demo

This project is a self-contained demonstration of running a local Language Model (LLM) with Retrieval-Augmented 
Generation (RAG) and a web-based user interface (UI) to interact with the LLM.

## Features

- Local LLM execution using the Ollama server
- Retrieval-Augmented Generation (RAG) using Langchain
- Web-based user interface built with Chainlit
- Synthetic document dataset for showcasing RAG capabilities

## Architecture

The project leverages the following components:

- **LLM**: The Language Model is run locally using the [Ollama](https://ollama.com/download) server. Alternatively, a remote LLM (such as ChatGPT) can be easily integrated.
- **RAG**: [Langchain](https://www.langchain.com/) is used for implementing Retrieval-Augmented Generation and interacting with the LLM.
- **Web UI**: The user interface is built using [Chainlit](https://docs.chainlit.io/get-started/overview).

## Dataset

A synthetic dataset of documents is included in the [documents](./documents) directory to demonstrate the LLM's ability to generate responses based on information not present in its training data. The dataset represents a fictional product called "Product Purchaser Solution" that enables users to purchase products from a website.

The dataset consists of:
- [API documentation](./documents/api_docs)
- [CQL schemas](./documents/cql)
- [Cucumber feature files](./documents/cucumber_feature_files)
- [High level documents](./documents/high_level_docs). Containing both pdf and markdown documents. To demonstrate OCR capabilities.
- [Mermaid diagrams](./documents/mermaid)
- [Images](./documents/images)

Please note that the Mermaid diagrams, images, and CQL files are currently not included in the RAG process. Architectural images were parsed with high inaccuracy on commercially available LLMs (Claude, ChatGPT), indicating potential challenges with local LLMs. The Mermaid and CQL files require the implementation of a custom [document loader](https://python.langchain.com/v0.1/docs/modules/data_connection/document_loaders/custom/).


## Getting Started

### Installation

1. Install Ollama by following the instructions for your operating system from https://ollama.com/download/.

2. Pull the llama3 image:
   ```shell
   ollama pull llama3
   ```
3. (Optional) If you have an NVIDIA GPU with CUDA capability and want to utilize it for LLM acceleration, install the CUDA Toolkit from https://developer.nvidia.com/cuda-downloads?target_os=Linux.
4. Install OCR dependencies for PDF parsing
   - macOS:
    ```shell
    brew install tesseract poppler
    ```
   - linux:
   ```shell
   sudo apt-get install -y tesseract-ocr poppler-utils
   ```
5. Set up a virtual environment and install the required Python packages
    ```shell
   python -m venv ./venv
    source ./venv/bin/activate
    pip install -r requirements.txt
    ```
### Usage
To run the web UI:
```shell
chainlit run web.py -w
```
After running navigate to [localhost:8000](http://localhost:8000).

### Jupyter Notebooks
The [jupyter](./jupyter) directory contains Jupyter notebooks that demonstrate different RAG solutions. You can explore these notebooks to understand various approaches to implementing RAG with the local LLM.