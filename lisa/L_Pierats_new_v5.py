import streamlit as st
from pages.helpers_v2 import sidebar_color
from pages.Eisenhower_Q3 import Eisenhower_quest3
from pages.Eisenhower_Q2 import Eisenhower_quest2
from pages.welcome_page_v2 import open_welcome
from pages.backpack import open_backpack_1, open_backpack_2, open_backpack_3, open_backpack_4
from pages.Blurting_method import blurting_method
from pages.Cornell_method import cornell_method
from pages.Pomodoro_technique import pomodoro_technique
from pages.finish_page import open_finish

# Initialize a session state variable that tracks the sidebar state (either 'expanded' or 'collapsed').
if 'sidebar_state' not in st.session_state:
    st.session_state.sidebar_state = 'collapsed'

st.set_page_config(
    page_title="PIERATS - Productivity Island Expedition",
    page_icon="🐢",
    layout="wide",
    initial_sidebar_state=st.session_state.sidebar_state,
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# Kiona and Lisa's Game!"
    }
)

st.sidebar.image("../pictures/shelly_ahoi.png")
# Set up sidebar

open_welcome()

if st.sidebar.button("Welcome"):
    open_welcome()
if st.sidebar.button("First Quest"):
    st.markdown("First Quest")
if st.sidebar.button("Second Quest"):
    st.switch_page("pagesy/Eisenhower_Q2.py")
if st.sidebar.button("Third Quest"):
    Eisenhower_quest3()
if st.sidebar.button("Backpack 1"):
    open_backpack_1()
if st.sidebar.button("Cornell Method"):
    cornell_method()
if st.sidebar.button("Backpack 2"):
    open_backpack_2()
if st.sidebar.button("Blurting Method"):
    blurting_method()
if st.sidebar.button("Backpack 3"):
    open_backpack_3()
if st.sidebar.button("Pomodoro Technique"):
    pomodoro_technique()
if st.sidebar.button("Backpack 4"):
    open_backpack_4()
if st.sidebar.button("Finish"):
    open_finish()

sidebar_color()




