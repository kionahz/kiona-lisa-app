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

tab_titles = ["Pirate 1",
              "Pirate 2",
              "Pirate 3"
              ]


def render_pirate():
    tab1, tab2, tab3 = st.tabs(tab_titles)

    with tab1:
        col1, col2, col3, col4 = st.columns((x, y, y, x))
        with col2:
            st.image("../pictures/pirate.png")

        with col3:
            st.markdown("Speech 1")

    with tab2:
        col1, col2, col3, col4 = st.columns((x, y, y, x))
        with col2:
            st.image("../pictures/pirate.png")

        with col3:
            st.markdown("Speech 2")

    with tab3:
        col1, col2, col3, col4 = st.columns((x, y, y, x))
        with col2:
            st.image("../pictures/pirate.png")

        with col3:
            st.markdown("Speech 3")


render_pirate()
