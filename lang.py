
from dotenv import load_dotenv
load_dotenv() 

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


model=genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response=chat.send_message(question,stream=True)
    return response


st.set_page_config(page_title="Vimal's ParaBOT")


st.markdown("""
    <style>
        .stApp {
            background-image: url('https://assets.infoq.com/content/en/service-mesh-feat.jpg');
            background-size: cover;
        }
        h1 {
            color: #FFFFFF;
            font-size: 60px;
            text-align: center;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
        }
        .stTextInput>div>input {
            color: black;
        }
    </style>
    """, unsafe_allow_html=True)

# Title in big text
st.markdown("<h1> Vimal's chatBOT vr.06</h1>", unsafe_allow_html=True)

# Blog generation header
st.header("Developed by Vimal using Gemini Pro LLM model ")


if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

if submit and input:
    response=get_gemini_response(input)
    
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))
st.subheader("The Chat History is")
    
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
    

