from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
model = SentenceTransformer('all-MiniLM-L6-v2')

def split_text(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    return chunks


def create_vector_store(chunks):

    embeddings = model.encode(chunks)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    return index, chunks


def search(question, index, chunks):

    question_embedding = model.encode([question])

    D, I = index.search(question_embedding, k=3)

    results = [chunks[i] for i in I[0]]

    return results