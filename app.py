import os
import streamlit as st 
import requests
from io import BytesIO
from PIL import Image

import streamlit as st
from data_ingest import DataIngest
from embeddings import Embeddings
from vectorstore import VectorStore
from llm_model import LLMModel
from memory import Memory
from chain import Chain
from html_templates import css, user_template, bot_template

document_loader = DataIngest(path='data/', glob='*.pdf')
documents = document_loader.split_text()
embed_documents = Embeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", 
                                     model_kwargs={'device': "cpu"})
embeddings = embed_documents.embed_documents()
create_vectorstore = VectorStore()
vectorstore = create_vectorstore.vectorstore(documents=documents,
                                             embeddings=embeddings)
create_llm = LLMModel(model='mistral-7b-instruct-v0.1.Q2_K.gguf', 
                            config={'max_new_tokens': 150, 'temperature': 0.01}, 
                            streaming=True)
llm = create_llm.llm_model()
create_memory = Memory(memory_key='chat_history', return_messages=True)
memory = create_memory.memory()
create_chain = Chain(llm=llm, retriever=vectorstore, memory=memory)
chain = create_chain.chain()
# st.session_state.conversation = chain 

def generated_conversations(user_input):
    
    with st.spinner("Generating a response..."):
        question = st.session_state.conversation({"question": user_input})
        st.session_state.chat_history = question['chat_history']
        
        for i, message in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
            else:
                st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
    
def main():
    url = "https://cdn-icons-png.flaticon.com/512/3135/3135714.png"
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    page_title = 'PrepBot - Interview preparation Assistant'
    page_icon = image
    layout = 'centered'

    st.set_page_config(page_title=page_title,
                    page_icon=page_icon,
                    layout=layout
                    )

    hide_style = '''
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                <style>
                
                '''
    header_style = '''
                <style>
                .navbar {
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    z-index: 1;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 80px;
                    background-color: #475063;
                    box-sizing: border-box;
                }
                
                .navbar-brand {
                    color: white !important;
                    font-size: 23px;
                    text-decoration: none;
                    margin-right: auto;
                    margin-left: 50px;
                }
                
                .navbar-brand img {
                    margin-bottom: 6px;
                    margin-right: 1px;
                    width: 40px;
                    height: 40px;
                    justify-content: center;
                }
                
                /* Add the following CSS to change the color of the text */
                .navbar-brand span {
                    color: #EF6E04;
                    justify-content: center;
                }
                
                </style>
                
                <nav class="navbar">
                    <div class="navbar-brand">
                    <img src="https://cdn-icons-png.flaticon.com/512/3135/3135714.png" alt="Logo">
                        PrepBot - Interview preparation Assistant
                    </div>
                </nav>
                '''
    st.markdown(hide_style, unsafe_allow_html=True)
    st.markdown(header_style, unsafe_allow_html=True)
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = chain
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    # query = st.text_input("Ask me about interview guide")
    query = st.chat_input(placeholder="Ask me about interview guide")
    if query:
        generated_conversations(query)
            
if __name__ == "__main__":
    main()