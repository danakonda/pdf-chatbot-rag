import streamlit as st
import requests
backend_url="http://localhost:8000"
st.set_page_config(page_title="PDF Chatbot",layout="wide")
st.title("multi pdf rag chatbot")
#upload pdf
upload_file=st.file_uploader("upload PDF",type=["pdf"])
if upload_file:
    files={"file":(upload_file.name,upload_file.getvalue(),"application/pdf")}
    response=requests.post(f"{backend_url}/upload",files=files)
    st.success(response.json())
    
question=st.text_input("Ask a Question: ")
if st.button("Ask"):
    response=requests.get(f"{backend_url}/ask",params={"question":question})
    data=response.json()
    st.subheader("Answer")
    st.write(data["answer"])
    st.subheader("Source Documents")
    st.json(data["sources"])
#chat hisotry
if st.button("Show History"):
    response=requests.get(f"{backend_url}/history")
    history=response.json()
    st.subheader("Chat Hisstory")
    for item in history:
        st.write(f"Q: {item['question']}")
        st.write(f"A: {item['answer']}")
        st.divider()