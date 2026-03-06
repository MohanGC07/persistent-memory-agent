# 🧠 Persistent Memory Agent

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://persistent-memory-agent.streamlit.app)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 📖 Project Description

**Persistent Memory Agent** is a Python-based AI agent that can store, retrieve, and reason over user-provided memories using semantic search. Unlike traditional chatbots that forget context between sessions, this agent leverages **ChromaDB** as a persistent vector store and **SentenceTransformers** for high-quality sentence embeddings — enabling it to recall semantically relevant information even across separate sessions.

The project features a clean, interactive **Streamlit** frontend that makes it easy to interact with the agent directly in your browser. Its modular architecture keeps each concern (embeddings, memory management, vector storage, UI) in a separate module, making it straightforward to extend or swap out components.

**Key highlights:**
- 🔍 Semantic memory storage using sentence embeddings
- 💾 Persistent memory across sessions via ChromaDB
- 🖥️ Interactive Streamlit-powered user interface
- 🧩 Modular and extendable codebase

---

## ✨ Features

- **📥 Store Memories Interactively** — Type any piece of information and the agent will embed and store it in its persistent memory.
- **🔎 Semantic Memory Recall** — Query the agent in natural language; it retrieves the most relevant stored memories using vector similarity search.
- **💾 Persistent Across Sessions** — ChromaDB stores embeddings to disk, so memories survive app restarts and redeployments.
- **🖥️ Streamlit UI** — Clean, intuitive browser-based interface with no frontend coding required.
- **🧩 Modular Design** — Clearly separated modules for embeddings, memory management, and vector storage make it easy to extend or replace individual components.
- **⚡ Fast & Lightweight** — Uses efficient SentenceTransformer models that run on CPU, requiring no GPU.

---

## 🛠️ Technology Stack

| Technology | Version | Purpose |
|---|---|---|
| **Python** | 3.11 | Core language |
| **Streamlit** | Latest | Interactive web UI |
| **SentenceTransformers** | Latest | Semantic embedding model |
| **ChromaDB** | Latest | Persistent vector store |
| **NumPy** | Latest | Numerical operations |
| **Pandas** | Latest | Data handling (optional) |
| **Requests** | Latest | HTTP utilities (optional) |

---

## 🚀 Installation Instructions

### Prerequisites

- Python 3.11 or higher
- `pip` package manager
- Git

### Steps

**1. Clone the repository**

```bash
git clone https://github.com/MohanGC07/persistent-memory-agent.git
cd persistent-memory-agent
```

**2. Create a virtual environment**

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

> 💡 **Tip:** If you encounter issues with ChromaDB on Windows, ensure you have the latest version of `pip` and `setuptools`:
> ```bash
> pip install --upgrade pip setuptools
> ```

---

## ▶️ Usage Instructions

### Run Locally

Start the Streamlit app with:

```bash
streamlit run app.py
```

The app will automatically open in your default browser at:

```
http://localhost:8501
```

### Using the App

1. **Store a memory** — Type a sentence or fact into the *"Add Memory"* input field and click **Save**.
2. **Recall memories** — Enter a query in the *"Search Memory"* field and click **Recall** to retrieve semantically similar stored memories.
3. **Persistent storage** — All memories are automatically saved to the `data/` directory via ChromaDB and will persist across sessions.

---

## 🌐 Demo / Deployment

The app is deployed on **Streamlit Cloud** and accessible at:

🔗 **[https://persistent-memory-agen.streamlit.app](https://persistent-memory-agen.streamlit.app)**

> To deploy your own instance:
> 1. Fork this repository
> 2. Go to [share.streamlit.io](https://share.streamlit.io)
> 3. Connect your GitHub account and select this repo
> 4. Set the main file path to `app.py` and click **Deploy**

---

## 📁 Project Structure

```
persistent-memory-agent/
│
├── app.py                # Streamlit frontend — handles UI, user input, and display logic
├── embeddings.py         # Embedding model — loads SentenceTransformer and generates vectors
├── memory_agent.py       # MemoryAgent class — core logic for storing and retrieving memories
├── vector_store.py       # ChromaDB persistent vector store — manages collections and queries
├── requirements.txt      # Project dependencies — all packages needed to run the app
├── data/                 # Folder to store ChromaDB persistent files (auto-created at runtime)
├── venv/                 # Python virtual environment (excluded from version control)
└── .gitignore            # Git ignore rules — excludes venv/, data/, __pycache__/, etc.
```

| File / Folder | Description |
|---|---|
| `app.py` | Entry point for the Streamlit app; renders the UI and connects all modules |
| `embeddings.py` | Wraps the SentenceTransformer model; exposes an `embed(text)` function |
| `memory_agent.py` | High-level `MemoryAgent` class with `add_memory()` and `recall()` methods |
| `vector_store.py` | Abstracts ChromaDB operations: collection setup, upsert, and similarity queries |
| `requirements.txt` | Pinned dependencies for reproducible installs |
| `data/` | Runtime directory where ChromaDB writes its persistent SQLite and index files |
| `venv/` | Local virtual environment; **not committed to Git** |
| `.gitignore` | Ensures `venv/`, `data/`, and cache files are excluded from source control |

---

## 🤝 Contributing

Contributions are welcome and appreciated! Here's how to get started:

1. **Fork** the repository on GitHub
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/MohanGC07/persistent-memory-agent.git
   ```
3. **Create a new branch** for your feature or fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes** and commit with a clear message:
   ```bash
   git commit -m "feat: add support for memory deletion"
   ```
5. **Push** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Open a Pull Request** against the `main` branch of this repository

> Please ensure your code follows the existing style, includes comments where appropriate, and does not break existing functionality. For major changes, open an issue first to discuss your proposal.

---

## 📄 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2024 Mohan GC

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

See the [LICENSE](LICENSE) file for full details.

---

## 👤 Author

**Mohan GC**

---

<div align="center">

⭐ If you found this project useful, please consider giving it a star on GitHub!

</div>