import streamlit as st

st.set_page_config(
    page_title="PIERATS - Productivity Island Expedition",
    page_icon="🐢",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "# Kiona and Lisa's Game!"
    }
)

# Define the tasks
tasks = [
    "Search for a container e.g. for food or water",
    "Build a fire",
    "Build Shelter",
    "Collect Shells",
    "Collect Wood",
    "Watch the Sunset",
    "Search for drinking water",
    "Search for Food",
    "Build a Weapon",
    "Explore the surroundings",
]

# Initialize a dictionary to store tomato emojis for each task
if 'tomatoes' not in st.session_state:
    st.session_state.tomatoes = {task: [] for task in tasks}

col3, col4, col5, col6 = st.columns((2, 1,1, 3))
with col4:
    # Add buttons to add tomatoes for each task
    for task in tasks:
        if st.button(f"{task} + "):
            st.session_state.tomatoes[task].append("🍅")

with col5:
    # Add buttons to remove tomatoes for each task
    for task in tasks:
        if st.button(f"{task} - "):
            if st.session_state.tomatoes[task]:
                st.session_state.tomatoes[task].pop()

with col6:
    # Display the tomato emojis for each task
    for task in tasks:
        st.text(f"{task}: {' '.join(st.session_state.tomatoes[task])}")
