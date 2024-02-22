import streamlit as st


def open_welcome():
    col1, col2 = st.columns((6, 1))
    col1.title("PIERATS - Productivity Island Expedition")
    col2.image("../pictures/logo.png", width=120)
    col3, col4 = st.columns((3, 1))
    col3.image("../pictures/island.png")
    col4.markdown("Hey Sailor! Looks like you and your little brother stranded on a deserted island. Unfortunately, "
                  "your boat has broken down and you need new equipment. As you explore the individual quests, "
                  "you will find new materials and learn new things in order to survive and ultimately escape from the "
                  "island. Let's get started and begin with the first quest!")