import google.generativeai as genai

genai.configure(api_key="AIzaSyDn9hQKsx6YD5SIRwbwzygPLeVY2Hqa0i0")

model = genai.GenerativeModel("gemini-1.5-flash-latest")

def generate_answer(question, context):

    prompt = f"""
You are an AI tutor helping rural students.

Use the textbook content below to answer the question in simple language.

Textbook Content:
{context}

Question:
{question}

Explain clearly like a teacher.
"""

    response = model.generate_content(prompt)

    return response.text