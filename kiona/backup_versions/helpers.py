import streamlit as st


# change background color of the sidebar and the background
def background_colors():
    st.markdown("""
    <style>
        .stApp {
                background-color: #132b3a;
            }
        [data-testid=stSidebar] {
            background-color: #29bdbc;
        }
    </style>
    """, unsafe_allow_html=True)