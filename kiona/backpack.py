import streamlit as st


def open_backpack():
    col5, col6 = st.columns((5, 1))
    col5.title("Your Backpack")
    col6.image("../pictures/backpack.png")
    st.image("../pictures/open_backpack.png")