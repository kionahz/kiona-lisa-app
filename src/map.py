import streamlit as st
import time


def render_map_1():
    progress_10 = st.sidebar.progress(0)
    for percent_complete_10 in range(1, 10):
        time.sleep(0.01)
        progress_10.progress(percent_complete_10)

    st.sidebar.markdown(f"""
            <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p>
            <p style="padding-left: 30px; line-height:100%; font-size: 1.3vw;"><strong>Map</strong></p>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("pictures/island_01.png")
    with col2:
        st.markdown(
            f""" <p style="line-height:130%; font-size: 2vw; color: white">OH NO, WHAT HAPPENED HERE?!</p> <p 
            style="line-height:130%; font-size: 1.5vw; color: white">Looks like you and your little brother stranded 
            on a deserted island. Unfortunately, your boat has broken down and you need new equipment to repair it. 
            As you explore the individual quests, you will be rewarded with new equipment which you can find in your 
            backpack.<br> Also, you can always check your current game progress in the sidebar on the left.<br> Have a 
            quick look into your backpack before we start!</p> """,
            unsafe_allow_html=True
        )
        st.image("pictures/shelly_with_backpack.png", width=300)

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("Open Backpack"):
            st.session_state.place = "backpack_empty"
            st.rerun()


def render_map_2():
    progress_20 = st.sidebar.progress(0)
    for percent_complete_20 in range(1, 20):
        time.sleep(0.01)
        progress_20.progress(percent_complete_20)

    st.sidebar.markdown(f"""
                <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p>
                <p style="line-height: 100%; font-size: 1.1vw;">First Quest</p>
                <p style="padding-left: 30px; line-height:100%; font-size: 1.3vw;"><strong>Map</strong></p>
            """, unsafe_allow_html=True)
    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("pictures/island_02.png")
    with col2:
        st.markdown(f""" <p style="line-height:130%; font-size:2vw; color:white">Look! There is a way through the 
        jungle!</p><p style="line-height:150%; font-size: 1.5vw; color: white">When finishing quests you not only get 
        new equipment but can also find your way back to your boat. Stay strong sailor!</p>""", unsafe_allow_html=True)
        st.image("pictures/shelly_with_backpack.png", width=300)

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("Open Backpack"):
            st.session_state.place = "backpack_1"
            st.rerun()


def render_map_3():
    progress_30 = st.sidebar.progress(0)
    for percent_complete_30 in range(1, 30):
        time.sleep(0.01)
        progress_30.progress(percent_complete_30)

    st.sidebar.markdown(f"""
                    <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p>
                    <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower First Try</p>
                    <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Method</p>
                    <p style="padding-left: 30px; line-height:100%; font-size: 1.3vw;"><strong>Map</strong></p>
                """, unsafe_allow_html=True)
    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("pictures/island_03.png")
    with col2:
        st.markdown(f""" <p style="line-height:130%; font-size:2vw; color:white">That's the way to go!</p><p 
        style="line-height:150%; font-size: 1.5vw; color: white">Even more jungle has cleared. Keep going, 
        you have quite the way in front of you!</p>""", unsafe_allow_html=True)
        st.image("pictures/shelly_with_backpack.png", width=300)

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("Open Backpack"):
            st.session_state.place = "backpack_2"
            st.rerun()


def render_map_4():
    progress_40 = st.sidebar.progress(0)
    for percent_complete_40 in range(1, 40):
        time.sleep(0.01)
        progress_40.progress(percent_complete_40)

    st.sidebar.markdown(f"""
                <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower First Try</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Method</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Applied</p>
                <p style="padding-left: 30px; line-height:100%; font-size: 1.3vw;"><strong>Map</strong></p>
            """, unsafe_allow_html=True)
    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("pictures/island_04.png")
    with col2:
        st.markdown(f""" <p style="line-height:130%; font-size:2vw; color:white">You did a great job applying the 
        Eisenhower method!</p><p style="line-height:150%; font-size: 1.5vw; color: white">Look how much of the way 
        has cleared!<br>Have you checked your backpack yet?</p>""", unsafe_allow_html=True)
        st.image("pictures/shelly_with_backpack.png", width=300)

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("Open Backpack"):
            st.session_state.place = "backpack_3"
            st.rerun()


def render_map_5():
    progress_50 = st.sidebar.progress(0)
    for percent_complete_50 in range(1, 50):
        time.sleep(0.01)
        progress_50.progress(percent_complete_50)

    st.sidebar.markdown(f"""
                <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower First Try</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Method</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Applied</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Cornell Method</p>
                <p style="padding-left: 30px; line-height:100%; font-size: 1.3vw;"><strong>Map</strong></p>
            """, unsafe_allow_html=True)
    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("pictures/island_05.png")
    with col2:
        st.markdown(f""" <p style="line-height:130%; font-size:2vw; color:white">Now you know everything about the 
        Cornell method!</p><p style="line-height:150%; font-size: 1.5vw; color: white"> Looks like you made it 
        halfway through the jungle!</p>""", unsafe_allow_html=True)
        st.image("pictures/shelly_with_backpack.png", width=300)

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("Open Backpack"):
            st.session_state.place = "backpack_4"
            st.rerun()


def render_map_6():
    progress_60 = st.sidebar.progress(0)
    for percent_complete_60 in range(1, 60):
        time.sleep(0.01)
        progress_60.progress(percent_complete_60)

    st.sidebar.markdown(f"""
                <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower First Try</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Method</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Applied</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Cornell Method</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Blurting Method</p>
                <p style="padding-left: 30px; line-height:100%; font-size: 1.3vw;"><strong>Map</strong></p>
            """, unsafe_allow_html=True)
    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("pictures/island_06.png")
    with col2:
        st.markdown(f""" <p style="line-height:130%; font-size:2vw; color:white">Now you know everything about the 
        Blurting method!</p><p style="line-height:150%; font-size: 1.5vw; color: white">Did you know, the best way to 
        use it, is to combine it with the Cornell method?<br>Also have you noticed your progress on the island?</p>""",
                    unsafe_allow_html=True)
        st.image("pictures/shelly_with_backpack.png", width=300)

    cola, colb = st.columns((8, 1))
    with colb:
        # button to start the next quest
        if st.button("Open Backpack"):
            st.session_state.place = "backpack_5"
            st.rerun()


def render_map_7():
    progress_70 = st.sidebar.progress(0)
    for percent_complete_70 in range(1, 70):
        time.sleep(0.01)
        progress_70.progress(percent_complete_70)

    st.sidebar.markdown(f"""
                <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower First Try</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Method</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Applied</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Cornell Method</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Blurting Method</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Quest First Try</p>
                <p style="padding-left: 30px; line-height:100%; font-size: 1.3vw;"><strong>Map</strong></p>
            """, unsafe_allow_html=True)
    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("pictures/island_07.png")
    with col2:
        st.markdown(f""" <p style="line-height:130%; font-size:2vw; color:white">Well done!</p><p 
        style="line-height:150%; font-size: 1.5vw; color: white">I knew you would do well in this quest. Would you 
        like to get to know a method that will make you a pro in time management?<br>But first let's check out your 
        new equipment!</p>""",
                    unsafe_allow_html=True)
        st.image("pictures/shelly_with_backpack.png", width=300)

    cola, colb = st.columns((8, 1))
    with colb:
        # button to start the next quest
        if st.button("Open Backpack"):
            st.session_state.place = "backpack_6"
            st.rerun()


def render_map_8():
    progress_80 = st.sidebar.progress(0)
    for percent_complete_80 in range(1, 80):
        time.sleep(0.01)
        progress_80.progress(percent_complete_80)

    st.sidebar.markdown(f"""
                <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower First Try</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Method</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Applied</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Cornell Method</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Blurting Method</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Pomodoro First Try</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Pomodoro Method</p>
                <p style="padding-left: 30px; line-height:100%; font-size: 1.3vw;"><strong>Map</strong></p>
            """, unsafe_allow_html=True)
    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("pictures/island_08.png")
    with col2:
        st.markdown(f""" <p style="line-height:130%; font-size:2vw; color:white">Bravissimo!</p><p 
        style="line-height:150%; font-size: 1.5vw; color: white">When hearing all these italian foods I have to show 
        off some of my Italian.<br> Wow, have a look on the island! I think I can already see some light coming 
        through the jungle.<br><br>Don't stop now, you almost made it!</p>""",
                    unsafe_allow_html=True)
        st.image("pictures/shelly_with_backpack.png", width=300)

    cola, colb = st.columns((8, 1))
    with colb:
        # button to start the next quest
        if st.button("Open Backpack"):
            st.session_state.place = "backpack_7"
            st.rerun()


def render_map_9():
    progress_90 = st.sidebar.progress(0)
    for percent_complete_90 in range(1, 90):
        time.sleep(0.01)
        progress_90.progress(percent_complete_90)

    st.sidebar.markdown(f"""
                <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower First Try</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Method</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Applied</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Cornell Method</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Blurting Method</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Pomodoro First Try</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Pomodoro Method</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Pomodoro Applied</p>
                <p style="padding-left: 30px; line-height:100%; font-size: 1.3vw;"><strong>Map</strong></p>
            """, unsafe_allow_html=True)
    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("pictures/island_09.png")
    with col2:
        st.markdown(f""" <p style="line-height:130%; font-size:2vw; color:white">You did it!</p><p 
        style="line-height:150%; font-size: 1.5vw; color: white">Amazing job applying the Pomodoro method.<br>Look, the jungle has cleared all the way and you and your 
        brother can return to your boat.<br>Wow, and I think your backpack is getting quite heavy. Let's check it 
        out!</p>""",
                    unsafe_allow_html=True)
        st.image("pictures/shelly_with_backpack.png", width=300)

    cola, colb = st.columns((8, 1))
    with colb:
        # button to start the next quest
        if st.button("Open Backpack"):
            st.session_state.place = "backpack_8"
            st.rerun()
