import streamlit as st
import google.generativeai as genai
from llm import generate_answer
from pdf_loader import load_pdf
from vector_store import split_text, create_vector_store, search

st.title("AI Tutor for Rural Education")

# Load textbook only once
if "index" not in st.session_state:

    text = load_pdf(r"C:\Users\anjal\OneDrive\Desktop\AI_Tutor_Project\textbooks\science_book.pdf")

    chunks = split_text(text)

    index, stored_chunks = create_vector_store(chunks)

    st.session_state.index = index
    st.session_state.chunks = stored_chunks


question = st.text_input("Ask your question from the textbook")

if question:

    results = search(question, st.session_state.index, st.session_state.chunks)

    context = " ".join(results)

    st.write("Relevant textbook content:")
    st.write(context)

    # AI explanation
    answer = generate_answer(question, context)

    st.subheader("AI Tutor Explanation")
    st.write(answer)