import streamlit as st
# from helpers import sidebar_color
from welcome_page_v2 import open_welcome
# from second_quest import open_second_quest
# from first_quest import open_first_quest
# from backpack import open_backpack

st.set_page_config(
    page_title="PIERATS - Productivity Island Expedition",
    page_icon="🐢",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# Kiona and Lisa's Game!"
    }
)

sidebar_options = {
    0: ["Home ", "First Quest "],
    1: ["Home ", "First Quest ", "Second Quest "],
    2: ["Home ", "First Quest ", "Second Quest ", "Third Quest "],
    3: ["Home ", "First Quest ", "Second Quest ", "Third Quest ", "Backpack "],
    4: ["Home ", "First Quest ", "Second Quest ", "Third Quest ", "Backpack "]
}

# Define a variable to keep track of the current quest progress
current_quest = 0
# action = "First Quest "

# Function to set up the sidebar based on the current quest progress

def render_sidebar(current_quest):
    ## Jana's Example

    # Generate a unique key based on current_quest
    options = sidebar_options[current_quest]
    # key = f"sidebar_radio_{current_quest}"
    print(current_quest)
    print(options)

    if options is None:
        # Handle invalid quest progress (e.g., negative values)
        return None

    if current_quest == 0:
        quest_radio = st.sidebar.radio("Hey sailor! What do you want to do?", options)
        open_welcome()
        current_quest += 1
        st.sidebar.empty()

    if current_quest == 1:
        quest_radio = st.sidebar.radio("Hey sailor! What do you want to do?", options, index=1)
        current_quest += 1
        st.sidebar.empty()

    if current_quest == 2:
        quest_radio = st.sidebar.radio("Hey sailor! What do you want to do?", options, index=2)

    if current_quest == 3:
        quest_radio = st.sidebar.radio("Hey sailor! What do you want to do?", options, index=3)

    if current_quest == 4:
        quest_radio = st.sidebar.radio("Hey sailor! What do you want to do?", options, index=4)

    # todo globalise this so we can destroy it after each action step below
    return current_quest

# Set up sidebar based on current quest progress
action = render_sidebar(current_quest)
