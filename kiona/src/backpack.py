import streamlit as st


def render_backpack_1():
    col1, col2 = st.columns((5, 1))
    col1.title("Your Backpack")
    col2.image("../pictures/backpack.png")
    col3, col4, col5 = st.columns((4, 1, 2))
    with col3:
        st.image("../pictures/backpack_items_1.png")
    with col5:
        st.markdown(
            f""" <p style="line-height:130%; font-size: 1.5vw; color: white"><br><br><br>Great!<br><br>You 
                    collected the first item in your backpack. Its a saw that you will need to cut the wood to 
                    size.<br><br>Good job!</p>""",
            unsafe_allow_html=True
        )
    if st.button("Next Quest"):
        st.session_state["temp"] = ""
        st.session_state.place = "cornell_method"
        st.rerun()


def render_backpack_2():
    col1, col2 = st.columns((5, 1))
    col1.title("Your Backpack")
    col2.image("../pictures/backpack.png")
    col3, col4, col5 = st.columns((4, 1, 2))
    with col3:
        st.image("../pictures/backpack_items_2.png")
    with col5:
        st.markdown(
            f""" <p style="line-height:130%; font-size: 1.5vw; color: white"><br><br><br>Fantastic!<br><br>You collected 
                    the second item in your backpack. You can now use the hammer and nails to attach the cut wood to 
                    your ship to patch up the holes.<br><br>Keep up the good 
                    work!</p>""",
            unsafe_allow_html=True
        )
    if st.button("Next Quest"):
        st.session_state["temp"] = ""
        st.session_state.place = "blurting_method"
        st.rerun()


def render_backpack_3():
    col1, col2 = st.columns((5, 1))
    col1.title("Your Backpack")
    col2.image("../pictures/backpack.png")
    col3, col4, col5 = st.columns((4, 1, 2))
    with col3:
        st.image("../pictures/backpack_items_3.png")
    with col5:
        st.markdown(
            f""" <p style="line-height:130%; font-size: 1.5vw; color: white"><br><br><br>Amazing!<br><br>You collected the 
                    third item in your backpack. Its a fabric that can help you fix your sails.<br><br>Don't stop now, you are almost there!</p>""",
            unsafe_allow_html=True
        )
    if st.button("Next Quest"):
        st.session_state["temp"] = ""
        st.session_state.place = "pomodoro_method"
        st.rerun()


def render_backpack_4():
    col1, col2 = st.columns((5, 1))
    col1.title("Your Backpack")
    col2.image("../pictures/backpack.png")
    col3, col4, col5 = st.columns((4, 1, 2))
    with col3:
        st.image("../pictures/backpack_items_all.png")
    with col5:
        st.markdown(
            f""" <p style="line-height:130%; font-size: 1.5vw; color: white"><br><br><br>Awesome!<br><br>You collected 
                    the fourth and last item in your backpack. Its a rope that you can use to set and adjust the 
                    sails.<br><br>Good work. You can now finally repair your boat and sail away!</p>""",
            unsafe_allow_html=True
        )
    if st.button("Sail Away"):
        st.session_state["temp"] = ""
        st.session_state.place = "sail_away"
        st.rerun()
