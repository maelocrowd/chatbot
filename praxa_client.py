import torch
torch.classes.__path__ = []
import streamlit as st
import praxa_rag
import time

# Streamed response emulator
def response_generator(question):
    response = praxa_rag.answer_and_sources(question)
    answer = response["answer"] if isinstance(response, dict) else str(response)
    for word in answer.split():
        yield word + " "
        time.sleep(0.05)

st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if question := st.chat_input("Ask me about a theatre!"):
    with st.chat_message("user"):
        st.markdown(question)
    st.session_state.messages.append({"role": "user", "content": question})

    assistant_message = ""
    with st.chat_message("assistant"):
        placeholder = st.empty()
        for chunk in response_generator(question):
            assistant_message += chunk
            placeholder.markdown(assistant_message + "▌")
        placeholder.markdown(assistant_message)

    st.session_state.messages.append({"role": "assistant", "content": assistant_message})

