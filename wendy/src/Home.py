import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="💧", page_title="Wendy | DC Water LLM")

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

    # Display creators
    st.markdown("""
    **Created by** \n 
    Phanindra Vantipalli  
    Dolly Gada  
    Laxmi Yogita Attaluri
    """, unsafe_allow_html=True)
    
    # Display LinkedIn links
    st.markdown("""
    **LinkedIn:**  
    [Dolly Gada](https://www.linkedin.com/in/dolly-gada/)  
    [Phanindra Vantipalli](https://www.linkedin.com/in/phanindra-vantipalli/)  
    [Yogita Attaluri](https://www.linkedin.com/in/laxmiyogitaattaluri/)
    """, unsafe_allow_html=True)

    # Display GitHub links
    st.markdown("""
    **GitHub:**  
    [Phanindra Vantipalli](https://github.com/peevs99)  
    [Yogita Attaluri](https://github.com/YogitaAttaluri)
    """, unsafe_allow_html=True)
    
    # Display Email links
    st.markdown("""
    **Email:**  
    vantipalliphanindra@gmail.com  
    dollygada10@gmail.com  
    yogitalakshmi0805@gmail.com
    """, unsafe_allow_html=True)
    



#Title
st.markdown(
    """
    <h2 style='text-align: center;'>Wendy AI – Gen AI Customer Service LLM for DC Water💧</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")

#st.image('wendy1.png')
#Description
st.markdown(
    """ 
    <h5 style='text-align:center;'>Wendy is DC Water's adorable mascot, symbolizing the essence of water. 
    She's a water droplet who educates and reminds us of the crucial role water plays in our lives, 
    from hydration to sanitation. Through Wendy, DC Water encourages everyone to conserve water 
    and understand its significance!</h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")







