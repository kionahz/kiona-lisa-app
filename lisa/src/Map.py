import streamlit as st


def render_map_1():
    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/island_01.png")
    with col2:
        st.markdown(
            f""" <p style="line-height:130%; font-size: 2vw; color: white">OH NO, WHAT HAPPENED HERE?!</p> <p 
            style="line-height:130%; font-size: 1.5vw; color: white">Looks like you and your little brother stranded 
            on a deserted island. Unfortunately, your boat has broken down and you need new equipment. As you explore 
            the individual quests, you will find new materials in your backpack after finishing quests that relate to 
            one method. You will learn new things in order to survive and ultimately escape from the island.<br> 
            Let's get started and begin with the first quest!</p> """,
            unsafe_allow_html=True
        )
        st.image("../pictures/shelly_with_backpack.png", width=300)

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("View Backpack"):
            st.session_state.place = "backpack_empty"
            st.rerun()


def render_map_2():
    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/island_02.png")
    with col2:
        st.image("../pictures/shelly_with_backpack.png", width=300)

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("View Backpack"):
            st.session_state.place = "backpack_1"
            st.rerun()


def render_map_3():
    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/island_03.png")
    with col2:
        st.image("../pictures/shelly_with_backpack.png", width=300)

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("View Backpack"):
            st.session_state.place = "backpack_2"
            st.rerun()


def render_map_4():
    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/island_04.png")
    with col2:
        st.image("../pictures/shelly_with_backpack.png", width=300)

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("View Backpack"):
            st.session_state.place = "backpack_3"
            st.rerun()


def render_map_5():
    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/island_05.png")
    with col2:
        st.image("../pictures/shelly_with_backpack.png", width=300)

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("View Backpack"):
            st.session_state.place = "backpack_4"
            st.rerun()


def render_map_6():
    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/island_06.png")
    with col2:
        st.image("../pictures/shelly_with_backpack.png", width=300)

    cola, colb = st.columns((8, 1))
    with colb:
        # button to start the next quest
        if st.button("View Backpack"):
            st.session_state.place = "backpack_5"
            st.rerun()


def render_map_7():
    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/island_07.png")
    with col2:
        st.image("../pictures/shelly_with_backpack.png", width=300)

    cola, colb = st.columns((8, 1))
    with colb:
        # button to start the next quest
        if st.button("View Backpack"):
            st.session_state.place = "backpack_6"
            st.rerun()


def render_map_8():
    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/island_08.png")
    with col2:
        st.image("../pictures/shelly_with_backpack.png", width=300)

    cola, colb = st.columns((8, 1))
    with colb:
        # button to start the next quest
        if st.button("View Backpack"):
            st.session_state.place = "backpack_7"
            st.rerun()


def render_map_9():
    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/island_09.png")
    with col2:
        st.image("../pictures/shelly_with_backpack.png", width=300)

    cola, colb = st.columns((8, 1))
    with colb:
        # button to start the next quest
        if st.button("View Backpack"):
            st.session_state.place = "backpack_8"
            st.rerun()
