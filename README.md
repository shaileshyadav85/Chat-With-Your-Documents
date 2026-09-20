<div align="center">

# 📄 Chat With Your Documents

An AI-powered Document Intelligence application that enables natural language querying over multi-format documents with zero hallucination risk using Retrieval-Augmented Generation (RAG).

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Groq](https://img.shields.io/badge/Groq_Cloud-F55036?style=for-the-badge&logo=fastapi&logoColor=white)

<br/>

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://chat-with-your-documents-uuasgmkmcsqtcvzgj2jyeh.streamlit.app)

**🔗 Live Demo:** [chat-with-your-documents.streamlit.app](https://chat-with-your-documents-uuasgmkmcsqtcvzgj2jyeh.streamlit.app)

</div>

---

## ⚡ Overview

**Chat With Your Documents** allows users to upload local files and ask questions grounded strictly in their own data. By combining vector embeddings with high-speed LLM inference, the system extracts, indexes, and queries content locally, providing accurate responses accompanied by source citations.

---

## ✨ Current Features

- **Multi-Document Support:** Upload and parse `.pdf`, `.docx`, and `.txt` files directly from the UI.
- **RAG Architecture:** Breaks text into semantic chunks and uses similarity search to retrieve relevant context.
- **Grounded Verification:** Transparent citation engine with collapsible source references for each response.
- **Interactive Control Panel:**
  - Real-time LLM model switching.
  - Temperature control for output determinism.
  - Configurable retrieval depth ($k$-nearest neighbors) and token budget limits.
- **Low-Latency Inference:** Powered by Groq Cloud for ultra-fast response delivery.

---

## 🏗️ System Architecture

User Query + Uploaded Doc
│
▼
┌──────────────────┐
│   file_loader    │ ───► Extract Raw Text (PDF / DOCX / TXT)
└──────────────────┘
│
▼
┌──────────────────┐
│     chunker      │ ───► Semantic Text Splitting
└──────────────────┘
│
▼
┌──────────────────┐
│   vector_store   │ ───► Generate Embeddings & Index Chunks
└──────────────────┘
│
Cosine Similarity Search (Top-k Chunks)
│
▼
┌──────────────────┐
│       llm        │ ◄─── Context + Prompt
└──────────────────┘
│
▼
Streamlit UI Response with Source Citations

---

## 🚀 Future Roadmap & Planned Features

- [ ] **OCR Engine Integration:** Add Tesseract/pdf2image support to extract text from scanned and handwritten PDFs.
- [ ] **Multi-File Upload & Cross-Querying:** Enable simultaneous multi-document processing and comparative analysis.
- [ ] **Conversational Memory:** Integrate conversational buffer memory to retain multi-turn context across chat sessions.
- [ ] **Streaming Token Generation:** Implement real-time typewriter-style response streaming for reduced perceived latency.
- [ ] **Hybrid Search & Re-ranking:** Combine BM25 keyword matching with dense vector retrieval, refined by Cohere cross-encoders.
- [ ] **Exportable Chat History:** Download chat sessions directly in `.txt` or `.pdf` formats.

---

## 📂 Repository Layout

```text
Chat-With-Your-Documents/
├── app.py              # Application entry point & Streamlit interface
├── chunker.py          # Document splitting and overlap logic
├── config.py           # Model definitions and runtime hyperparameters
├── file_loader.py      # Multi-format document parser engine
├── llm.py              # LLM client configuration (Groq integration)
├── rag.py              # Retrieval-augmented execution pipeline
├── vector_store.py     # Local vector database storage & similarity querying
├── test_groq.py        # API diagnostics script
├── requirements.txt    # Project dependencies
├── .gitignore          # Environment and cache protection rules
└── README.md           # Project documentation

🛠️ Quickstart Guide

1. Set Up Virtual Environment
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

2. Install Dependencies
pip install -r requirements.txt

3. Launch the Web Application
streamlit run app.py