import streamlit as st

def render_eisenhower_q1():
    st.markdown("Eisenhower Quest - not finished yet")

    cola, colb = st.columns((8, 1))
    with colb:
        # button to return to the map
        if st.button("Continue"):  # TODO
            st.session_state.place = "map_2"
            st.rerun()



