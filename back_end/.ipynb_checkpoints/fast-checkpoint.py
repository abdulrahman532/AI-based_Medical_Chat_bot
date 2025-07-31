from fastapi import FastAPI
from dotenv import load_dotenv
from together import Together
from pydantic import BaseModel
import re
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document


load_dotenv()
app = FastAPI()
client = Together(api_key="4ac69519b74d2a7ee9311e218bea67f57a919706089146fefb052a05200b39be")

user_context = {}

# Load FAISS index and embedding model once
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    answer: str

@app.post("/llm/", response_model=ChatResponse)


def l_l_m(chat_input: ChatRequest):
    user_input = chat_input.query

    # Extract name
    name_match = re.search(r"my name is (\w+)", user_input.lower())
    if name_match:
        user_context["name"] = name_match.group(1).capitalize()

    if "name" in user_context and "my name is" not in user_input.lower():
        user_input = f"{user_context['name']} said: {user_input}"

    # Step 1: Retrieve relevant chunks from FAISS
    retrieved_docs = vectorstore.similarity_search(user_input, k=3)
    retrieved_text = "\n\n".join(doc.page_content for doc in retrieved_docs)

    # Step 2: Build prompt with retrieved context
    full_prompt = f"""Use the context below to answer the user's question.
Context:
{retrieved_text}

Question: {user_input}
Answer:"""

    # Step 3: Send to LLM
    try:
        response = client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
            messages=[{"role": "user", "content": full_prompt}]
        )
        model_ans = response.choices[0].message.content
    except Exception as e:
        model_ans = f"❌ LLM Error: {e}"

    return ChatResponse(answer=model_ans)

