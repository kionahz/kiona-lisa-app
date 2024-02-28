import streamlit as st

def welcome_page():
    col1, col2, col3 = st.columns((1, 4, 1))
    with col2:
        logo = st.image("../pictures/logo_banner.png")
        # welcome = st.empty()
        welcome = st.markdown(f""" <p style="font-family: serif; font-size:3vw; color:white; 
        text-align:center;"><strong>Welcome to PIERATS<br>the Productivity Island Expedition!</strong></p>""",
                              unsafe_allow_html=True)

        divider = st.divider()

        input_text = st.markdown(f"""<p style="line-height:130%; font-size: 1.5vw; color: white; text-align:center">Are 
        you ready for your adventure?<br>Let me know your name and hit enter to start the game</p>""",
                                 unsafe_allow_html=True)
        player_name_container = st.empty()
        player_name_container.text_input(
            "Text Input", key="player_name",
            label_visibility="hidden"
        )

    col4, col5, col6 = st.columns((1, 4, 1))
    with col5:
        st.text("")