import streamlit as st 
import langchain
from langchain_community.llms import HuggingFaceHub
from langchain_community.chat_models.huggingface import ChatHuggingFace
from langchain_community.llms import HuggingFaceEndpoint
from PIL import Image

import os
HUGGINGFACEHUB_API_TOKEN =  st.secrets['HUGGINGFACEHUB_API_TOKEN']
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


st.set_page_config(page_title="Huggingface LLMs Chatbot", layout="wide")

def reset_conversation():
  st.session_state.messages = []

st.markdown("""
        <style>
               .block-container {
                    padding-top: 0.9rem;
                    padding-left: 3rem;
                    padding-right: 3rem;
                    padding-bottom: -1rem;
                }
        </style>
        """, unsafe_allow_html=True)


st.markdown("""
<style>
.stButton > button {
  background-color: #4CAF50; /* Green */
  border: solid;
  color: black;
  padding: 11px 15px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 32px;
  border-radius: 12px;
  transition-duration: 0.4s;
}

.stButton > button:hover {
  background-color: black; /* Change to black on hover */
  box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
  color: red; /* Change the font color to red on hover */
  font-weight: bold; /* Make the font bold on hover */
}
</style>
""", unsafe_allow_html=True)

col1,col2, col3, col4  = st.columns([0.2,0.35, 0.35, 0.10])
with col1:
    st.image(Image.open('opaquelogo.png'))
with col2:
    # st.markdown(f'''<span style="background-color:#FFFFFF; border-radius:5px;
    #             color: #000000; padding: 0.8em 1.2em; position: relative;
    #             text-decoration: none; font-weight: bold; margin-top: 20px; font-size: 2.25em;
    #             ">Plug & Play LLMs</span>''', unsafe_allow_html=True)
    st.title('Plug & Play LLMs')

    
llm_model = col3.selectbox('**Select LLM**', ["google/gemma-2b-it", "google/gemma-7b-it",
                          "mistralai/Mistral-7B-Instruct-v0.2","mistralai/Mixtral-8x7B-Instruct-v0.1", 
                          'NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO', 
                         "HuggingFaceH4/zephyr-7b-beta"])


col4.button('Clear Chat', on_click= reset_conversation)



llm = HuggingFaceEndpoint(
    repo_id=llm_model, 
    # model_kwargs={"temperature": temperature, "max_new_tokens": max_tokens, "top_k": top_k, "load_in_8bit": True}
    temperature = 0.1,
    max_new_tokens = 1024,
    top_k = 50,
    model_kwargs = {'load_in_8bit': True}
)



    # Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# React to user input
if prompt := st.chat_input(f"Ask  {llm.model.split('/')[-1]}"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = llm(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})



