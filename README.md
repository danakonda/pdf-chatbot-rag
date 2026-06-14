# Multi-PDF RAG Chatbot

## Overview

Multi-PDF RAG Chatbot is a Generative AI application that allows users to upload multiple PDF documents and ask questions based on their content.

The application uses Retrieval-Augmented Generation (RAG), semantic search, embeddings, and vector databases to retrieve relevant information from uploaded PDFs and generate accurate answers.

---

## Features

- Upload Multiple PDFs
- PDF Text Extraction
- Intelligent Text Chunking
- Embedding Generation
- Semantic Search
- ChromaDB Vector Storage
- Retrieval-Augmented Generation (RAG)
- Source Document Tracking
- Chat History
- FastAPI Backend
- Streamlit Frontend
- Docker Support

---

## Project Architecture

PDF Upload

↓

Text Extraction

↓

Chunking

↓

Embeddings

↓

ChromaDB Vector Database

↓

Similarity Search

↓

Relevant Chunks

↓

LLM

↓

Answer Generation

↓

Streamlit UI

---

## Technologies Used

### Backend

- Python
- FastAPI

### Frontend

- Streamlit

### AI / NLP

- Sentence Transformers
- Transformers
- FLAN-T5

### Vector Database

- ChromaDB

### Document Processing

- PyPDF

### Deployment

- Docker
- Render

---

## Folder Structure

multi-pdf-rag-chatbot/

├── app.py

├── frontend.py

├── requirements.txt

├── Dockerfile

├── README.md

├── documents/

├── chroma_db/

└── screenshots/

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/multi-pdf-rag-chatbot.git

cd multi-pdf-rag-chatbot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Backend

```bash
uvicorn app:app --reload
```

Backend URL:

```text
http://localhost:8000
```

---

## Run Frontend

```bash
streamlit run frontend.py
```

Frontend URL:

```text
http://localhost:8501
```

---

## API Endpoints

### Home

```http
GET /
```

Returns application status.

---

### Upload PDF

```http
POST /upload
```

Uploads PDF files and stores document chunks in ChromaDB.

---

### Ask Question

```http
GET /ask
```

Parameters:

```text
question
```

Returns:

- Answer
- Source Documents

---

### Chat History

```http
GET /history
```

Returns all previous questions and answers.

---

## Example Workflow

### Upload Documents

```text
python.pdf

java.pdf

ml.pdf
```

---

### Ask Question

```text
What is Python?
```

---

### Output

```text
Python is a high-level programming language used for web development, AI, automation, and data science.
```

---

### Source

```text
python.pdf
```

---

## Example Features

### Multi PDF Search

Searches across multiple uploaded PDFs simultaneously.

### Semantic Search

Finds information based on meaning rather than exact keywords.

### Persistent Storage

Uploaded document embeddings remain available after server restart.

### Source Tracking

Displays the document used to generate the answer.

---

## Future Improvements

- OpenAI Integration
- Gemini Integration
- LangChain RAG Pipeline
- LangGraph Agents
- User Authentication
- PDF Summarization
- Citation Support
- Cloud Storage
- Multi-User Support

---

## Screenshots

Add screenshots inside:

```text
screenshots/
```

Examples:

- PDF Upload Screen
- Question Answering Screen
- Chat History Screen
- Source Document Display

---

## Learning Outcomes

This project demonstrates:

- Retrieval-Augmented Generation (RAG)
- Embeddings
- Vector Databases
- ChromaDB
- Semantic Search
- FastAPI Development
- Streamlit Development
- Docker Deployment
- Generative AI Application Development

---

## Resume Description

Developed a Multi-PDF RAG Chatbot using FastAPI, ChromaDB, Sentence Transformers, and Streamlit. Implemented document ingestion, semantic search, retrieval-augmented generation, source tracking, persistent vector storage, chat history, Docker containerization, and deployment-ready architecture.

---

## Author

Raj

B.Tech Computer Science Engineering

Generative AI | Python | FastAPI | RAG | LangChain | AI Agents
