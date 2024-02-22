import streamlit as st
from helpers_v2 import sidebar_color
from welcome_page import open_welcome
from first_quest import open_first_quest


st.set_page_config(
    page_title="PIERATS - Productivity Island Expedition",
    page_icon="🐢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define a variable to keep track of the current quest progress
current_quest = 0



# Function to set up the sidebar based on the current quest progress
def setup_sidebar(current_quest):
    global action
    if current_quest == 0:
        action = st.sidebar.radio("Hey sailor! What do you want to do?", ("Welcome",
                                                                          "First Quest 🏳️",
                                                                          "Home 🏠",
                                                                          "Backpack "))
    elif current_quest == 1:
        action = st.sidebar.radio("Hey sailor! What do you want to do?", ("Welcome",
                                                                          "First Quest 🏳️",
                                                                          "Second Quest 🔒",
                                                                          "Home 🏠",
                                                                          "Backpack "))
    elif current_quest == 2:
        action = st.sidebar.radio("Hey sailor! What do you want to do?", ("Welcome",
                                                                          "First Quest 🏳️",
                                                                          "Second Quest 🔒",
                                                                          "Third Quest 🔒",
                                                                          "Home 🏠",
                                                                          "Backpack "))
    sidebar_color()
    return action


st.sidebar.image("../pictures/turtle.png")

# Set up sidebar based on current quest progress
action = setup_sidebar(current_quest)

# Update page based on sidebar selection
if action == "Welcome":
    open_welcome()

elif action == "First Quest 🏳️":
    open_first_quest()


elif action == "Backpack ":
    col5, col6 = st.columns((5, 1))
    col5.title("Your Backpack")
    col6.image("../pictures/backpack.png")
    st.image("../pictures/open_backpack.png")
