import os
import streamlit as st
import tempfile
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
import easyocr

def main():
    load_dotenv()
    st.set_page_config(page_title="Ask Your Image")
    st.header("Ask from your Image")

    # upload file
    uploaded_file = st.file_uploader("Upload the Image", type=["jpeg", "jpg", "png"])

    if uploaded_file is not None:
        # Save the uploaded file to a temporary file
        temp_file_path = save_uploaded_file(uploaded_file)

        # extract the text using OCR
        reader = easyocr.Reader(["en"])  # language
        results = reader.readtext(temp_file_path)

        text = " ".join(result[1] for result in results)

        # split text into chunks
        text_splitter = CharacterTextSplitter(separator="\n", chunk_size=10, chunk_overlap=0, length_function=len)
        texts = text_splitter.split_text(text)

        # create embeddings
        embeddings = OpenAIEmbeddings()
        document_search = FAISS.from_texts(texts, embeddings)

        # show user input
        user_question = st.text_input("Ask a question from your image:")

        if user_question:
            docs = document_search.similarity_search(user_question)

            # load QA chain
            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type="stuff")

            # run QA chain
            response = chain.run(input_documents=texts, question=user_question)

            st.write(response)

def save_uploaded_file(uploaded_file):
    # Save the uploaded file to a temporary file and return its path
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file_path = temp_file.name

    try:
        temp_file.write(uploaded_file.read())
    finally:
        temp_file.close()

    return temp_file_path

if __name__ == '__main__':
    main()
