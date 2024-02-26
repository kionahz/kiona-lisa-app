import streamlit as st

def render_blurting_method():
    st.image("../pictures/blurting.png")

    # button to start the next quest
    if st.button("View map"):
        st.session_state["temp"] = ""
        st.session_state.place = "map_5"
        st.rerun()
