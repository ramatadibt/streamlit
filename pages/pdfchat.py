import streamlit as st 
import langchain
from langchain_community.llms import HuggingFaceEndpoint
from PIL import Image
import fitz 

from streamlit_card import card

import os
HUGGINGFACEHUB_API_TOKEN =  st.secrets['HUGGINGFACEHUB_API_TOKEN']
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN


# Initialize chat history
if "pdfmessages" not in st.session_state:
    st.session_state.pdfmessages = []

if 'total_pdf_text' not in st.session_state:
    st.session_state.total_pdf_text = ''


st.set_page_config(page_title="Chat With PDFs", layout="wide")

def reset_conversation():
  st.session_state.pdfmessages = []
  st.session_state.total_pdf_text = ''
  st.session_state.uploaded_file  =  None
  st.session_state.uploaded_file_content = None
  st.session_state.uploaded_file_name = ''

st.markdown("""
        <style>
               .block-container {
                    padding-top: 0.85rem;
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

col1,col2, col3, col4, col5  = st.columns([0.2,0.30, 0.32, 0.09, 0.11])
with col1:
    st.image(Image.open('opaquelogo.png'))
with col2:
    st.write(r"$\textsf{\huge Plug \& Play LLMs}$")

    
llm_model = col3.selectbox('**Select LLM**', ["google/gemma-2b-it", "google/gemma-7b-it",
                          "mistralai/Mistral-7B-Instruct-v0.2","mistralai/Mixtral-8x7B-Instruct-v0.1", 
                          'NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO', 
                         "HuggingFaceH4/zephyr-7b-beta"])


col4.button('Clear Chat', on_click= reset_conversation)


if col5.button("Chat with LLMs"):
    st.switch_page("app.py")

llm = HuggingFaceEndpoint(
    repo_id=llm_model, 
    temperature = 0.1,
    max_new_tokens = 1024,
    top_k = 50)

st.session_state.uploaded_file = st.file_uploader(':blue[**Upload the PDF (Should be less than 4 pages)**]',  type = 'pdf')


if st.session_state.uploaded_file is not None:
    st.session_state.uploaded_file_content = st.session_state.uploaded_file.read()
    st.session_state.uploaded_file_name = st.session_state.uploaded_file.name

# if 'uploaded_file_content' in st.session_state:
if st.session_state.uploaded_file is not None:
    with fitz.open(stream=st.session_state.uploaded_file_content, filetype="pdf") as doc:
        text = ""
        num_pages = len(doc)
        if num_pages < 5: 
            for page in doc:
                text += page.get_text()

            st.session_state.total_pdf_text = text

            # Display chat messages from history on app rerun
            for message in st.session_state.pdfmessages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

        
            # React to user input
            prompt = st.chat_input(f"Ask  {llm.model.split('/')[-1]} questions about {st.session_state.uploaded_file_name}")
            
            if prompt :
                if prompt.lower() in ['hi', 'hello']:
                    # Display user message in chat message container
                    st.chat_message("user").markdown(prompt)
                    # Add user message to chat history
                    st.session_state.pdfmessages.append({"role": "user", "content": prompt})
            
                    response = 'Hi, How can I assist you today?'
                    # Display assistant response in chat message container
                    with st.chat_message("assistant"):
                        st.markdown(response)
                    # Add assistant response to chat history
                    st.session_state.pdfmessages.append({"role": "assistant", "content": response})

                else:        
                    # Display user message in chat message container
                    st.chat_message("user").markdown(prompt)
                    # Add user message to chat history
                    st.session_state.pdfmessages.append({"role": "user", "content": prompt})
    
                    response = llm(st.session_state.total_pdf_text + prompt)
                    # Display assistant response in chat message container
                    with st.chat_message("assistant"):
                        st.markdown(response)
                    # Add assistant response to chat history
                    st.session_state.pdfmessages.append({"role": "assistant", "content": response})
            
