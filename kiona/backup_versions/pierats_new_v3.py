import streamlit as st
from helpers_v2 import sidebar_color
from welcome_page import open_welcome
from second_quest import open_second_quest
from first_quest import open_first_quest
from backpack import open_backpack


# Define a variable to keep track of the current quest progress
current_quest = 0


# Function to set up the sidebar based on the current quest progress
def setup_sidebar(current_quest):
    if current_quest == 0:
        action = st.sidebar.radio("Hey sailor! What do you want to do?", ("Home 🏠",
                                                                          "First Quest 🏳️",
                                                                          "Backpack 🎒"))
    elif current_quest == 1:
        action = st.sidebar.radio("Hey sailor! What do you want to do?", ("Home 🏠",
                                                                          "First Quest 🏳️",
                                                                          "Second Quest 🔒",
                                                                          "Backpack 🎒"))
    elif current_quest == 2:
        action = st.sidebar.radio("Hey sailor! What do you want to do?", ("Home 🏠",
                                                                          "First Quest 🏳️",
                                                                          "Second Quest 🔒",
                                                                          "Third Quest 🔒",
                                                                          "Backpack 🎒"))
    sidebar_color()
    return action


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

st.sidebar.image("../pictures/turtle.png")

# Set up sidebar based on current quest progress
action = setup_sidebar(current_quest)

# Update page based on sidebar selection
if action == "Home 🏠":
    open_welcome()

elif action == "First Quest 🏳️":
    open_first_quest()
    current_quest = 1

elif action == "Second Quest 🔒":
    open_second_quest()
    current_quest = 2


elif action == "Backpack 🎒":
    open_backpack()

# Update sidebar based on current quest progress after each action
# action = setup_sidebar(current_quest)
