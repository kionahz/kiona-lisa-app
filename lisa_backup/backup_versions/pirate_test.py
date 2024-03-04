import streamlit as st

# set up streamlit page configuration
st.set_page_config(
    page_title="PIERATS - Productivity Island Expedition",
    page_icon="🐢",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "#Kiona and Lisa's Game!"
    }
)

x = 1
y = 4


def render_pirate():

        col1, col2, col3, col4 = st.columns((x, y, y, x))
        with col2:
            st.image("../pictures/pirate.png")

        with col3:
            speech1_container = st.empty()
            speech1_container.markdown("Speech 1")
            next_button1_container = st.empty()
            next_button1_container.button("Next", key="button1_key")

            if next_button1_container:
                speech1_container.empty()
                next_button1_container.empty()
                next_button2_container = st.empty()
                next_button2_container.button("Next", key="button2_key")
                speech2_container = st.empty()
                speech2_container.markdown("Speech 2")

            if next_button2_container:
                speech2_container.empty()
                next_button2_container.empty()
                speech3_container = st.empty()
                speech3_container.markdown("Speech 3")


render_pirate()
