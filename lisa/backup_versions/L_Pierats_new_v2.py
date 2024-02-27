import streamlit as st
from helpers_v2 import sidebar_color
from Eisenhower_Q3 import Eisenhower_quest3
from Eisenhower_Q2 import Eisenhower_quest2

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

st.sidebar.image("../pictures/shelly_ahoi.png")
# Set up sidebar
action = st.sidebar.radio("Hey sailor! What do you want to do?", ("Welcome",
                                                                  "First Quest 🏳️",
                                                                  "Second Quest 🔒",
                                                                  "Third Quest 🔒",
                                                                  "Home 🏠",
                                                                  "Backpack 🎒"))
sidebar_color()


# Update page based on sidebar selection
if action == "Welcome":
    col1, col2 = st.columns((6, 1))
    col1.title("PIERATS - Productivity Island Expedition")
    col2.image("../pictures/logo.png", width=120)
    col3, col4 = st.columns((3, 1))
    col3.image("../pictures/island_dschungel.png")
    col4.markdown("Hey Sailor! Looks like you and your little brother stranded on a deserted island. Unfortunately, "
                  "your boat has broken down and you need new equipment. As you explore the individual quests, "
                  "you will find new materials and learn new things in order to survive and ultimately escape from the "
                  "island. Let's get started and begin with the first quest!")

elif action == "First Quest 🏳️":
    st.markdown("First Quest")

elif action == "Second Quest 🔒":
    Eisenhower_quest2()


elif action == "Third Quest 🔒":
    Eisenhower_quest3()





elif action == "Backpack 🎒":
    col1, col2 = st.columns((5, 1))
    col1.title("Your Backpack")
    col2.image("../pictures/backpack.png")
    st.image("../pictures/open_backpack.png")
