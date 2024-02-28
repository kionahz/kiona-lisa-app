import streamlit as st


def render_introduction():
    player_name = st.session_state.player_name
    if player_name is not None:
        player_name = player_name.upper()

    col1, col2 = st.columns((7, 1))
    col1.title("PIERATS - Productivity Island Expedition")
    col2.image("../pictures/logo.png")

    col1, col2, col3, col4 = st.columns((1, 4, 4, 1), gap="small")
    with col2:
        st.image("../pictures/shelly_speech.png")
    with col3:
        st.markdown(
            f""" <br><br><p style="line-height:130%; font-size:2vw; color:white">AHOI {player_name}! ⛵️️︎</p> <p 
            style="line-height:130%; font-size: 1.5vw; color: white">I am Productivishelly, but you can call me 
            Shelly!<br>I will join you on your journey today. You will learn about time management and productivity while playing fun mini games!
            Click on the button below to start your adventure of the productivity island expedition. I'll see you there!</p>""",
            unsafe_allow_html=True
        )

    cola, colb = st.columns((8, 1))
    with colb:
        # button to start the next quest
        if st.button("Let's start"):
            st.session_state["temp"] = ""
            st.session_state.place = "map_1"
            st.rerun()
