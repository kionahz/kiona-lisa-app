import streamlit as st


def render_pomodoro_method():
    st.image("../pictures/pomodoro.png")

    # button to start the next quest
    if st.button("View map"):
        st.session_state["temp"] = ""
        st.session_state.place = "map_6"
        st.rerun()
