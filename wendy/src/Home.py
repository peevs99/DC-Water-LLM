import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="💧", page_title="Wendy | DC Water LLM")

# Add custom CSS for changing link color and reducing spacing
st.markdown("""
<style>
    /* Change anchor element color */
    a {
        color: #000 !important; /* Change this to your desired link color */
    }

    /* Change the hover color */
    a:hover {
        color: #fff !important; /* Change this to your desired hover color */
    }

    /* Reduce spacing */
    div[data-baseweb="block"] {
        margin-bottom: 0.5rem !important;
    }
</style>
""", unsafe_allow_html=True)


#contact

with st.sidebar.expander("📬 Contact"):

    # Display LinkedIn links
    st.markdown("""
    <h2>
    <span style='color: black; font-weight: bold'>Created By</span></h2>
    \n 
    [Dolly Gada](https://www.linkedin.com/in/dolly-gada/)  
    [Phanindra Vantipalli](https://www.linkedin.com/in/phanindra-vantipalli/)  
    [Yogita Attaluri](https://www.linkedin.com/in/laxmiyogitaattaluri/)
    """, unsafe_allow_html=True)

    # Display GitHub links
    st.markdown("""
    <h2>
    <span style='color: black; font-weight: bold'>Git Hub</span></h2>
    \n 
    [Phanindra Vantipalli](https://github.com/peevs99)  
    [Yogita Attaluri](https://github.com/YogitaAttaluri)
    """, unsafe_allow_html=True)
    
    # Display Email links
    st.markdown("""
    <h2>
    <span style='color: black; font-weight: bold'>Email</span></h2>
    \n 
    vantipalliphanindra@gmail.com  
    dollygada10@gmail.com  
    yogitalakshmi0805@gmail.com
    """, unsafe_allow_html=True)



#Title
st.markdown(
    """
    <h2 style='text-align: center;'>Wendy AI – Generative AI Customer Service LLM for DC Water💧</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")

#st.image('wendy1.png')
#Description
#st.markdown(
 #   """ 
  #  <h5 style='text-align:center;'>Wendy is DC Water's adorable mascot, symbolizing the essence of water. 
   # She's a water droplet who educates and reminds us of the crucial role water plays in our lives, 
    #from hydration to sanitation. Through Wendy, DC Water encourages everyone to conserve water 
    #and understand its significance!</h5>
    #""",
    #unsafe_allow_html=True)
#st.markdown("---")

st.markdown(
    """
    <h3 style="font-weight: bold">Overview</h3>
    <p>
        Wendy AI is a specialized AI-driven customer service platform developed for DC Water. 
        It's designed to handle various water supply chain operations and service-related queries, 
        synergizing advanced NLP techniques, Large Language Models, and LLM prompt engineering.
    </p>

    <h3 style="font-weight: bold">Key Features</h3>
    <p>
        <ul>
            <li>RAG Application</li>
            <li>Specialized Responses</li>
            <li>Integration & Framework</li>
        </ul>
    </p>

    <h3 style="font-weight: bold">Technologies and Methods Used</h3>
        <ul>
            <li>
                <h5 style="font-weight: bold">Vector Stores</h5>
                <p>
                    One of the most common ways to store and search over unstructured data is to embed 
                    it and store the resulting embedding vectors. 
                    At query time, the unstructured query is embedded, and the embedding vectors 
                    that are 'most similar' to the embedded query are retrieved. 
                    A vector store takes care of storing embedded data and performing vector search. 
                    Learn more about it here.
                <p>
            </li>
            <li>
                <h5 style="font-weight: bold">ConversationalRetrievalQA</h5>
                <p>
                    This chain builds on RetrievalQAChain, providing a chat history component. 
                    It combines chat history and the question to retrieve relevant documents, 
                    which are then passed to a question-answering chain for responses. 
                    More details can be found here.
                </p>
            </li>
            <li>
                <h5 style="font-weight: bold">LangChain</h5>
                <p>
                    LangChain is a unique framework designed for applications powered by language models. 
                    It's data-aware, agentic and is primarily characterized by its components and 
                    off-the-shelf chains. Learn more about its capabilities here.
                </p>
            </li>
            <li>
                <h5 style="font-weight: bold">FAISS</h5>
                <p>
                    Facebook AI Similarity Search (FAISS) is a library crafted to facilitate developers 
                    in the swift search of multimedia document embeddings that resemble each other, 
                    solving traditional query search engines' limitations.
                </p>
            </li>
            <li>
                <h5 style="font-weight: bold">Streamlit</h5>
                <p>
                    The user interface of Wendy AI is powered by Streamlit, 
                    offering an interactive and user-friendly experience. 
                    The project is hosted on the Streamlit Community cloud.
                </p>
            </li>
            <li>
                <h5 style="font-weight: bold">Retrieval Augmented Generation (RAG)</h5    >
                <p>
                    RAG is an AI framework that retrieves data from external sources to ground 
                    Large Language Models (LLMs) on accurate, recent information, 
                    thus enhancing the LLMs' generative process. 
                    The principle of RAG ensures that the LLM responses are grounded on the most recent 
                    and reliable sources, supplementing the LLM’s internal information representation. 
                    Further reading on RAG.
                </p>
            </li>
        </ul>
""",
unsafe_allow_html=True)







