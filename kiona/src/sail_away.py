import streamlit as st
import base64


# Code from https://discuss.streamlit.io/t/how-to-play-an-audio-file-automatically-generated-using-text-to-speech-in
# -streamlit/33201/2
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
    col1, col2 = st.columns((5, 3), gap="large")
    with col1:
        st.image("../pictures/ship.png")
    with col2:
        st.markdown(
            f"""<p style="line-height:130%; font-size: 1.5vw; color: white">Well done Sailor! You can now call 
            yourself CAPTAIN PRODUCTIVITY!!!<br><br>Sail home safely!</p> """, unsafe_allow_html=True)
        st.image("../pictures/shelly_captain.png", width=300)
        autoplay_audio("../audio/Orinoco-Flow.mp3")

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("Thanks for playing!"):
            st.balloons()
