import streamlit as st


def render_exit():
    st.markdown(f""" <p style="font-family: serif; font-size:2vw; color:white; text-align:center;">Thanks for 
    playing!<br>See you next time.<br><br>You can now close the window.<br></p>""", unsafe_allow_html=True)
    st.image("../pictures/logo_banner.png")
