import streamlit as st
from helpers_v2 import sidebar_color, eisenhower_bg
from streamlit_elements import elements, mui, html

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

    with elements("dashboard"):


        # You can create a draggable and resizable dashboard using
        # any element available in Streamlit Elements.

        from streamlit_elements import dashboard

        # First, build a default layout for every element you want to include in your dashboard

        layout = [
            dashboard.Item("item1", 1, 1, 2, 0.5, isResizable=False),
            dashboard.Item("item2", 1, 2, 2, 0.5, isResizable=False),
            dashboard.Item("item3", 1, 3, 2, 0.5, isResizable=False),
            dashboard.Item("item4", 1, 4, 2, 0.5, isResizable=False),
            dashboard.Item("item5", 1, 5, 2, 0.5, isResizable=False),
            dashboard.Item("item6", 3, 1, 2, 0.5, isResizable=False),
            dashboard.Item("item7", 3, 2, 2, 0.5, isResizable=False),
            dashboard.Item("item8", 3, 3, 2, 0.5, isResizable=False),
            dashboard.Item("item9", 3, 4, 2, 0.5, isResizable=False),
            dashboard.Item("item10", 3, 5, 2, 0.5, isResizable=False),
        ]

        # Create the dashboard layout using the dashboard.Grid component
        with dashboard.Grid(layout):
            # Create ten draggable elements with text content
            mui.Paper("Item 1", key="item1", style={"backgroundColor": "#452d20"})
            mui.Paper("Item 2", key="item2", style={"backgroundColor": "#452d20"})
            mui.Paper("Item 3", key="item3", style={"backgroundColor": "#452d20"})
            mui.Paper("Item 4", key="item4", style={"backgroundColor": "#452d20"})
            mui.Paper("Item 5", key="item5", style={"backgroundColor": "#452d20"})
            mui.Paper("Item 6", key="item6", style={"backgroundColor": "#452d20"})
            mui.Paper("Item 7", key="item7", style={"backgroundColor": "#452d20"})
            mui.Paper("Item 8", key="item8", style={"backgroundColor": "#452d20"})
            mui.Paper("Item 9", key="item9", style={"backgroundColor": "#452d20"})
            mui.Paper("Item 10", key="item10", style={"backgroundColor": "#452d20"})




elif action == "Backpack 🎒":
    col1, col2 = st.columns((5, 1))
    col1.title("Your Backpack")
    col2.image("../pictures/backpack.png")
    st.image("../pictures/open_backpack.png")
