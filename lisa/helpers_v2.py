import streamlit as st
import base64


# change background color of the sidebar
def sidebar_color():
    st.markdown("""
    <style>
        [data-testid=stSidebar] {
            background-color: #29bdbc;
        }
    </style>
    """, unsafe_allow_html=True)


def eisenhower_bg():
    eisenhower_bg_image = open("../pictures/em_empty.png", "rb").read()
    eisenhower_bg_image_base64 = base64.b64encode(eisenhower_bg_image).decode('utf-8')
    eisenhower_bg_image_url = f"data:image/png;base64,{eisenhower_bg_image_base64}"

    st.markdown(
        f""" 
            <div>
            <img src = "{eisenhower_bg_image_url}" alt = "Map" width = "100%"> 
            </div> """,
        unsafe_allow_html=True
    )