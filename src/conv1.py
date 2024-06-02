from langchain_core.messages import HumanMessage
from langchain_openai import AzureChatOpenAI
import streamlit as st

model = AzureChatOpenAI(
    openai_api_version=st.secrets["AZURE_OPENAI_API_VERSION"],
    azure_deployment=st.secrets["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"],
)

message = HumanMessage(
    content="Dame una recomendación para este día frío de domingo."
)
print(model.invoke([message]).content)
