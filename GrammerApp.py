# prompt: Develop a Streamlit app that offers an aesthetically pleasing chat interface.

##%%writefile app.py
import streamlit as st
from transformers import pipeline

# Load the grammar correction model
corrector = pipeline(
    'text2text-generation',
    'pszemraj/flan-t5-large-grammar-synthesis',
)

# Streamlit app
st.set_page_config(page_title="Chat With Dr.Morgans", page_icon=":pencil:")
st.title("Chat With Dr.Morgans")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Enter your text here:"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat
    with st.chat_message("user"):
        st.markdown(prompt)

    # Correct grammar
    corrected_text = corrector(prompt)[0]['generated_text']

    # Add assistant message to chat history
    st.session_state.messages.append({"role": "assistant", "content": corrected_text})
    # Display assistant message in chat
    with st.chat_message("assistant"):
        st.markdown(corrected_text)
