from fastapi import FastAPI,UploadFile
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader
from transformers import pipeline
import chromadb
app=FastAPI()
chat_history=[]
@app.post("/upload")
async def upload_pdf(file: UploadFile):
   
    file_path=f"documents/{file.filename}"
    contents=await file.read()
    with open(file_path,"wb")as f:
        f.write(contents)
    text=extract_text(file_path)
    chunks=create_chunks(text)
    embeddings=create_embeddings(chunks)
    print(store_chunks(chunks,file.filename))
    return {
        "filename":file.filename,
        "characters":len(text),
        "preview":text[:500],
        "chunks":chunks[0],
        "embeddings":len(embeddings[0]),
    }
#create fucntion
def extract_text(pdf_path):
    reader=PdfReader(pdf_path)
    text=""
    for page in reader.pages:
        page_text=page.extract_text()
        if page_text:
            text+=page_text
    return text
#create chunks
def create_chunks(text):
    splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
    chunks=splitter.split_text(text)
    return chunks
model=SentenceTransformer("BAAI/bge-small-en")
#create embeddings generate
def create_embeddings(chunks):
    embeddings=model.encode(chunks)
    return embeddings


#create for storing embedings in chromadb
client=chromadb.Client()
#restart then data loss whta why using
client=chromadb.PersistentClient(path="./chroma_db")
collection=client.get_or_create_collection(name="pdf_docs")
def store_chunks(chunks,filename):

    for i ,chunks in enumerate(chunks):
        collection.add(documents=[chunks],ids=[f"{filename}_{i}"],metadatas=[{"source":filename}]) 
        return {
            "message":"PDF Stored",
            "chunks":len(chunks)
        }
generator=pipeline("text2text-generation",model="google/flan-t5-base")
@app.get("/ask")
def ask(question:str):
    results=collection.query(query_texts=[question],n_results=3)
    context="\n".join(results["documents"][0])
    prompt=f"""
    You are an expert assistant.
    Use only the provided context.
    If answer is not present,
    reply:
    I don't know.
    Context:
    {context}
    Question:
    {question}:
    Answer:    
    """
    response=generator(prompt,max_new_tokens=150)
    chat_history.append( {
        "question":question,
        "answer":response[0]["generated_text"],"sources":results["metadatas"][0]
    })
    return {
        "question":question,
        "answer":response[0]["generated_text"],"sources":results["metadatas"][0]
    }
@app.get("/history")
def history():
    return chat_history