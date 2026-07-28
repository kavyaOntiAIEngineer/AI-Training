# AI-Powered Intelligent Search System using Sentence Transformers & Vector Databases

##  Overview

This capstone project demonstrates the implementation of an **AI-Powered Intelligent Search System** using **Sentence Transformers** and **Vector Databases**. Unlike traditional keyword-based search, this system understands the semantic meaning of user queries and retrieves the most relevant documents using vector similarity search.

The project covers the complete workflow, from data preprocessing and embedding generation to vector indexing, semantic retrieval, and performance evaluation.

---

##  Objectives

- Build a semantic search application using a real-world Kaggle dataset.
- Clean and preprocess textual data.
- Generate dense vector embeddings using Sentence Transformers.
- Store embeddings in vector databases.
- Perform natural language search.
- Retrieve and rank the most relevant results.
- Display metadata with similarity scores.
- Measure indexing and query execution times.
- Compare two vector databases and identify the most suitable one.

---

##  Features

- Semantic search using Sentence Transformers
- Text preprocessing and cleaning
- Vector indexing with FAISS
- Metadata storage using ChromaDB
- Natural language query support
- Similarity score ranking
- Performance benchmarking
- Comparison of vector databases

---

##  Technologies Used

- Python
- Pandas
- NumPy
- Sentence Transformers
- FAISS
- ChromaDB
- Kaggle Dataset
- Jupyter Notebook
- VS Code

---

##  Project Workflow

1. Download and load a Kaggle dataset.
2. Clean and preprocess the text data.
3. Generate sentence embeddings using the **all-MiniLM-L6-v2** model.
4. Store embeddings in **FAISS**.
5. Store embeddings in **ChromaDB**.
6. Accept natural language queries.
7. Convert queries into embeddings.
8. Retrieve the most relevant documents.
9. Display metadata and similarity scores.
10. Measure indexing and query response times.
11. Compare the performance of FAISS and ChromaDB.

---

## Performance Metrics

The project evaluates:

- Embedding Generation Time
- Vector Indexing Time
- Query Response Time
- Similarity Ranking
- Search Accuracy


---

##  Installation

Clone the repository:

```bash
git clone https://github.com/your-username/AI-Powered-Intelligent-Search-System.git
```

Install the required libraries:

```bash
pip install pandas numpy sentence-transformers faiss-cpu chromadb kaggle
```

---

##  How to Run

1. Open the project in **VS Code** or **Jupyter Notebook**.
2. Download the required Kaggle dataset.
3. Run each notebook cell sequentially.
4. Enter a natural language query.
5. View the retrieved results along with similarity scores and metadata.

---

##  Concepts Covered

- Semantic Search
- Natural Language Processing (NLP)
- Sentence Embeddings
- Vector Databases
- FAISS
- ChromaDB
- Similarity Search
- Information Retrieval
- Dense Vector Representations

---

##  Learning Outcomes

By completing this project, I learned how to:

- Build an end-to-end semantic search application.
- Generate sentence embeddings using transformer models.
- Perform vector similarity search efficiently.
- Compare multiple vector databases.
- Measure indexing and query performance.
- Work with real-world NLP datasets.
- Understand the fundamentals of modern information retrieval systems.

---

##  Future Enhancements

- Integrate Pinecone or Weaviate.
- Build a Streamlit-based user interface.
- Implement Hybrid Search (Keyword + Semantic Search).
- Add document reranking models.
- Support real-time document indexing.

---

##  Conclusion

This project demonstrates how semantic search can significantly improve information retrieval by understanding the contextual meaning of user queries. By combining **Sentence Transformers**, **FAISS**, and **ChromaDB**, the system provides fast, accurate, and scalable document retrieval, making it suitable for search engines, chatbots, recommendation systems, and Retrieval-Augmented Generation (RAG) applications.
