import os
import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Load environment variables
load_dotenv()

# Configure Mistral API
model = ChatMistralAI(
    model="mistral-large-latest",
    mistral_api_key=os.getenv("MISTRAL_API_KEY")
)

# Initialize session state for memory
if "memory" not in st.session_state:
    st.session_state.memory = [
        SystemMessage(content="You are a funny assistant and your name is Jassi.")
    ]

# UI Title
st.title("🤖 Jassi Chatbot")

# Display chat history
for msg in st.session_state.memory:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").write(msg.content)

# Input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message
    st.session_state.memory.append(HumanMessage(content=user_input))
    st.chat_message("user").write(user_input)

    # Get response
    response = model.invoke(st.session_state.memory)

    # Store AI response
    st.session_state.memory.append(AIMessage(content=response.content))
    st.chat_message("assistant").write(response.content)