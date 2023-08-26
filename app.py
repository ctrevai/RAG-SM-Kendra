import streamlit as st
import sys
import llm_retriever as llm

from dotenv import load_dotenv
import boto3
load_dotenv()

st.title("LLAMA Demo with Kendra")

query = st.text_input("Enter your question here:")

if query:
    chain = llm.build_chain()
    result = llm.run_chain(chain, query)
    st.write(result['answer'])
    st.write("Sources:")
    for doc in result['source_documents']:
        st.write(doc.metadata['source'])

pdf = st.file_uploader("Upload PDF here")
if pdf is not None:
    s3 = boto3.client('s3')
    s3.upload_fileobj(pdf, 'raggenaiexp', pdf.name)
    st.write("Uploaded to S3")
