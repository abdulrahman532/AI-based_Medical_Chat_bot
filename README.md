# 🩺 AI Medical Assistant Chatbot

An AI-powered medical chatbot that answers general health questions using document retrieval (RAG) and large language models. It uses **Streamlit**, **FastAPI**, **LangChain**, **FAISS**, and **Together AI's LLaMA 3** — powered by the book *Where There Is No Doctor*.

---

## 🔧 Tech Stack

| Component         | Tool/Library                                     |
| ----------------- | ------------------------------------------------ |
| **UI**            | Streamlit                                        |
| **Backend**       | FastAPI                                          |
| **Vector Search** | LangChain + FAISS                                |
| **Embedding**     | Hugging Face: `all-MiniLM-L6-v2`                 |
| **LLM**           | Together AI: `meta-llama/Llama-3.3-70B-Instruct` |
| **Tunneling**     | Ngrok (for public access to local backend)       |
| **Document**      | *Where There Is No Doctor* (PDF)                 |

---

## ✅ Features

* Natural conversation interface (Streamlit)
* Automatically generates chat titles
* Session-based chat history
* Uses real medical content via RAG
* Personalizes responses using user name
* Can be exposed to the internet using ngrok

---

## ⚠️ Disclaimer

> This chatbot is for **educational and informational purposes only**.
> It does **not** provide real medical advice, diagnosis, or treatment.

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-medical-chatbot.git
cd ai-medical-chatbot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Prepare the FAISS Vector Index

Make sure the file `14.DavidWerner-WhereThereIsNoDoctor.pdf` is in the root directory. Then run:

```bash
python rag.py
```

This creates a folder called `faiss_index/` which holds the searchable vector data.

### 5. Set Up Environment Variables

Create a `.env` file and add your Together AI API key:

```
TOGETHER_API_KEY=your_together_api_key
```

---

## 🌐 Make Backend Public with ngrok

### 6. Install ngrok

If you don’t have ngrok installed yet:

* Download it from [https://ngrok.com/download](https://ngrok.com/download)
* Or install using a package manager:

```bash
brew install ngrok
# or
sudo snap install ngrok
```

### 7. Start the FastAPI Backend

```bash
uvicorn backend:app --port 8000 --reload
```

### 8. Expose the Backend via ngrok

In another terminal:

```bash
ngrok http 8000
```

Copy the HTTPS forwarding URL from ngrok, such as:

```
Forwarding: https://abc123.ngrok.io -> http://127.0.0.1:8000
```

### 9. Update Streamlit to Use ngrok URL

In your `app.py` file, update this line:

```python
url = "http://127.0.0.1:8000/llm/"
```

To your ngrok HTTPS address:

```python
url = "https://abc123.ngrok.io/llm/"
```

---

## 🔁 Run the Chat UI

In a new terminal window, run:

```bash
streamlit run app.py
```

Then open your browser and go to:

```
http://localhost:8501
```

You can now interact with your medical chatbot.

---

## 📂 Project Structure

```
.
├── app.py                  # Streamlit frontend
├── backend.py              # FastAPI backend logic
├── rag.py                  # Builds FAISS index from the medical PDF
├── faiss_index/            # Vector search index (generated)
├── .env                    # API key (excluded from Git)
├── requirements.txt        # Python dependencies
├── 14.DavidWerner-WhereThereIsNoDoctor.pdf  # Source medical content
└── README.txt              # This documentation (optional)
```

---

## 🔒 Security Tips

* Never commit your `.env` file or API keys to GitHub.
* Add the following to your `.gitignore` file:

```
.env
faiss_index/
__pycache__/
```

---

## 💡 To-Do (Future Improvements)

* [ ] Add persistent chat storage using a database
* [ ] Allow uploading custom medical PDFs
* [ ] Deploy to Render, HuggingFace Spaces, or Docker
* [ ] Integrate voice input/output (speech-to-text and TTS)
* [ ] Expand knowledge base to support more languages and documents


## 📦 requirements.txt

Below is the list of required Python packages. You can copy this into a file called `requirements.txt`.

```
# --- Frontend ---
streamlit

# --- Backend ---
fastapi
uvicorn
python-dotenv
requests

# --- LangChain & Vector Search ---
langchain
faiss-cpu
sentence-transformers
langchain-community
langchain-core
langchain-huggingface

# --- Together AI SDK ---
together

# --- PDF Processing ---
pypdf

# --- Optional Tools ---
tqdm

# --- Tunneling (Public Access) ---
ngrok
```

---
