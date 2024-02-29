import streamlit as st
import time
# TODO copy all as is

def render_exit():
    progress_60 = st.sidebar.progress(0)
    for percent_complete_60 in range(1, 60):
        time.sleep(0.01)
        progress_60.progress(percent_complete_60)

    col1, col2, col3 = st.columns((1, 5, 1))
    with col2:
        st.markdown(f""" <p style="font-family: serif; font-size:2vw; color:white; text-align:center;">Thanks for 
        playing!<br>See you next time ☺︎<br><br>You can close the window now.<br></p>""", unsafe_allow_html=True)
        st.image("../pictures/logo_banner.png")
