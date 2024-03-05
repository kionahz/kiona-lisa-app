import streamlit as st


def render_pomodoro_q2():
    st.sidebar.progress(80)

    st.sidebar.markdown(f"""
    <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower First Try</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Method</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Applied</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Cornell Method</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Blurting Method</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Pomodoro First Try</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Pomodoro Method</p>
        <p style="line-height: 100%; font-size: 1.3vw;"><strong>Pomodoro Applied</strong></p>
    """, unsafe_allow_html=True)

    col_1, col_2 = st.columns((1, 4))
    with col_1:
        st.image("../pictures/shelly.png")
    with col_2:
        st.title("Let's talk tomatoes!")
        st.markdown(
            f""" <p style="line-height:130%; font-size: 1.5vw; color: white">Now you learned everything about the 
            Pomodoro Method. Shall we have another look at the time management of your tasks? Let's try to break down 
            your tasks in pomodoros. For example I would choose one Pomodoro for the time I need for cleaning my 
            shell. </p>""",
            unsafe_allow_html=True
        )
        st.info("Continue once you are finished with the button on the bottom right.", icon="❕")

    st.divider()
    st.markdown(f""" <p style="text-align: center; line-height:130%; font-size: 1.5vw; color: white">🍅  =  1 
    Pomodoro  =  25 minutes of focused work session  +  5 minutes break</p> """, unsafe_allow_html=True)

    col3, col4, col5, col6 = st.columns((2, 1, 1, 3))
    with col3:
        st.markdown(
            f""" <p style="text-align:right; font-size:1.7vw; line-height: 194%;">Search for drinking water<br>Build 
            a Shelter<br>Serach for food<br>Collect Wood<br>Build a fire<br>Search for a container (for water or 
            food)<br>Build a weapon<br>Explore the surroundings<br>Collect Shells<br>Watch the Sunset</p> """,
            unsafe_allow_html=True)
    with col4:
        # Initialize the tomatoes list in the session state
        if 'tomatoes' not in st.session_state:
            st.session_state.tomatoes = []

        # Add button to add a tomato
        if st.button("+ Add 🍅"):
            st.session_state.tomatoes.append("🍅")

    with col5:
        # Add button to remove a tomato
        if st.button("- Remove 🍅"):
            if st.session_state.tomatoes:
                st.session_state.tomatoes.pop()

    with col6:
        # Display the tomato emojis
        st.text(" ".join(st.session_state.tomatoes))

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("Continue"):
            st.session_state.place = "map_9"
            st.rerun()
