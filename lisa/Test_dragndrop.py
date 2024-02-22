# Import the necessary modules from Streamlit Elements
from streamlit_elements import elements, mui, html
import streamlit as st

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
        mui.Paper("Search for a container (for food or water)", key="item1", style={"backgroundColor": "#452d20"})
        mui.Paper("Item 2", key="item2", style={"backgroundColor": "#452d20"})
        mui.Paper("Item 3", key="item3", style={"backgroundColor": "#452d20"})
        mui.Paper("Item 4", key="item4", style={"backgroundColor": "#452d20"})
        mui.Paper("Item 5", key="item5", style={"backgroundColor": "#452d20"})
        mui.Paper("Item 6", key="item6", style={"backgroundColor": "#452d20"})
        mui.Paper("Item 7", key="item7", style={"backgroundColor": "#452d20"})
        mui.Paper("Item 8", key="item8", style={"backgroundColor": "#452d20"})
        mui.Paper("Item 9", key="item9", style={"backgroundColor": "#452d20"})
        mui.Paper("Item 10", key="item10", style={"backgroundColor": "#452d20"})
