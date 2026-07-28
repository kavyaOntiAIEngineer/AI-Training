# Enterprise AI Knowledge Assistant

An Enterprise AI-powered Knowledge Assistant that allows users to upload PDF documents, ask questions in natural language, and receive accurate answers using Retrieval-Augmented Generation (RAG). The application integrates Input Guardrails, Output Guardrails, and AI Evaluation to provide secure, reliable, and production-ready responses.

---

## Project Overview

This project demonstrates how modern enterprise AI assistants are built by combining Large Language Models (LLMs), Vector Databases, Retrieval-Augmented Generation (RAG), Guardrails, and AI Evaluation.

The assistant can:

- Upload one or more PDF documents
- Extract and process document content
- Generate vector embeddings
- Store embeddings in a FAISS Vector Database
- Retrieve relevant document chunks
- Generate context-aware responses
- Detect unsafe or malicious prompts
- Check AI-generated responses for safety
- Evaluate response quality using AI evaluation metrics

---

## Features

- PDF Upload
- Document Text Extraction
- Intelligent Text Chunking
- Embedding Generation
- FAISS Vector Database
- Semantic Search
- Retrieval-Augmented Generation (RAG)
- Input Guardrails
- Output Guardrails
- AI Response Evaluation
- Streamlit User Interface

---

## Project Workflow

```
User Uploads PDF
        │
        ▼
Extract Text
        │
        ▼
Split into Chunks
        │
        ▼
Generate Embeddings
        │
        ▼
Store in FAISS Vector Database
        │
        ▼
User Asks Question
        │
        ▼
Retrieve Relevant Chunks
        │
        ▼
Generate Response using LLM
        │
        ▼
Output Guardrails
        │
        ▼
AI Evaluation
        │
        ▼
Display Safe Response
```

---

## Technologies Used

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Framework | LangChain |
| LLM | Hugging Face Transformers |
| Embedding Model | Sentence Transformers |
| Vector Database | FAISS |
| Document Loader | PyPDF |
| UI | Streamlit |
| AI Evaluation | Ragas / DeepEval |
| Guardrails | Custom Guardrails |
| Development | VS Code, Jupyter Notebook |

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Enterprise-AI-Knowledge-Assistant.git

cd Enterprise-AI-Knowledge-Assistant
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

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Required Python Packages

```text
langchain
langchain-community
langchain-text-splitters
langchain-huggingface
sentence-transformers
transformers
faiss-cpu
pypdf
streamlit
ragas
deepeval
scikit-learn
```

---

## Running the Notebook

Open VS Code or Jupyter Notebook and execute all cells sequentially.

```bash
jupyter notebook
```

or

```bash
code .
```

---

## Running the Streamlit Application

```bash
streamlit run app.py
```

---

## Input Guardrails

The assistant validates user prompts before sending them to the LLM.

Checks include:

- Prompt Injection Detection
- Jailbreak Attempts
- Restricted Topics
- Malicious Keywords
- Unsafe Instructions

---

## Output Guardrails

Generated responses are validated before displaying them.

Checks include:

- Hallucination Detection
- Toxic Language Detection
- Sensitive Information Detection
- Confidential Content Filtering
- Policy Compliance

---

## AI Evaluation Metrics

The generated responses are evaluated using:

- Faithfulness
- Relevance
- Semantic Similarity
- Context Precision
- Hallucination Detection
- Response Latency


---

## Expected Output

- Safe AI-generated responses
- Relevant document retrieval
- Semantic search results
- Evaluation metrics
- Hallucination status
- Safety status

---

## Learning Outcomes

Through this project, I learned:

- Building enterprise-level RAG applications
- Working with LangChain pipelines
- Document embedding techniques
- FAISS Vector Database implementation
- Retrieval-Augmented Generation (RAG)
- Input and Output Guardrails
- AI Evaluation techniques
- Streamlit application development

---

## Future Enhancements

- Multiple PDF support
- Chat history
- Authentication
- Role-Based Access Control (RBAC)
- API Integration
- Analytics Dashboard
- Cloud Deployment
- Docker Support

---
