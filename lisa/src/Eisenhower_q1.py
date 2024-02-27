import streamlit as st

def render_eisenhower_q1():
    st.markdown("Eisenhower Quest - not finished yet")

    # button to return to the map
    if st.button("View Map"):
        st.session_state["temp"] = ""
        st.session_state.place = "map_2"
        st.rerun()



