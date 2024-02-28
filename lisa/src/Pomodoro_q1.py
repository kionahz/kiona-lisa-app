import streamlit as st


def render_pomodoro_q1():
    st.markdown("Pomodoro Quest 1 - not finished yet")

    cola, colb = st.columns((8, 1))
    with colb:
        # button to return to the map
        if st.button("Continue"):  # TODO
            st.session_state.place = "map_7"
            st.rerun()
