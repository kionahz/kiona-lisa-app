# First, import the elements you need
from streamlit_elements import elements, mui, html

with elements("dashboard"):

    # You can create a draggable and resizable dashboard using
    # any element available in Streamlit Elements.

    from streamlit_elements import dashboard

    # First, build a default layout for every element you want to include in your dashboard

    layout = [
        # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
        dashboard.Item("first_item", 1, 1, 2, 0.5, isResizable=False),
        dashboard.Item("second_item", 1, 2, 2, 0.5, isResizable=False),
        dashboard.Item("third_item", 1, 3, 2, 0.5, isResizable=False),
    ]

    # Next, create a dashboard layout using the 'with' syntax. It takes the layout
    # as first parameter, plus additional properties you can find in the GitHub links below.


    # If you want to retrieve updated layout values as the user move or resize dashboard items,
    # you can pass a callback to the onLayoutChange event parameter.

    def handle_layout_change(updated_layout):
        # You can save the layout in a file, or do anything you want with it.
        # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
        print(updated_layout)

    with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
        mui.Paper("Search for a container (for food or water)", key="first_item")
        mui.Paper("Build a fire", key="second_item")
        mui.Paper("Collect Shells", key="third_item")