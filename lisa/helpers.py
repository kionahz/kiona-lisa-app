import streamlit as st


# change background color of the sidebar
def background_colors():
    st.markdown("""
    <style>
        .stApp {
                background-color: #132b3a; /* Change background color */
            }
        [data-testid=stSidebar] {
            background-color: #29bdbc;
        }
    </style>
    """, unsafe_allow_html=True)