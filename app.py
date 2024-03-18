import streamlit as st 
import langchain
from langchain_community.llms import HuggingFaceHub
from langchain_community.chat_models.huggingface import ChatHuggingFace
from langchain_community.llms import HuggingFaceEndpoint
from PIL import Image

import os
HUGGINGFACEHUB_API_TOKEN =  st.secrets['HUGGINGFACEHUB_API_TOKEN']
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN

from streamlit_card import card

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []




st.set_page_config(page_title="Huggingface LLMs Chatbot", layout="wide")


def reset_conversation():
  st.session_state.messages = []
  st.session_state.card1 = False
  st.session_state.card2 = False
  st.session_state.card3 = False
  st.session_state.card4 = False
  st.session_state.card5 = False
  st.session_state.card6 = False


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

col1,col2, col3, col4, col5  = st.columns([0.2,0.30, 0.32, 0.09, 0.11])
with col1:
    st.image(Image.open('opaquelogo.png'))
with col2:
     st.write(r"$\textsf{\huge Plug and Play LLMs}$")

llm_model = col3.selectbox('**Select LLM**', ["google/gemma-2b-it", "google/gemma-7b-it",
                          "mistralai/Mistral-7B-Instruct-v0.2","mistralai/Mixtral-8x7B-Instruct-v0.1", 
                          'NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO', 
                         "HuggingFaceH4/zephyr-7b-beta"])


col4.button('Clear Chat', on_click= reset_conversation)


if col5.button("Chat with PDF"):
    st.switch_page("pages/pdfchat.py")

def handle_click(card_name):
    st.session_state.card_states = {
        "prompt1": False,
        "prompt2": False,
        "prompt3": False,
        "prompt4": False,
        "prompt5": False,
        "prompt6": False,
    }
    st.session_state.card_states[card_name] = True

col5, col6, col7,col8,col9,col10  = st.columns(6)

with col5:
    prompt1 = card(
        title="Coding",
        text="Write a python code to print fibonacci series",
        image="https://images.pexels.com/photos/3861972/pexels-photo-3861972.jpeg?auto=compress&cs=tinysrgb&w=600", 
        key = 'card1',
        styles={
        "card": {
            "width": "160px",
            "height": "120px",
            "border-radius": "2px",
            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",  
            
        },
        "text": {
            "font-family": "serif",
            "font-size" : "12px",
        }
    }
        )
    
with col6:
    prompt2 = card(
        title="Cooking",
        text="Give the step-by-step recipe to make a delicious pizza.",
        image="https://images.pexels.com/photos/905847/pexels-photo-905847.jpeg?auto=compress&cs=tinysrgb&w=600", 
        key = 'card2',
        styles={
        "card": {
            "width": "170px",
            "height": "120px",
            "border-radius": "2px",
            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
            
        },
        "text": {
            "font-family": "serif",
            "font-size" : "12px",
            
        }
    }
        )

with col7:
    prompt3 = card(
        title="Mails",
        text="Draft an email to a seller asking about computer specifications.",
        image="https://images.unsplash.com/photo-1637593992672-ed85a851fdc3?q=80&w=2062&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        key = 'card3',
        styles={
        "card": {
            "width": "170px",
            "height": "120px",
            "border-radius": "2px",
            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
            
        },
        "text": {
            "font-family": "serif",
            "font-size" : "12px",
           
        }
    }
        )
    

with col8:
    prompt4 = card(
        title="Explain",
        text="Teach me how a neural network works like I am 10 years old.",
        image="https://images.pexels.com/photos/5212338/pexels-photo-5212338.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", 
        key = 'card4',
        styles={
        "card": {
            "width": "170px",
            "height": "120px",
            "border-radius": "2px",
            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
            
        },
        "text": {
            "font-family": "serif",
            "font-size" : "12px",
        }
    }
        )
    

with col9:
    prompt5 = card(
        title="Brainstorming",
        text="What are some off-the-beaten-path destinations to explore in India?",
        image="https://miro.medium.com/v2/resize:fit:1000/1*QJ53LegShIfxuqljSB0w8Q.jpeg", 
        key = 'card5',
        styles={
        "card": {
            "width": "170px",
            "height": "120px",
            "border-radius": "2px",
            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
            
        },
        "title":{
            "font-size" : "22px", 
    
        },
        "text": {
            "font-family": "serif",
            "font-size" : "12px",
        }
    }
        )
    
with col10:
    prompt6 = card(
        title="Mentorship",
        text="Act as Steve Jobs. Give me your advice in how can I improve my time management.",
        image="https://ideas.ted.com/wp-content/uploads/sites/3/2018/09/featured_art_mentor_istock.jpg", 
        key = 'card6',
        styles={
        "card": {
            "width": "170px",
            "height": "120px",
            "border-radius": "2px",
            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
            
        },
        "title":{
            "font-size" : "22px", 
    
        },
        "text": {
            "font-family": "serif",
            "font-size" : "12px",
        }
    }
        )




llm = HuggingFaceEndpoint(
    repo_id=llm_model, 
    temperature = 0.1,
    max_new_tokens = 1024,
    top_k = 50,
    model_kwargs = {'load_in_8bit': True}
)



    # Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.session_state.card1:
    p1 = "Write a python code to print fibonacci series"
    st.chat_message("user").markdown(p1)
    # Add user message to chat history
    # st.session_state.messages.append({"role": "user", "content": p1})

    response1 = llm(p1)
    with st.chat_message("assistant"):
        st.markdown(response1)
    # st.chat_message("assistant").markdown(response1)
    # Add assistant response to chat history
    # st.session_state.messages.append({"role": "assistant", "content": response1})

if st.session_state.card2:
    p2 = "Give the step-by-step recipe to make a delicious pizza."
    st.chat_message("user").markdown(p2)
    # Add user message to chat history
    # st.session_state.messages.append({"role": "user", "content": p2})
    response2 = llm(p2)
    with st.chat_message("assistant"):
        st.markdown(response2)
    # st.chat_message("assistant").markdown(response2)
    # Add assistant response to chat history
    # st.session_state.messages.append({"role": "assistant", "content": response2})

if st.session_state.card3:
    p3 = "Draft an email to a seller asking about computer specifications."
    st.chat_message("user").markdown(p3)
    # Add user message to chat history
    # st.session_state.messages.append({"role": "user", "content": p3})
    response3 = llm(p3)
    with st.chat_message("assistant"):
        st.markdown(response3)
    # st.chat_message("assistant").markdown(response3)
    # Add assistant response to chat history
    # st.session_state.messages.append({"role": "assistant", "content": response3})


if st.session_state.card4:
    p4 = "Teach me how a neural network works like I am 10 years old."
    st.chat_message("user").markdown(p4)
    # Add user message to chat history
    # st.session_state.messages.append({"role": "user", "content": p4})
    response4 = llm(p4)
    with st.chat_message("assistant"):
        st.markdown(response4)
    # st.chat_message("assistant").markdown(response4)
    # Add assistant response to chat history
    # st.session_state.messages.append({"role": "assistant", "content": response4})


if st.session_state.card5:
    p5 = "What are some off-the-beaten-path destinations to explore in India?"
    st.chat_message("user").markdown(p5)
    # Add user message to chat history
    # st.session_state.messages.append({"role": "user", "content": p5})
    response5 = llm(p5)
    with st.chat_message("assistant"):
        st.markdown(response5)
    # st.chat_message("assistant").markdown(response5)
    # Add assistant response to chat history
    # st.session_state.messages.append({"role": "assistant", "content": response5})




if st.session_state.card6:
    p6 = "Act as Steve Jobs. Give me your advice in how can I improve my time management."
    st.chat_message("user").markdown(p6)
    # Add user message to chat history
    # st.session_state.messages.append({"role": "user", "content": p6})
    response6 = llm(p6)
    with st.chat_message("assistant"):
        st.markdown(response6)
    # st.chat_message("assistant").markdown(response6)
    # Add assistant response to chat history
    # st.session_state.messages.append({"role": "assistant", "content": response6})


# React to user input
prompt = st.chat_input(f"Ask  {llm.model.split('/')[-1]}")

if prompt :
    if prompt.lower() in ['hi', 'hello']:
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = 'Hi, How can I assist you today?'
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        
    else:
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
