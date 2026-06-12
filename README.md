# 🎭 Praxa Theatre Chatbot

**Praxa Theatre Chatbot** is a smart conversational AI that answers questions about theatre, plays, and scripts. It uses a **Retrieval-Augmented Generation (RAG)** pipeline to fetch accurate facts from local PDF documents and feed them to a Large Language Model (LLM). This ensures up-to-date answers and prevents the AI from making up information.

---

## 🚀 Key Features

* 💬 **Streamed Chat Interface**: Powered by Streamlit for a smooth, word-by-word responsive user experience.
* 🧠 **Advanced LLM**: Uses the powerful, free-tier `google/gemma-4-31b-it:free` model hosted via OpenRouter.
* 📁 **Local Document Context**: Automatically processes, chunks, and indexes a folder full of theatre PDF scripts or reference books.
* 🔍 **Local Vector Storage**: Utilizes an embedded, high-performance Chroma vector database.
* 🔤 **Open-Source Embeddings**: Computes text vectors locally using the `all-MiniLM-L6-v2` model from Hugging Face.
* 📄 **Source Tracking**: Displays exactly which PDF file and page number were used to answer your question.

---

## 🛠️ Codebase Overview

The application is structured into four simple Python modules:

* **`model.py`**: Custom wrapper for LangChain's `ChatOpenAI` class that routes requests to the OpenRouter API endpoint using your security key.
* **`context.py`**: Handles downloading PDFs via `gdown`, loading documents, splitting text into 1,000-character chunks, and managing the Chroma vector database.
* **`praxa_rag.py`**: Builds the core LangChain Expression Language (LCEL) pipeline. It chains together the retriever, custom theatre system prompts, the LLM, and extracts sources.
* **`praxa_client.py`**: The frontend UI built on Streamlit that accepts questions and displays streamed responses.

---

## 💻 Technical Setup & Installation

### 1. Prerequisites
Make sure you have **Python 3.10+** and `pip` installed on your machine.

### 2. Install Required Packages
Create a virtual environment and install the required software packages using terminal commands:

```bash
# Create a virtual environment
python -m venv venv

# Activate the environment (Windows)
.\venv\Scripts\activate


# Install dependencies from requirements.txt
pip install -r requirements.txt
```

### 3. Environment Setup
Create a file named `.env` in the root directory of your project and add your unique OpenRouter API key:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

### 4. Prepare Context Data (PDFs)
Place all your theatre reference books, scripts, or history guidelines inside a directory named `./context_data/`. 

---

## 🏃 Running the Application

### Step 1: Initialize the Vector Store (First Time Only)
Before launching the UI, you must process your local PDFs to build the local vector database. You can do this by executing a quick script or running Python in your terminal:

```python
import context

# Load the raw PDFs from your folder
docs = context.load_context_data()

# Split the texts into smaller chunks
chunks = context.chunk_context_data(docs)

# Create and save the local Chroma database
context.create_vector_store(chunks)
print("Vector store successfully created!")
```

### Step 2: Start the Web App
Run the following terminal command to boot up the web interface:

```bash
streamlit run praxa_client.py
```

Your web browser will pop open automatically at `http://localhost:8501`, allowing you to begin chatting with your AI assistant about theatre!

## 📄 License & Copyright

© 2026. All rights reserved. 

This project is maintained and contributed by Mael Taye Deneke. 