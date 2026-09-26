# AI RAG Assistant

A Python-based application that allows users to ask questions about PDF documents using Retrieval-Augmented Generation (RAG), vector search, and a Large Language Model (LLM).

## Overview

AI RAG Assistant is a document question-answering application. It extracts text from PDF files, splits the text into smaller chunks, converts them into embeddings, and stores them in ChromaDB.

When a user asks a question, the application retrieves relevant chunks from the selected document and sends them to an LLM to generate a contextual answer.

## Features

- Add PDF documents
- Extract text from PDF files
- Split documents into text chunks
- Generate embeddings using HuggingFace
- Store and retrieve document embeddings with ChromaDB
- Ask questions about a selected PDF
- Generate answers using Ollama and Llama 3.1
- List and delete documents
- Persistent vector database

## Technologies

- Python
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Ollama
- Llama 3.1 (8B)
- PyMuPDF

## Project Structure

```text
Projet_RAG/
├── app.py
├── menu.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
├── database/
└── src/
    ├── document_manager.py
    ├── pdf_reader.py
    ├── text_splitter.py
    ├── vector_store.py
    └── llm_manager.py