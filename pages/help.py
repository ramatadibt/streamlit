import streamlit as st 
from PIL import Image

st.set_page_config(page_title="Help section", layout="wide")

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

col1,col2,col3, col4  = st.columns([0.30,0.30, 0.2, 0.2])
with col1:
    st.image(Image.open('opaquelogo.png'))  
with col2:
     st.write(r"$\textsf{\huge Plug \& Play LLMs}$")


if col3.button('Chat with LLMs'):
    st.switch_page('app.py')

if col4.button("Chat with PDF"):
    st.switch_page("pages/pdfchat.py")

col1,col2, col3 = st.columns([0.3, 0.4, 0.3])

col2.title("How to use this App")



st.header(" 🗣️ Chat with LLMs")
st.markdown('''
1. **Choose your LLM:** Use the :blue[Select LLM] dropdown to pick the Large Language Model you want to talk to.
2. **Try example prompts:** Click on any of the 6 example prompt cards to see how the LLM responds to different topics.
3. **Ask your question:** Type your question in the Chat Input box at the bottom of the screen and press enter. The LLM will answer you.
4. **Switch LLMs:** If you want to talk to a different LLM, just pick another one from the dropdown. The new LLM will be ready to chat.
5. **Clear chat history:** To start a fresh conversation, click on the :blue[Clear Chat] button.
6. **Chat with a PDF:** Want to ask questions about a PDF? Click on the :blue[Chat with PDF] button.

# ''')

st.header('📚 Chat with  PDF')
st.markdown('''
1. **Choose your LLM:** Use the :blue[Select LLM] dropdown to pick the Large Language Model you want to use.
2. **Upload a PDF:** Click on the :blue[Browse Files] button to upload the PDF you want to ask questions about. Remember, the PDF should not be more than 3 pages long.
3. **Ask your question:** Type your question about the PDF in the Chat Input box at the bottom of the screen and press enter. The LLM will answer you.
4. **Switch LLMs:** If you want to talk to a different LLM, just pick another one from the dropdown. The new LLM will be ready to chat.
5. **Clear chat history:** To start a fresh conversation, click on the :blue[Clear Chat] button.
6. **Go back to LLMs:** Want to chat with LLMs again? Click on the :blue[Chat with LLMs] button.
''')
