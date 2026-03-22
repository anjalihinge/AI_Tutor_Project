AI Tutor for Rural Education

Project Overview
AI Tutor for Rural Education is an AI-powered learning tool that helps students understand textbook concepts more easily. The system allows users to ask questions related to a textbook, retrieves the most relevant content from a PDF, and generates a clear explanation using AI.
This project aims to support students, especially in rural areas, by providing an interactive way to learn and understand academic topics without needing constant teacher assistance.

🚀 Features
* Ask questions from a textbook
* Retrieves relevant content from PDF
* AI-generated explanations
* Simple and interactive interface
* Fast search using vector similarity

🛠️ Technologies Used
* Python
* Streamlit for building the web interface
* FAISS for semantic search
* Google Gemini for generating explanations
* PyPDF for reading textbook PDFs
* Sentence Transformers for text embeddings

📂 Project Structure

AI_Tutor_Project
│
├── app.py
├── llm.py
├── pdf_loader.py
├── vector_store.py
├── requirements.txt
│
└── textbooks
    └── science_book.pdf
    
⚙️ Installation
Clone the repository:

git clone https://github.com/yourusername/AI_Tutor_Project.git

Move into the project folder:

cd AI_Tutor_Project

Install required dependencies:

pip install -r requirements.txt


▶️ Run the Application

Start the app using:

python -m streamlit run app.py

The AI tutor will open in your browser.

🔑 API Key Setup

Open `llm.py` and add your API key:

genai.configure(api_key="YOUR_API_KEY")

You can generate an API key from Google AI Studio.

🎯 Future Improvements

* Support for multiple textbooks
* Voice-based question input
* Multi-language explanations for rural students
* Mobile-friendly interface

