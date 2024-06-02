import streamlit as st
from openai import OpenAI
from langchain_core.messages import HumanMessage
from langchain_openai import AzureChatOpenAI

st.title("KnaufGPT")
st.image('D:\\Documentos\\GenAI\\ConversationalChat\\img\\knauf.png', width=200)

model = AzureChatOpenAI(
    openai_api_version=st.secrets["AZURE_OPENAI_API_VERSION"],
    azure_deployment=st.secrets["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"])

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Qué quieres preguntar?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        mensaje_humano = HumanMessage(
            content=prompt)
        stream = model.invoke([mensaje_humano]).content
        response = st.write(stream)
    st.session_state.messages.append({"role": "assistant", "content": stream})
    print(st.session_state.messages)