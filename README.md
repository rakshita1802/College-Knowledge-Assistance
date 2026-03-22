# 🎓 College Knowledge Assistant (RAG)

## 📌 Project Overview

This project is a Retrieval-Augmented Generation (RAG) system designed to help college students quickly find information from official documents like handbooks, syllabi, and academic calendars.

## 🚀 Features

* Semantic search using embeddings
* Vector database (ChromaDB)
* LLM-based answer generation (Ollama - Phi3)
* Source citations
* Streamlit UI

## 🛠 Tech Stack

* Python
* LangChain
* ChromaDB
* HuggingFace Embeddings
* Ollama (Phi3)
* Streamlit

## ▶️ How to Run

```bash
pip install -r requirements.txt
python ingest.py
streamlit run app.py
```

## 📂 Project Structure

* app.py → UI
* ingest.py → data processing
* src/ → RAG pipeline
* data/ → documents

## 🎯 Use Case

Helps students find academic rules, attendance requirements, syllabus, and more.
