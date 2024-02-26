import streamlit as st
import game_def_test


def map_1():
    col1, col2 = st.columns((6, 1))
    col1.title("PIERATS - Productivity Island Expedition")
    col2.image("../pictures/logo.png", width=120)

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

    if st.button("Next Quest"):
        st.session_state["scenes_counter"]["intro_counter"] += 1
        st.session_state.place = "Eisenhower_Q2"
        game_def_test.temp_clear()
        st.rerun()


def Eisenhower_Q2():
    st.markdown("Eisenhower Q2")


def Eisenhower_Q3():
    st.markdown("Eisenhower Q3")
