import streamlit as st
from helpers_v2 import sidebar_color
from welcome_page import open_welcome
from second_quest import open_second_quest
from first_quest import open_first_quest
from backpack import open_backpack


# Define a variable to keep track of the current quest progress
current_quest = 0

sidebar_options = {
    0: ["Home ", "First Quest ", "Backpack "],
    1: ["Home ", "First Quest ", "Second Quest ", "Backpack "],
    2: ["Home ", "First Quest ", "Second Quest ", "Third Quest ", "Backpack "],
    4: ["Home ", "First Quest ", "Backpack "]
}


# Function to set up the sidebar based on the current quest progress
def setup_sidebar(current_quest):
    # st.sidebar.empty()
    # action_widgets = st.sidebar.radio("Hey sailor! What do you want to do?", options, key=key)
    # action_widget = action_widgets.get(f"sidebar_radio_{current_quest}")
    # if action_widget:
    #     action_widget.empty()

    options = sidebar_options.get(current_quest)
    if options is None:
        # Handle invalid quest progress (e.g., negative values)
        return None

    # Generate a unique key based on current_quest
    key = f"sidebar_radio_{current_quest}"

    action = st.sidebar.radio("Hey sailor! What do you want to do?", options, key=key)
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
if action == "Home ":
    open_welcome()
    current_quest = 0
    setup_sidebar(current_quest)

elif action == "First Quest ":
    open_first_quest()
    current_quest = 1
    setup_sidebar(current_quest)

elif action == "Second Quest ":
    current_quest = 2
    setup_sidebar(current_quest)

elif action == "Backpack ":
    open_backpack()
    current_quest = 4
    setup_sidebar(current_quest)


