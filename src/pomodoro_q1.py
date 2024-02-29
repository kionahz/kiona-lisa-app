import streamlit as st
import time


def render_pomodoro_q1():
    st.sidebar.progress(60)

    st.sidebar.markdown(f"""
    <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower First Try</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Method</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Applied</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Cornell Method</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Blurting Method</p>
        <p style="line-height: 100%; font-size: 1.3vw;"><strong>Quest First Try</strong></p>
    """, unsafe_allow_html=True)

    col_1, col_2 = st.columns((1, 4))
    with col_1:
        st.image("pictures/shelly.png")
    with col_2:
        st.title("Hurry up!")
        st.markdown(
            f""" <p style="line-height:130%; font-size: 1.5vw; color: white">As you just heard from the pirate: time 
            management is a crucial part of surviving this island. So let's have a look at your tasks again. Looks 
            like the pirate has already sorted them for you in the order that he would recommend. The only thing left 
            for you to do is to think about how much time you need for the individual tasks. Fill out the time slots 
            in hours and minutes by either selecting one of the suggested times or by writing them down in the slots. 
            <br>For example it takes me about 23 minutes to clean my shell. So I would put in 00:23 for this 
            task.</p>""",
            unsafe_allow_html=True
        )
        st.info("Continue once you are finished with the button on the bottom right.", icon="❕")

    st.divider()

    col3, col4 = st.columns((2, 3))

    with col3:
        st.markdown(
            f""" <p style="text-align:right; font-size:1.7vw; line-height: 194%;">Search for drinking water<br>Build 
            a Shelter<br>Serach for food</p> """,
            unsafe_allow_html=True)

    with col4:
        st.time_input('Label1', value=None, label_visibility="collapsed")
        st.time_input('Label2', value=None, label_visibility="collapsed")
        st.time_input('Label3', value=None, label_visibility="collapsed")

    col5, col6 = st.columns((2, 3))
    with col5:
        st.markdown(
            f""" <p style="text-align:right; font-size:1.7vw; line-height: 194%;">Collect Wood<br>Build a 
            fire<br>Search for a container (for water or food)</p> """,
            unsafe_allow_html=True)

    with col6:
        st.time_input('Label4', value=None, label_visibility="collapsed")
        st.time_input('Label5', value=None, label_visibility="collapsed")
        st.time_input('Label6', value=None, label_visibility="collapsed")

    col7, col8 = st.columns((2, 3))
    with col7:
        st.markdown(
            f""" <p style="text-align:right; font-size:1.7vw; line-height: 194%;">Build a weapon<br>Explore the 
            surroundings<br>Collect Shells</p> """,
            unsafe_allow_html=True)

    with col8:
        st.time_input('Label7', value=None, label_visibility="collapsed")
        st.time_input('Label8', value=None, label_visibility="collapsed")
        st.time_input('Label9', value=None, label_visibility="collapsed")

    col9, col10 = st.columns((2, 3))
    with col9:
        st.markdown(f""" <p style="text-align:right; font-size:1.7vw; line-height: 194%;">Watch the Sunset</p> """,
                    unsafe_allow_html=True)

    with col10:
        st.time_input('Label10', value=None, label_visibility="collapsed")

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("Continue"):
            st.session_state.place = "map_7"
            st.rerun()
