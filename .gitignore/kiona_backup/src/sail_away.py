import streamlit as st
import base64
import time


def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )


def render_sail_away():
    progress_100 = st.sidebar.progress(0)
    for percent_complete_100 in range(0, 101):
        time.sleep(0.01)
        progress_100.progress(percent_complete_100)

    st.sidebar.markdown(f"""
    <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower First Try</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Method</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Applied</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Cornell Method</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Blurting Method</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Pomodoro First Try</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Pomodoro Method</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Pomodoro Applied</p>
    <p style="line-height: 100%; font-size: 1.3vw;"><strong>Sail Away</strong></p>
    """, unsafe_allow_html=True)

    player_name = st.session_state.player_name
    if player_name is not None:
        player_name = player_name.upper()

    col1, col2 = st.columns((5, 3), gap="large")
    with col1:
        st.image("../pictures/ship.png")
    with col2:
        st.markdown(
            f"""<p style="line-height:160%; font-size: 2vw; color: white">WELL DONE {player_name}!</p> <p 
            style="line-height:130%; font-size: 1.5vw; color: white">You can now call yourself<br>CAPTAIN 
            PRODUCTIVITY!!!<br><br>Sail home safely!</p> """, unsafe_allow_html=True)
        if st.button("Click here to celebrate!"):
            st.balloons()
        st.image("../pictures/shelly_captain.png", width=300)

    cola, colb = st.columns((8, 1))
    with cola:
        autoplay_audio("../audio/Orinoco-Flow.mp3")
    with colb:
        if st.button("Start again"):
            st.session_state.place = "introduction"
            st.rerun()
        if st.button("Exit the game"):
            st.session_state.place = "exit"
            st.rerun()
