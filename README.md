
# RAG Chatbot

**RAG (Retrieval-Augmented Generation) Chatbot** combines the power of advanced language models with document retrieval techniques to create a context-aware conversational agent. This chatbot leverages a collection of Markdown files to provide accurate and contextually relevant answers, enhancing the traditional chatbot experience.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Supported Models](#supported-models)
- [Response Synthesis Strategies](#response-synthesis-strategies)
- [Example Data](#example-data)
- [Running the Chatbot](#running-the-chatbot)
- [Debugging](#debugging)
- [References](#references)
- [License](#license)

## Introduction

This project implements a Retrieval-Augmented Generation (RAG) chatbot. The RAG Chatbot enhances its responses by retrieving relevant information from a pre-indexed set of documents, allowing for more accurate and context-aware interactions.

The system is designed to:
- Deliver a **ChatGPT-like experience** with enhanced context awareness.
- Integrate **retrieval-augmented generation** techniques to refine responses.
- Operate efficiently on local hardware, including GPU-accelerated systems.

## Features

- **Memory Builder**: Pre-processes Markdown documents, chunks them into manageable sections, generates embeddings, and stores them in a Chroma database.
- **Contextual Retrieval**: Retrieves relevant document sections based on user queries.
- **Enhanced Response Generation**: Utilizes sophisticated response synthesis strategies to refine and deliver accurate answers.
- **Local Model Support**: Supports running models locally with quantization and GPU acceleration.

## Architecture

The architecture of the chatbot includes the following components:

1. **Memory Builder**: Processes and indexes Markdown files by creating embeddings using the `all-MiniLM-L6-v2` model.
2. **RAG Workflow**: 
   - Receives a user query.
   - Optionally rephrases the query using a language model for better retrieval.
   - Retrieves relevant sections from the Chroma embedding database.
   - Generates a response using the retrieved context.
3. **Response Synthesis**: Combines or refines the context to produce the final response.

![RAG Chatbot Architecture](path/to/architecture-image.png)

## Prerequisites

- **Python** 3.10+
- **GPU** supporting CUDA 12.1, 12.2, 12.3, or 12.4
- **Poetry** 1.7.0 for dependency management

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Anonymous3017/chatbot_rag.git
   cd chatbot_rag
   ```

2. **Install Poetry**:
   Follow the [Poetry installation guide](https://python-poetry.org/docs/#installation).

3. **Bootstrap the environment**:
   ```bash
   make setup_cuda  # For systems with NVIDIA CUDA support
   # or
   make setup_metal  # For macOS systems with Metal GPU support
   ```

## Usage

### Building the Memory Index

To build the memory index from your Markdown files:

```bash
python chatbot/memory_builder.py --chunk-size 1000
```

### Running the Chatbot

For a standard chatbot experience:

```bash
streamlit run chatbot/chatbot_app.py -- --model openchat-3.6 --max-new-tokens 1024
```

For the RAG Chatbot with context-aware retrieval:

```bash
streamlit run chatbot/rag_chatbot_app.py -- --model openchat-3.6 --k 2 --synthesis-strategy async-tree-summarization
```

## Supported Models

The following models are supported, optimized for both CPU and GPU environments:

- **Llama-3** (8B parameters)
- **OpenChat-3.6** (8B parameters)
- **Mistral** (7B parameters)
- **Starling Beta** (7B parameters)
- **Phi-3.1 Mini** (3.8B parameters)

These models are available in quantized formats to enable efficient local execution.

## Response Synthesis Strategies

The chatbot supports various strategies to manage and synthesize context:

1. **Create and Refine**: Sequentially refines the response through multiple stages.
2. **Hierarchical Summarization**: Independently generates answers from each retrieved section and hierarchically combines them.
3. **Async Hierarchical Summarization**: A parallelized version of hierarchical summarization for faster response times.

## Example Data

To test the chatbot, you can download example Markdown pages and place them in the `docs` directory. The `Blendle Employee Handbook` is a good source for testing.

## Debugging

To debug the chatbot using PyCharm:

1. Set up your environment with the necessary configurations.
2. Use PyCharm's built-in debugging tools to step through the `Streamlit` application.

![Debugging with PyCharm](path/to/debug-image.png)

## References

- [LangChain Documentation](https://python.langchain.com)
- [Chroma Embedding Database](https://www.chroma.com)
- [Streamlit Documentation](https://docs.streamlit.io)

## License

This project is licensed under the Apache-2.0 License - see the [LICENSE](LICENSE) file for details.
