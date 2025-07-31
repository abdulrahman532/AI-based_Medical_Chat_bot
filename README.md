

# 🩺 Medical Assistant Chatbot

A multi-functional AI-powered medical chatbot that fuses document retrieval, large language models, OCR, and disease-specific logic to deliver actionable health insights. Developed as an NTI graduation project using industry-standard AI tools.

## 🚀 Features

- ✅ Interactive chat-based Q\&A on medical topics
- 🧠 Retrieval-Augmented Generation (RAG) from trusted medical PDFs
- 📝 OCR support for extracting text from scanned prescriptions or medical documents
- 📊 Disease risk analysis based on user-entered values (e.g., glucose, blood pressure)
- 🧾 Auto-generated titles for each chat
- 🗂️ Persistent session chat history


## 🧪 Technologies Used

- 🐍 **Python** — Core programming language
- 🌐 **Streamlit** — User-friendly frontend chat interface
- ⚡ **FastAPI** — High-performance backend/API
- 🤖 **Together AI (LLaMA 3)** — Advanced language model for natural-language answers
- 🔗 **LangChain** — Modular RAG and workflow orchestration
- 📁 **FAISS** — Fast similarity search for document chunks
- 🔍 **pytesseract** — OCR for image and scan text extraction
- 🧬 **Custom medical logic** — Disease risk evaluation by thresholding lab/test results


## 🧠 How It Works

1. **User submits a medical question** through the Streamlit chat interface.
2. **Backend fetches related document excerpts** via FAISS and LangChain for accurate, context-aware responses.
3. **Prompt is sent to LLaMA 3** on Together AI for answer generation.
4. If an image is provided, **OCR extracts text** and feeds it to the model as context.
5. If the user includes measurements (e.g., blood sugar), **custom disease logic** analyzes health risk and gives warnings.
6. **Answers and session titles are stored** in chat history for future reference.

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-medical-chatbot.git
cd ai-medical-chatbot
```


### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```


### 3. Install Dependencies

```bash
pip install -r requirements.txt
```


### 4. Prepare the FAISS Vector Index

Place the medical PDF (`14.DavidWerner-WhereThereIsNoDoctor.pdf`) in the root directory. Then run:

```bash
python rag.py
```

This will create a `faiss_index/` folder to store indexed vector data for fast retrieval.

### 5. Configure API Keys

Create a `.env` file with the following (replace with your actual key):

```
TOGETHER_API_KEY=your_together_api_key
```


## 🌐 Public Deployment with ngrok

### 6. Install ngrok

Download ngrok from [ngrok.com/download](https://ngrok.com/download) or via package manager:

```bash
brew install ngrok
# OR
sudo snap install ngrok
```


### 7. Launch the FastAPI Backend

```bash
uvicorn backend:app --port 8000 --reload
```


### 8. Share Backend via ngrok

```bash
ngrok http 8000
```

Copy the HTTPS forwarding URL, for example:

```
Forwarding: https://xyz123.ngrok.io -> http://127.0.0.1:8000
```


### 9. Update Streamlit with ngrok URL

Edit the `url` variable in `app.py`:

```python
url = "https://xyz123.ngrok.io/llm/"
```


## 🔁 Running the Chatbot UI

Launch:

```bash
streamlit run app.py
```

Open your browser at:

```
http://localhost:8501
```

Start chatting with your AI-powered medical assistant!

## 📂 Project Structure

```
.
├── app.py                  # Streamlit UI
├── backend.py              # FastAPI API/AI backend
├── rag.py                  # Medical PDF to FAISS index builder
├── faiss_index/            # (generated) vector search folder
├── .env                    # API key (excluded from version control)
├── requirements.txt        # All dependencies
├── 14.DavidWerner-WhereThereIsNoDoctor.pdf  # Medical reference
└── README.md               # This documentation
```


## 🔒 Security Best Practices

- Never upload your `.env` or API keys to public repos.
- Add these lines to your `.gitignore`:

```
.env
faiss_index/
__pycache__/
```


## 💡 To-Do / Improvements

- [ ] Persistent chat storage with a real database
- [ ] User-uploaded custom PDFs for more sources
- [ ] Containerized deployment (Docker, Render, Hugging Face Spaces)
- [ ] Speech recognition (voice input/output)
- [ ] Expanded multilingual and multi-document support


## Team Members

- Abdelrahman Hamada Yousef
- Yousef Reda Hassan
- Yousef Hazem
- Kadria Munir Ibrahim


## 📦 requirements.txt

Copy and use this file for package installation:

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

Make sure [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) is installed before running the system.

## ⚠️ Disclaimer

> This chatbot is intended strictly for **educational and reference use**.
> It does **not** diagnose, treat, or offer professional medical advice.
> Always consult licensed medical professionals for real-life healthcare situations.
