import streamlit as st
from openai import OpenAI
from langchain_core.messages import HumanMessage
from langchain_openai import AzureChatOpenAI
import time

st.title("KnaufGPT")
st.image('D:\\Documentos\\GenAI\\ConversationalChat\\img\\knauf2png.png', width=400)
#st.image('D:\\Documentos\\GenAI\\ConversationalChat\\img\\knauf.jpg', width=600)

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

def response_generator(response: str):
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


prompt_fijo = '''\n 
Recuerda que eres un agente de ventas de Knauf Chile. 
Recuerda que debes ser respetuoso y profesional, e intentar recomendar los productos de Knauf cada vez que puedas. 
En particular, enfócate en los productos AQUAPANEL y en el concepto de sistema constructivo, esto es, 
la combinación de productos que Knauf ofrece para solucionar problemas específicos en la construcción.
'''

# Accept user input
if prompt := st.chat_input("Qué quieres preguntar?"):
    prompt2 = prompt + prompt_fijo
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        mensaje_humano = HumanMessage(
            content=prompt2)
        stream = model.invoke([mensaje_humano]).content
        response = st.write_stream(response_generator(stream))
    st.session_state.messages.append({"role": "assistant", "content": stream})
    print(st.session_state.messages)