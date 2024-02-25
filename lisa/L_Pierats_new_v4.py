import streamlit as st
from helpers_v2 import sidebar_color
from Eisenhower_Q3 import Eisenhower_quest3
from Eisenhower_Q2 import Eisenhower_quest2
from welcome_page_v2 import open_welcome
from backpack import open_backpack_1, open_backpack_2, open_backpack_3, open_backpack_4
from Blurting_method import blurting_method
from Cornell_method import cornell_method
from Pomodoro_technique import pomodoro_technique
from finish_page import open_finish

# Initialize a session state variable that tracks the sidebar state (either 'expanded' or 'collapsed').
if 'sidebar_state' not in st.session_state:
    st.session_state.sidebar_state = 'collapsed'

st.set_page_config(
    page_title="PIERATS - Productivity Island Expedition",
    page_icon="🐢",
    layout="wide",
    initial_sidebar_state=st.session_state.sidebar_state,
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# Kiona and Lisa's Game!"
    }
)

st.sidebar.image("../pictures/shelly_ahoi.png")
# Set up sidebar
action = st.sidebar.radio("Hey sailor! What do you want to do?", ("Welcome",
                                                                  "First Quest",
                                                                  "Second Quest",
                                                                  "Third Quest",
                                                                  "Backpack 1",
                                                                  "Cornell Method",
                                                                  "Backpack 2",
                                                                  "Blurting Method",
                                                                  "Backpack 3",
                                                                  "Pomodoro Technique",
                                                                  "Backpack 4",
                                                                  "Finish"))
sidebar_color()

# Update page based on sidebar selection
if action == "Welcome":
    open_welcome()

elif action == "First Quest":
    st.markdown("First Quest")

elif action == "Second Quest":
    Eisenhower_quest2()

elif action == "Third Quest":
    Eisenhower_quest3()

elif action == "Backpack 1":
    open_backpack_1()

elif action == "Cornell Method":
    cornell_method()

elif action == "Backpack 2":
    open_backpack_2()

elif action == "Blurting Method":
    blurting_method()

elif action == "Backpack 3":
    open_backpack_3()

elif action == "Pomodoro Technique":
    pomodoro_technique()

elif action == "Backpack 4":
    open_backpack_4()

elif action == "Finish":
    open_finish()
