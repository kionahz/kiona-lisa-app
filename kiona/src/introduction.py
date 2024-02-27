import streamlit as st


def render_introduction():
    col1, col2 = st.columns((7, 1))
    col1.title("PIERATS - Productivity Island Expedition")
    col2.image("../pictures/logo.png")

    col1, col2, col3, col4 = st.columns((1, 4, 4, 1))
    with col2:
        st.image("../pictures/shelly_speech.png")
    with col3:
        st.markdown(
            f""" <br><br><br><p style="line-height:130%; font-size:2vw; color:white">AHOI 
            {st.session_state.player_name} ⛵️</p>
            <p style="line-height:130%; font-size: 1.5vw; color: white">I am Productivishelly,
            I will join you on your journey to better time management and show you different methods!
            You can click on the tabs above my head to check out how to start the game. I'll see you there!</p>""",
            unsafe_allow_html=True
        )
        # button to start the next quest
        if st.button("View Map"):
            st.session_state["temp"] = ""
            st.session_state.place = "map_1"
            st.rerun()


