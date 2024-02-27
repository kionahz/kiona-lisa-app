import streamlit as st


def render_map_1():
    col1, col2 = st.columns((5, 1))
    col1.title("The Map")
    col2.image("../pictures/logo.png")
    col3, col4, col5 = st.columns((4, 1, 2))
    with col3:
        st.image("../pictures/island_02.png")
    with col5:
        # button to start the next quest
        if st.button("Explanation Method"):
            st.session_state["temp"] = ""
            st.session_state.place = "eisenhower_method"
            st.rerun()


def render_map_2():
    col1, col2 = st.columns((5, 1))
    col1.title("The Map")
    col2.image("../pictures/logo.png")
    col3, col4, col5 = st.columns((4, 1, 2))
    with col3:
        st.image("../pictures/island_03.png")
    with col5:
        # button to start the next quest
        if st.button("Next Quest"):
            st.session_state["temp"] = ""
            st.session_state.place = "eisenhower_q2"
            st.rerun()


def render_map_3():
    col1, col2 = st.columns((5, 1))
    col1.title("The Map")
    col2.image("../pictures/logo.png")
    col3, col4, col5 = st.columns((4, 1, 2))
    with col3:
        st.image("../pictures/island_04.png")
    with col5:
        # button to show the backpack
        if st.button("View Backpack"):
            st.session_state["temp"] = ""
            st.session_state.place = "backpack_1"
            st.rerun()
        # button to start the next quest
        if st.button("Next Quest"):
            st.session_state["temp"] = ""
            st.session_state.place = "cornell_method"
            st.rerun()


def render_map_4():
    col1, col2 = st.columns((5, 1))
    col1.title("The Map")
    col2.image("../pictures/logo.png")
    col3, col4, col5 = st.columns((4, 1, 2))
    with col3:
        st.image("../pictures/island_05.png")
    with col5:
        # button to start the next quest
        if st.button("View Backpack"):
            st.session_state["temp"] = ""
            st.session_state.place = "backpack_2"
            st.rerun()
        # button to start the next quest
        if st.button("Next Quest"):
            st.session_state["temp"] = ""
            st.session_state.place = "blurting_method"
            st.rerun()


def render_map_5():
    col1, col2 = st.columns((5, 1))
    col1.title("The Map")
    col2.image("../pictures/logo.png")
    col3, col4, col5 = st.columns((4, 1, 2))
    with col3:
        st.image("../pictures/island_06.png")
    with col5:
        # button to start the next quest
        if st.button("View Backpack"):
            st.session_state["temp"] = ""
            st.session_state.place = "backpack_3"
            st.rerun()
        # button to start the next quest
        if st.button("Next Quest"):
            st.session_state["temp"] = ""
            st.session_state.place = "pomodoro_method"
            st.rerun()


def render_map_6():
    col1, col2 = st.columns((5, 1))
    col1.title("The Map")
    col2.image("../pictures/logo.png")
    col3, col4, col5 = st.columns((4, 1, 2))
    with col3:
        st.image("../pictures/island_07.png")
    with col5:
        # button to start the next quest
        if st.button("View Backpack"):
            st.session_state["temp"] = ""
            st.session_state.place = "backpack_4"
            st.rerun()
