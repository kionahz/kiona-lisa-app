import streamlit as st
import streamlit.components.v1 as components
# from streamlit_extras.stoggle import stoggle
# from streamlit_extras.metric_cards import style_metric_cards
# import time
# import random
import game_scenes_test
from Eisenhower_Q2 import Eisenhower_quest2
from Eisenhower_Q3 import Eisenhower_quest3


st.set_page_config(page_title="PIERATS", page_icon="turtle")

# variable responsible for checking if player provided his name and game can be started
start = False

# set session states
# if "level" not in st.session_state:
#    st.session_state["level"] = 0
if "place" not in st.session_state:
    st.session_state["place"] = "map_1"
if "temp" not in st.session_state:
    st.session_state["temp"] = ""
#if "counter" not in st.session_state:
#    st.session_state["counter"] = 0
#if "scenes_counter" not in st.session_state:
#    st.session_state["scenes_counter"] = {
#        "intro_counter": 0,
#        "cave_counter": 0,
#        "trip_counter": 0,
#        "elf_counter": 0,
#    }


welcome = st.empty()
welcome.title("Welcome to PIERATS, adventurer!")

# hero base statistics

player_name_container = st.empty()
player_name_container.text_input(
    "State your name and hit enter to start the game", key="player_name"
)
main_text_container = st.empty()


if st.session_state.player_name != "":
    player_name_container.empty()

    main_text_container.empty()
    start = True

# START THE GAME

if start:

    # delete welcome
    welcome.empty()

    if st.session_state.place == "map_1":
        game_scenes_test.map_1()
    elif st.session_state.place == "Eisenhower_Q2":
        Eisenhower_quest2()
    elif st.session_state.place == "Eisenhower_Q3":
        Eisenhower_quest3()



# this part of the code focuses input on text window
# please note that counter is required - for streamlit specific it does not work without it

#components.html(
#    f"""
#        <div>some hidden container</div>
#        <p>{st.session_state.counter}</p>
#        <script>
#            var input = window.parent.document.querySelectorAll("input[type=text]");
#            for (var i = 0; i < input.length; ++i) {{
#                input[i].focus();
#            }}
#    </script>
#    """,
#    height=0,
#)

#hide_streamlit_style = """
#            <style>
#            footer {visibility: hidden;}
#            </style>
#            """
#st.markdown(hide_streamlit_style, unsafe_allow_html=True)

