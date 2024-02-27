import streamlit as st
# import streamlit.components.v1 as components
from pages.helpers import sidebar_color
from pages.map import render_map_1, render_map_2, render_map_3, render_map_4, render_map_5, render_map_6
from pages.backpack import render_backpack_1, render_backpack_2, render_backpack_3, render_backpack_4
from pages.introduction import render_introduction
from pages.eisenhower_q1 import render_eisenhower_q1
from pages.eisenhower_method import render_eisenhower_method
from pages.eisenhower_q2 import render_eisenhower_q2
from pages.cornell_method import render_cornell_method
from pages.blurting_method import render_blurting_method
from pages.pomodoro_method import render_pomodoro_method
from pages.sail_away import render_sail_away


st.set_page_config(
    page_title="PIERATS - Productivity Island Expedition",
    page_icon="🐢",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# Kiona and Lisa's Game!"
    }
)

st.sidebar.image("../pictures/shelly_ahoi.png")
sidebar_color()

# variable responsible for checking if player provided his name and game can be started
start = False

# set session states
if "place" not in st.session_state:
    st.session_state["place"] = "introduction"
if "temp" not in st.session_state:
    st.session_state["temp"] = ""


welcome = st.empty()
welcome.title("Welcome to PIERATS the Productivity Island Expedition!")

# hero base statistics

player_name_container = st.empty()
player_name_container.text_input(
    "If you are ready for this crazy adventure enter your name and hit enter to start the game", key="player_name"
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

    if st.session_state.place == "introduction":
        render_introduction()
    elif st.session_state.place == "eisenhower_q1":
        render_eisenhower_q1()
    elif st.session_state.place == "map_1":
        render_map_1()
    elif st.session_state.place == "eisenhower_method":
        render_eisenhower_method()
    elif st.session_state.place == "map_2":
        render_map_2()
    elif st.session_state.place == "eisenhower_q2":
        render_eisenhower_q2()
    elif st.session_state.place == "map_3":
        render_map_3()
    elif st.session_state.place == "backpack_1":
        render_backpack_1()
    elif st.session_state.place == "cornell_method":
        render_cornell_method()
    elif st.session_state.place == "map_4":
        render_map_4()
    elif st.session_state.place == "backpack_2":
        render_backpack_2()
    elif st.session_state.place == "blurting_method":
        render_blurting_method()
    elif st.session_state.place == "map_5":
        render_map_5()
    elif st.session_state.place == "backpack_3":
        render_backpack_3()
    elif st.session_state.place == "pomodoro_method":
        render_pomodoro_method()
    elif st.session_state.place == "map_6":
        render_map_6()
    elif st.session_state.place == "backpack_4":
        render_backpack_4()
    elif st.session_state.place == "sail_away":
        render_sail_away()















#if "counter" not in st.session_state:
#    st.session_state["counter"] = 0
#if "scenes_counter" not in st.session_state:
#    st.session_state["scenes_counter"] = {
#        "intro_counter": 0,
#        "cave_counter": 0,
#        "trip_counter": 0,
#        "elf_counter": 0,
#    }


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

