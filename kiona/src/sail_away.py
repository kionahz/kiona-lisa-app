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
    col1, col2 = st.columns((1, 5))
    col1.image("../pictures/shelly.png")
    col2.title("Well done Sailor! You can now call yourself CAPTAIN PRODUCTIVITY!!! Sail home safely!")

    col3, col4, col5= st.columns((1, 5, 2))
    with col4:
        st.image("../pictures/ship.png")
    with col5:
        if st.button("Thanks for playing!"):
            st.balloons()
        autoplay_audio("../audio/Orinoco-Flow.mp3")
