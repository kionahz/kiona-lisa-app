import streamlit as st
from helpers import sidebar_color

st.set_page_config(
    page_title="PIERATS - Productivity Island Expedition",
    page_icon="🐢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Set up sidebar
action = st.sidebar.radio("Hey sailor! What do you want to do?", ("Welcome",
                                                                  "First Quest",
                                                                  "Second Quest",
                                                                  "Third Quest",
                                                                  "Home",
                                                                  "Backpack"))
st.sidebar.image("../pictures/turtle.png")
sidebar_color()

# Update page based on sidebar selection
if action == "Welcome":
    col1, col2 = st.columns((6, 1))
    col1.title("PIERATS - Productivity Island Expedition")
    col2.image("../pictures/logo.png", width=120)
    col3, col4 = st.columns((3, 1))
    col3.image("../pictures/island.png")
    col4.markdown("Hey Sailor! Looks like you and your little brother stranded on a deserted island. Unfortunately, "
                  "your boat has broken down and you need new equipment. As you explore the individual quests, "
                  "you will find new materials and learn new things in order to survive and ultimately escape from the "
                  "island. Let's get started and begin with the first quest!")

elif action == "First Quest":
    st.image("../pictures/em_empty.png")
