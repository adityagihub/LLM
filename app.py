from langchain_community.llms import Ollama
import streamlit as st

llm = Ollama(model = "llama3")

st.title("chatbot using llama3")

prompt = st.text_area("enter your prompt:")

if st.button("Generate"):
    if prompt:
        with st.spinner("Gennerating response..."):
           st.write_stream(llm.stream(prompt, stop = ['<|eot_id|>']))




