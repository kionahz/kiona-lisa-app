import streamlit as st

def render_cornell_method():
    st.image("../pictures/cornell.png")

    # button to start the next quest
    if st.button("View map"):
        st.session_state["temp"] = ""
        st.session_state.place = "map_4"
        st.rerun()
