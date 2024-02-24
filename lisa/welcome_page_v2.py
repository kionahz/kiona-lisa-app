import streamlit as st


def open_welcome():
    initial_sidebar_state = "collapsed"
    col1, col2 = st.columns((6, 1))
    col1.title("PIERATS - Productivity Island Expedition")
    col2.image("../pictures/logo.png", width=120)
    tab_titles = ["AHOI", "How to get started"]
    tab1, tab2 = st.tabs(tab_titles)

    with tab1:
        col1, col2, col3, col4 = st.columns((1, 4, 4, 1))
        with col2:
            st.image("../pictures/shelly_attemptspeech.png")
        with col3:
            st.markdown(
                f""" <br><br><p style="line-height:130%; font-size:2vw; color:white">AHOI Sailor! ⛵️️︎</p>
                <p style="line-height:130%; font-size: 1.5vw; color: white">I am Productivishelly, but you can call me Shelly!
                I will join you on your journey to better time managment and show you differnt methods!
                You can click on the tabs above my head to check out how to start the game. I'll see you there!</p>""",
                unsafe_allow_html=True
            )



    with tab2:
        col1, col2, col3, col4 = st.columns((1, 6, 5, 1))
        with col2:
            st.image("../pictures/island_dschungel.png")
        with col3:
            st.markdown(
                f""" <p style="line-height:130%; font-size: 2vw; color: white">OH NO, WHAT HAPPENED HERE?!</p> <p 
                style="line-height:130%; font-size: 1.5vw; color: white">Looks like you and your little brother 
                stranded on a deserted island. Unfortunately, your boat has broken down and you need new equipment. 
                As you explore the individual quests, you will find new materials and learn new things in order to 
                survive and ultimately escape from the island.\n Let's get started and begin with the first 
                quest!</p> """,
                unsafe_allow_html=True
            )
            # Toggle sidebar state between 'expanded' and 'collapsed'.
            if st.button("Let's play!"):
                st.session_state.sidebar_state = 'collapsed' if st.session_state.sidebar_state == 'expanded' else 'expanded'
                # Force an app rerun after switching the sidebar state.
                st.experimental_rerun()
