# 🤖 Jassi Chatbot (Streamlit + Mistral AI)

A simple and interactive chatbot built using Streamlit, LangChain, and Mistral AI.
The chatbot maintains conversation memory and responds with a fun personality named Jassi.

# 🚀 Features
💬 Chat interface using Streamlit
🧠 Conversation memory using LangChain messages
🤖 Powered by Mistral Large Language Model
😂 Fun assistant personality ("Jassi")
🔐 Environment-based API key management
# 🛠️ Tech Stack
Python
Streamlit
LangChain
Mistral AI
dotenv
# 📁 Project Structure
├── app.py                # Main Streamlit app
├── .env                  # Environment variables (API key)
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
# ⚙️ Installation

1. Create a virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
2. Install dependencies
pip install -r requirements.txt

# 🔑 Environment Setup
Create a .env file in the root directory and add your Mistral API key:

MISTRAL_API_KEY=your_api_key_here
▶️ Run the App
streamlit run app.py

Then open your browser at:

http://localhost:8501
# 🧠 How It Works
The chatbot uses LangChain message objects:
SystemMessage → defines chatbot personality
HumanMessage → user input
AIMessage → model responses

Conversation history is stored in:
st.session_state.memory
Each new message is sent along with past messages to maintain context.
# 🎭 Personality
The chatbot is initialized with:
"You are a funny assistant and your name is Jassi."
This makes responses humorous and engaging.

# 📦 Requirements

Example requirements.txt:
streamlit
python-dotenv
langchain
langchain-mistralai
# 📸 Demo

<img width="668" height="450" alt="jassi pic" src="https://github.com/user-attachments/assets/28b6c631-0735-41dd-a71e-27a25036756e" />

# 🔮 Future Improvements
Add chat history persistence (database)
Support for multiple users
Voice input/output
UI enhancements
Streaming responses

#🤝 Contributing
Feel free to fork this repo and improve the chatbot!

# 📜 License
This project is open-source and available under the MIT License.
