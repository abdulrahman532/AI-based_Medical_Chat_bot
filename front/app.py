import streamlit as st
import requests
import uuid

st.set_page_config(page_title="Medical Assistant Chatbot", layout="wide")
st.title("🩺 Medical Assistant Chatbot")

# Initialize session state
if "histories" not in st.session_state:
    st.session_state.histories = {f"chat_{uuid.uuid4()}": {"title": "New Chat", "messages": []}}
if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = next(iter(st.session_state.histories))
if "last_query" not in st.session_state:
    st.session_state.last_query = ""

# --- Sidebar ---
with st.sidebar:
    st.header("📜 Chat History")

    if st.button("➕ New Chat"):
        new_chat_id = f"chat_{uuid.uuid4()}"
        st.session_state.histories[new_chat_id] = {"title": "New Chat", "messages": []}
        st.session_state.current_chat_id = new_chat_id
        st.session_state.last_query = ""
        st.rerun()

    st.markdown("---")
    st.markdown("📋 *Your Chats*")
    for chat_id, chat_data in st.session_state.histories.items():
        if st.button(chat_data["title"], key=f"switch_to_{chat_id}"):
            st.session_state.current_chat_id = chat_id
            st.session_state.last_query = ""
            st.rerun()

    st.markdown("---")
    if st.button("🧹 Clear Current Chat"):
        st.session_state.histories[st.session_state.current_chat_id]["messages"] = []
        st.session_state.last_query = ""
        st.rerun()

    st.markdown("---")
    st.markdown("""
    ⚠ *Disclaimer*:  
    This is for educational/reference purposes only.  
    It does *not* provide medical advice or diagnosis.
    """)

# --- Main Chat Area ---
current_chat = st.session_state.histories[st.session_state.current_chat_id]
st.subheader(f"🗨 Conversation: {current_chat['title']}")

# Display messages
for role, message in current_chat["messages"]:
    if role == "User":
        st.markdown(f"🧑 *You:* {message}")
    else:
        st.markdown(f"🤖 *Bot:* {message}")

# --- Input Form ---
with st.form(key="chat_form"):
    query = st.text_input("💬 Ask a medical question:")
    submitted = st.form_submit_button("Send")

# Process input
if submitted and query and query != st.session_state.last_query:
    is_new_chat = not current_chat["messages"]

    url = "http://127.0.0.1:8000/llm/"
    payload = {"query": query, "generate_title": is_new_chat}

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        response_data = response.json()
        bot_answer = response_data.get("answer", "⚠ No response from model.")
        suggested_title = response_data.get("title")

        # Store messages
        current_chat["messages"].append(("User", query))
        current_chat["messages"].append(("Bot", bot_answer))

        # Update last query to avoid re-submission
        st.session_state.last_query = query

        st.rerun()

    except Exception as e:
        st.error(f"❌ Error: {e}")
