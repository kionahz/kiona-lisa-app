import streamlit as st
from helpers_v2 import sidebar_color, eisenhower_bg
from Eisenhower_Q3 import Eisenhower_quest3
from Eisenhower_Q2 import Eisenhower_quest2
from welcome_page_v2 import open_welcome
from backpack import open_backpack
from Blurting_method import blurting_method
from Cornell_method import cornell_method
from Pomodoro_technique import pomodoro_technique

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
                                                                  "First Quest 🏳️",
                                                                  "Second Quest 🔒",
                                                                  "Third Quest 🔒",
                                                                  "Cornell Method",
                                                                  "Blurting Method",
                                                                  "Pomodoro Technique",
                                                                  "Backpack 🎒"))
sidebar_color()


# Update page based on sidebar selection
if action == "Welcome":
    open_welcome()

elif action == "First Quest 🏳️":
    st.markdown("First Quest")

elif action == "Second Quest 🔒":
    Eisenhower_quest2()

elif action == "Third Quest 🔒":
    Eisenhower_quest3()

elif action == "Cornell Method":
    cornell_method()

elif action == "Blurting Method":
    blurting_method()

elif action == "Pomodoro Technique":
    pomodoro_technique()

elif action == "Backpack 🎒":
    open_backpack()
