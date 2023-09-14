# Wendy AI – Generative AI Customer Service LLM for DC Water💧

# App Link: https://wendyai-dcwaterllm.streamlit.app/

# 🚨 Data Usage Disclaimer 🚨

Important: The actual data behind Wendy AI is proprietary to DC Water and is not accessible to external parties. For demonstration and querying purposes, we rely solely on the publicly available ANNUAL report 2022 of DC Water.

Reference: You can download and consult the ANNUAL report 2022 from here: https://www.dcwater.com/sites/default/files/annual_report_2022_FINAL2.pdf

Await Wendy AI's response which will be displayed on the UI.

# Overview
Wendy AI is a specialized AI-driven customer service platform developed for DC Water. It's designed to handle various water supply chain operations and service-related queries, synergizing advanced NLP techniques, Large Language Models, and LLM prompt engineering.

# Key Features
1. RAG Application
2. Specialized Responses
3. Integration & Framework

# Technologies and Methods Used

# Vector Stores
One of the most common ways to store and search over unstructured data is to embed it and store the resulting embedding vectors. At query time, the unstructured query is embedded, and the embedding vectors that are 'most similar' to the embedded query are retrieved. A vector store takes care of storing embedded data and performing vector search. Learn more about it here.

# ConversationalRetrievalQA
This chain builds on RetrievalQAChain, providing a chat history component. It combines chat history and the question to retrieve relevant documents, which are then passed to a question-answering chain for responses. More details can be found here.

# LangChain
LangChain is a unique framework designed for applications powered by language models. It's data-aware, agentic and is primarily characterized by its components and off-the-shelf chains. Learn more about its capabilities here.

# FAISS
Facebook AI Similarity Search (FAISS) is a library crafted to facilitate developers in the swift search of multimedia document embeddings that resemble each other, solving traditional query search engines' limitations.

# Streamlit
The user interface of Wendy AI is powered by Streamlit, offering an interactive and user-friendly experience. The project is hosted on the Streamlit Community cloud.

# Retrieval Augmented Generation (RAG)
RAG is an AI framework that retrieves data from external sources to ground Large Language Models (LLMs) on accurate, recent information, thus enhancing the LLMs' generative process. The principle of RAG ensures that the LLM responses are grounded on the most recent and reliable sources, supplementing the LLM’s internal information representation. Further reading on RAG.

# Setup and Installation
# Prerequisites:
Python 3.8+

Virtual environment (optional but recommended)

# Steps:
1. Clone the repository:

gh repo clone peevs99/DC-Water-LLM

2. Navigate to the wendy project directory and then the src directory:

cd wendy

cd src

3. Set up a virtual environment (optional):

   python -m venv venv
   
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

5. Install the required packages:

pip install -r requirements.txt

# Usage
Run the Streamlit app:

streamlit run Home.py

Visit the provided link in your browser to interact with Wendy AI.

Interact with Wendy AI:

Once the Streamlit UI is active in your browser, enter your water service-related query in the provided input field.

# For Developers:

Dive into the Home.py and the associated modules to understand the underlying mechanisms and customize or extend functionalities as desired.

# Contributing
We encourage community contributions to enhance Wendy AI's capabilities. Here's how you can contribute:

1. Fork the repository and create your branch from master.
2. Make your changes and ensure any new code is adequately documented.
3. Test your changes to ensure stability and compatibility.
4. Submit a pull request. Include a comprehensive description of your changes.
5. Please adhere to this project's code of conduct, ensuring respect and inclusivity.


# Acknowledgements
OpenAI: For providing foundational knowledge and resources on LLMs.
Streamlit Community: For hosting and supporting our user interface.
LangChain: For the comprehensive framework that powered significant parts of Wendy AI.
DC Water: For the opportunity to serve and enhance their customer service operations.
Community & Contributors: Thank you to everyone who contributed their time, knowledge, and feedback to make Wendy AI a success.

