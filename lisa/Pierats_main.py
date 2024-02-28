import streamlit as st
# import streamlit.components.v1 as components
from src.Helpers import sidebar_color
from src.Map import render_map_1, render_map_2, render_map_3, render_map_4, render_map_5, render_map_6, render_map_7
from src.Backpack import render_backpack_1, render_backpack_2, render_backpack_3, render_backpack_4
from src.Introduction import render_introduction
from src.Eisenhower_q1 import render_eisenhower_q1
from src.Eisenhower_method import render_eisenhower_method
from src.Eisenhower_q2 import render_eisenhower_q2
from src.Cornell_method import render_cornell_method
from src.Blurting_method import render_blurting_method
from src.Pomodoro_method import render_pomodoro_method
from src.Sail_away import render_sail_away

# Todo delete all commented out stuff at the bottom!!!

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

# set session state
if "place" not in st.session_state:
    st.session_state["place"] = "introduction"

col1, col2, col3 = st.columns((1, 4, 1))
with col2:
    logo = st.image("../pictures/logo_banner.png")
    welcome = st.empty()
    welcome.markdown(f""" <p style="font-family: serif; font-size:3vw; color:white; 
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
    main_text_container = st.empty()

col4, col5, col6 = st.columns((1, 4, 1))
with col5:
    st.text("")

if st.session_state.player_name != "":
    welcome.empty()
    divider.empty()
    input_text.empty()
    main_text_container.empty()
    player_name_container.empty()
    logo.empty()

    start = True

# START THE GAME

if start:

    # delete welcome
    welcome.empty()

    if st.session_state.place == "introduction":
        render_introduction()
        st.sidebar.markdown("Introduction")
    elif st.session_state.place == "map_1":
        render_map_1()
        st.sidebar.markdown("Introduction")
        st.sidebar.markdown("--> Map")
    elif st.session_state.place == "eisenhower_q1":
        render_eisenhower_q1()
        st.sidebar.markdown("Introduction")
        st.sidebar.markdown("First Quest")
    elif st.session_state.place == "map_2":
        render_map_2()
        st.sidebar.markdown("Introduction")
        st.sidebar.markdown("First Quest")
        st.sidebar.markdown("--> Map")
    elif st.session_state.place == "eisenhower_method":
        render_eisenhower_method()
        st.sidebar.markdown("Introduction")
        st.sidebar.markdown("First Quest")
        st.sidebar.markdown("Eisenhower Method")
    elif st.session_state.place == "map_3":
        render_map_3()
        st.sidebar.markdown("Introduction")
        st.sidebar.markdown("First Quest")
        st.sidebar.markdown("Eisenhower Method")
        st.sidebar.markdown("--> Map")
    elif st.session_state.place == "eisenhower_q2":
        render_eisenhower_q2()
        st.sidebar.markdown("Introduction")
        st.sidebar.markdown("First Quest")
        st.sidebar.markdown("Eisenhower Method")
        st.sidebar.markdown("Second Quest")
    elif st.session_state.place == "map_4":
        render_map_4()
        st.sidebar.markdown("Introduction")
        st.sidebar.markdown("First Quest")
        st.sidebar.markdown("Eisenhower Method")
        st.sidebar.markdown("Second Quest")
        st.sidebar.markdown("--> Map")
    elif st.session_state.place == "backpack_1":
        render_backpack_1()
        st.sidebar.markdown("Introduction")
        st.sidebar.markdown("First Quest")
        st.sidebar.markdown("Eisenhower Method")
        st.sidebar.markdown("Second Quest")
        st.sidebar.markdown("--> Backpack")
    elif st.session_state.place == "cornell_method":
        render_cornell_method()
        st.sidebar.markdown("Introduction")
        st.sidebar.markdown("First Quest")
        st.sidebar.markdown("Eisenhower Method")
        st.sidebar.markdown("Second Quest")
        st.sidebar.markdown("Cornell Method")
    elif st.session_state.place == "map_5":
        render_map_5()
        st.sidebar.markdown("Introduction")
        st.sidebar.markdown("First Quest")
        st.sidebar.markdown("Eisenhower Method")
        st.sidebar.markdown("Second Quest")
        st.sidebar.markdown("Cornell Method")
        st.sidebar.markdown("--> Map")
    elif st.session_state.place == "backpack_2":
        render_backpack_2()
        st.sidebar.markdown("Introduction")
        st.sidebar.markdown("First Quest")
        st.sidebar.markdown("Eisenhower Method")
        st.sidebar.markdown("Second Quest")
        st.sidebar.markdown("Cornell Method")
        st.sidebar.markdown("--> Backpack")
    elif st.session_state.place == "blurting_method":
        render_blurting_method()
        st.sidebar.markdown("Introduction")
        st.sidebar.markdown("First Quest")
        st.sidebar.markdown("Eisenhower Method")
        st.sidebar.markdown("Second Quest")
        st.sidebar.markdown("Cornell Method")
        st.sidebar.markdown("Blurting Method")
    elif st.session_state.place == "map_6":
        render_map_6()
        st.sidebar.markdown("Introduction")
        st.sidebar.markdown("First Quest")
        st.sidebar.markdown("Eisenhower Method")
        st.sidebar.markdown("Second Quest")
        st.sidebar.markdown("Cornell Method")
        st.sidebar.markdown("Blurting Method")
        st.sidebar.markdown("--> Map")
    elif st.session_state.place == "backpack_3":
        render_backpack_3()
        st.sidebar.markdown("Introduction")
        st.sidebar.markdown("First Quest")
        st.sidebar.markdown("Eisenhower Method")
        st.sidebar.markdown("Second Quest")
        st.sidebar.markdown("Cornell Method")
        st.sidebar.markdown("Blurting Method")
        st.sidebar.markdown("--> Backpack")
    elif st.session_state.place == "pomodoro_method":
        render_pomodoro_method()
        st.sidebar.markdown("Introduction")
        st.sidebar.markdown("First Quest")
        st.sidebar.markdown("Eisenhower Method")
        st.sidebar.markdown("Second Quest")
        st.sidebar.markdown("Cornell Method")
        st.sidebar.markdown("Blurting Method")
        st.sidebar.markdown("Pomodoro Method")
    elif st.session_state.place == "map_7":
        render_map_7()
        st.sidebar.markdown("Introduction")
        st.sidebar.markdown("First Quest")
        st.sidebar.markdown("Eisenhower Method")
        st.sidebar.markdown("Second Quest")
        st.sidebar.markdown("Cornell Method")
        st.sidebar.markdown("Blurting Method")
        st.sidebar.markdown("Pomodoro Method")
        st.sidebar.markdown("--> Map")
    elif st.session_state.place == "backpack_4":
        render_backpack_4()
        st.sidebar.markdown("Introduction")
        st.sidebar.markdown("First Quest")
        st.sidebar.markdown("Eisenhower Method")
        st.sidebar.markdown("Second Quest")
        st.sidebar.markdown("Cornell Method")
        st.sidebar.markdown("Blurting Method")
        st.sidebar.markdown("Pomodoro Method")
        st.sidebar.markdown("--> Backpack")
    elif st.session_state.place == "sail_away":
        render_sail_away()
        st.sidebar.markdown("Introduction")
        st.sidebar.markdown("First Quest")
        st.sidebar.markdown("Eisenhower Method")
        st.sidebar.markdown("Second Quest")
        st.sidebar.markdown("Cornell Method")
        st.sidebar.markdown("Blurting Method")
        st.sidebar.markdown("Pomodoro Method")
        st.sidebar.markdown("Sail Away")















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

