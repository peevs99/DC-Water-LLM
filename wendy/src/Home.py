import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="Wendy | DC Water LLM 💧")

# Add custom CSS for changing link color and reducing spacing
st.markdown("""
<style>
    /* Change anchor element color */
    a {
        color: #4e4e4e; /* Change this to your desired link color */
    }

    /* Change the hover color */
    a:hover {
        color: #4e4e4e; /* Change this to your desired hover color */
    }

    /* Reduce spacing */
    div[data-baseweb="block"] {
        margin-bottom: 0.5rem !important;
    }
</style>
""", unsafe_allow_html=True)


#contact

with st.sidebar.expander("📬 Contact"):

    # Display GitHub links
    st.markdown("""
    **GitHub:**  
    [Phanindra Vantipalli](https://github.com/peevs99)  
    [Yogita Attaluri](https://github.com/YogitaAttaluri)
    """, unsafe_allow_html=True)
    
    # Display LinkedIn links
    st.markdown("""
    **LinkedIn:**  
    [Dolly Gada](https://www.linkedin.com/in/dolly-gada/)  
    [Phanindra Vantipalli](https://www.linkedin.com/in/phanindra-vantipalli/)  
    [Yogita Attaluri](https://www.linkedin.com/in/laxmiyogitaattaluri/)
    """, unsafe_allow_html=True)
    
    # Display Email links
    st.markdown("""
    **Email:**  
    vantipalliphanindra@gmail.com  
    dollygada10@gmail.com  
    yogitalakshmi0805@gmail.com
    """, unsafe_allow_html=True)
    
    # Display creators
    st.markdown("""
    **Created by** \n 
    Phanindra Vantipalli  
    Dolly Gada  
    Laxmi Yogita Attaluri
    """, unsafe_allow_html=True)


#Title
st.markdown(
    """
    <h2 style='text-align: center;'>Wendy, the DC Water Assistant LLM 💧</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")

#st.image('wendy1.png')
#Description
st.markdown(
    """ 
    <h5 style='text-align:justify;'>Wendy is DC Water's adorable mascot, symbolizing the essence of water. 
    She's a water droplet who educates and reminds us of the crucial role water plays in our lives, 
    from hydration to sanitation. Through Wendy, DC Water encourages everyone to conserve water 
    and understand its significance </h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")


#Robby's Pages
#st.subheader("🚀 Robby's Pages")
#st.write("""
#- **Robby-Sheet** (beta): Chat on tabular data (CSV) | for precise information | process the whole file | works with [CSV_Agent](https://python.langchain.com/en/latest/modules/agents/toolkits/examples/csv.html) + [PandasAI](https://github.com/gventuri/pandas-ai) for data manipulation and graph creation
#- **Robby-Youtube**: Summarize YouTube videos with [summarize-chain](https://python.langchain.com/en/latest/modules/chains/index_examples/summarize.html)
#""")
#st.markdown("---")


#Contributing
#st.markdown("### 🎯 Contributing")
#st.markdown("""
#**Robby is under regular development. Feel free to contribute and help me make it even more data-aware!**
#""", unsafe_allow_html=True)





