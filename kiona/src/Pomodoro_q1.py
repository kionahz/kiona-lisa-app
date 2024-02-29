import streamlit as st
import time
# TODO copy all as is

def render_pomodoro_q1():
    st.sidebar.progress(60)

    st.sidebar.markdown(f"""
    <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower First Try</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Method</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Applied</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Cornell Method</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Blurting Method</p>
        <p style="line-height: 100%; font-size: 1.3vw;"><strong>Quest First Try</strong></p>
    """, unsafe_allow_html=True)

    st.markdown("Pomodoro Quest 1 - not finished yet")

    cola, colb = st.columns((8, 1))
    with colb:
        # button to return to the map
        if st.button("Continue"):
            st.session_state.place = "map_7"
            st.rerun()
