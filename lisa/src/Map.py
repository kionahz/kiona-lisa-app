import streamlit as st


def render_map_1():
    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/island_01.png")
    with col2:
        st.markdown(  # TODO markdown
            f""" <p style="line-height:130%; font-size: 2vw; color: white">OH NO, WHAT HAPPENED HERE?!</p> <p 
            style="line-height:130%; font-size: 1.5vw; color: white">Looks like you and your little brother stranded 
            on a deserted island. Unfortunately, your boat has broken down and you need new equipment to repair it. 
            As you explore the individual quests, you will be rewarded with new materials which you can find in your 
            backpack.<br> Also, you can always check your current game progress in the sidebar on the left.<br> Have a 
            quick look into your backpack before we start!</p> """,
            unsafe_allow_html=True
        )
        st.image("../pictures/shelly_with_backpack.png", width=300)

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("Open Backpack"):  # TODO
            st.session_state.place = "backpack_empty"
            st.rerun()


def render_map_2():
    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/island_02.png")
    with col2:
        st.markdown(f""" <p style="line-height:130%; font-size:2vw; color:white">Look! There is a way through the 
        jungle!</p><p style="line-height:150%; font-size: 1.5vw; color: white">When finishing quests you not only get 
        new equipment but can also find your way back to your boat. Stay strong sailor!</p>""", unsafe_allow_html=True)
        st.image("../pictures/shelly_with_backpack.png", width=300)  # TODO

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("Open Backpack"):  # TODO
            st.session_state.place = "backpack_1"
            st.rerun()


def render_map_3():
    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/island_03.png")
    with col2:
        st.markdown(f""" <p style="line-height:130%; font-size:2vw; color:white">That's the way to go!</p><p 
        style="line-height:150%; font-size: 1.5vw; color: white">Even more jungle has cleared. Keep going, 
        you have quite the way in front of you!</p>""", unsafe_allow_html=True)  # TODO
        st.image("../pictures/shelly_with_backpack.png", width=300)

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("Open Backpack"):  # TODO
            st.session_state.place = "backpack_2"
            st.rerun()


def render_map_4():
    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/island_04.png")
    with col2:
        st.markdown(f""" <p style="line-height:130%; font-size:2vw; color:white">You did a great job applying the 
        Eisenhower method!</p><p style="line-height:150%; font-size: 1.5vw; color: white">Look how much of the way 
        has cleared!<br>Have you checked your backpack yet?</p>""", unsafe_allow_html=True)  # TODO
        st.image("../pictures/shelly_with_backpack.png", width=300)

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("Open Backpack"):  # TODO
            st.session_state.place = "backpack_3"
            st.rerun()


def render_map_5():
    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/island_05.png")
    with col2:
        st.markdown(f""" <p style="line-height:130%; font-size:2vw; color:white">Now you know everything about the 
        Cornell method!</p><p style="line-height:150%; font-size: 1.5vw; color: white"> Looks like you made it 
        halfway through the jungle!</p>""", unsafe_allow_html=True)  # TODO
        st.image("../pictures/shelly_with_backpack.png", width=300)

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("Open Backpack"):  # TODO
            st.session_state.place = "backpack_4"
            st.rerun()


def render_map_6():
    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/island_06.png")
    with col2:
        st.markdown(f""" <p style="line-height:130%; font-size:2vw; color:white">Now you know everything about the 
        Blurting method!</p><p style="line-height:150%; font-size: 1.5vw; color: white">Did you know, the best way to 
        use it, is to combine it with the Cornell method?<br>Also have you noticed your progress on the island?</p>""",
                    unsafe_allow_html=True)  # TODO
        st.image("../pictures/shelly_with_backpack.png", width=300)

    cola, colb = st.columns((8, 1))
    with colb:
        # button to start the next quest
        if st.button("Open Backpack"):  # TODO
            st.session_state.place = "backpack_5"
            st.rerun()


def render_map_7():
    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/island_07.png")
    with col2:
        st.markdown(f""" <p style="line-height:130%; font-size:2vw; color:white">Well done!</p><p 
        style="line-height:150%; font-size: 1.5vw; color: white">I knew you would do well in this quest. Would you 
        like to get to know a method that will make you a pro in time management?<br>But first let's check out your 
        new equipment!</p>""",
                    unsafe_allow_html=True)  # TODO
        st.image("../pictures/shelly_with_backpack.png", width=300)

    cola, colb = st.columns((8, 1))
    with colb:
        # button to start the next quest
        if st.button("Open Backpack"):  # TODO
            st.session_state.place = "backpack_6"
            st.rerun()


def render_map_8():
    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/island_08.png")
    with col2:
        st.markdown(f""" <p style="line-height:130%; font-size:2vw; color:white">Bravissimo!</p><p 
        style="line-height:150%; font-size: 1.5vw; color: white">When hearing all these italian foods I have to show 
        off some of my Italian.<br> Wow, have a look on the island! I think I can already see some light coming 
        through the jungle. Don't stop now, you almost made it!</p>""",
                    unsafe_allow_html=True)  # TODO
        st.image("../pictures/shelly_with_backpack.png", width=300)

    cola, colb = st.columns((8, 1))
    with colb:
        # button to start the next quest
        if st.button("Open Backpack"):  # TODO
            st.session_state.place = "backpack_7"
            st.rerun()


def render_map_9():
    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/island_09.png")
    with col2:
        st.markdown(f""" <p style="line-height:130%; font-size:2vw; color:white">You did it!</p><p 
        style="line-height:150%; font-size: 1.5vw; color: white">Amazing job applying the Pomodoro method.<br>Look, the jungle has cleared all the way and you and your 
        brother can return to your boat.<br>Wow, and I think your backpack is getting quite heavy. Let's check it 
        out!</p>""",
                    unsafe_allow_html=True)  # TODO
        st.image("../pictures/shelly_with_backpack.png", width=300)

    cola, colb = st.columns((8, 1))
    with colb:
        # button to start the next quest
        if st.button("Open Backpack"):  # TODO
            st.session_state.place = "backpack_8"
            st.rerun()
