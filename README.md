# RAG PDF QA System

This project implements an end-to-end Retrieval-Augmented Generation (RAG) system designed to allow users to upload PDF documents and then ask questions about their content. It leverages Large Language Models (LLMs) and vector databases to provide contextually relevant answers, transforming unstructured PDF data into an interactive knowledge base.

# Features

PDF Text Extraction: Seamlessly extracts textual content from uploaded PDF files.

Intelligent Text Chunking: Divides extracted text into manageable, overlapping chunks to optimize retrieval and context window management for LLMs.

Vector Embeddings: Converts text chunks into high-dimensional numerical vectors using state-of-the-art embedding models.

Vector Store Indexing: Indexes embedded text chunks into a FAISS vector database for efficient semantic search.

Contextual Question Answering: Retrieves the most relevant text chunks based on a user's query and uses an LLM to generate accurate, context-aware answers.

FastAPI Backend: Provides a robust and scalable RESTful API for document upload and question-answering functionalities.

OpenRouter Integration: Utilizes OpenRouter as a flexible gateway to access various LLMs (e.g., Mistral 7B) for enhanced model choice and cost efficiency.

# Technologies Used

Backend Framework: FastAPI (Python)

PDF Processing: PyMuPDF (fitz)

LLM Orchestration: LangChain

Embeddings: HuggingFaceEmbeddings (using all-MiniLM-L6-v2 model)

Vector Database: FAISS

Large Language Models: Mistral 7B Instruct (accessed via OpenRouter.ai)

Dependency Management: pip

Environment Management: virtualenv (recommended)

# Architecture & How It Works

The RAG PDF QA System operates in two main phases:

Document Ingestion & Indexing:

A user uploads a PDF file to the /upload_pdf/ endpoint.

The extract_text_from_pdf utility reads the PDF and extracts all text content.

The chunk_text utility breaks down the extracted text into smaller, overlapping segments (chunks).

These text chunks are then converted into numerical vector embeddings using a pre-trained HuggingFaceEmbeddings model.

Finally, these embeddings are indexed and stored in a FAISS vector database, creating a searchable knowledge base.

Question Answering (Retrieval-Augmented Generation):

A user submits a natural language query to the /ask/ endpoint.

The system converts this query into a vector embedding using the same embedding model.

This query embedding is used to perform a semantic search in the FAISS vector store, retrieving the most relevant text chunks from the original PDF.

These retrieved chunks, along with the user's original query, are then fed as context to a Large Language Model (Mistral 7B Instruct via OpenRouter).

The LLM generates a coherent and contextually accurate answer based on the provided information, which is then returned to the user.