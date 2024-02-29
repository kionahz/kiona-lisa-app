import streamlit as st

# TODO backpack 3 changes


def render_backpack_empty():
    st.sidebar.progress(10)

    st.sidebar.markdown(f"""
        <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p>
        <p style="padding-left: 30px; line-height:100%; font-size: 1.2vw;"><strong>Backpack</strong></p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/backpack_items_empty.png")
    with col2:
        st.markdown(
            f""" <p style="line-height:130%; font-size: 1.5vw; color: white"><br><br><br>This is your backpack. 
            Unfortunately, it is still empty. Once you finish a quest, you will find your collected equipment here. 
            Let´s see if you can gather enough equipment to repair your boat.<br><br>Let's get started and begin with 
            the first quest!</p>""",
            unsafe_allow_html=True
        )
        st.image("../pictures/shelly_without.png")

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("Start First Quest"):
            st.session_state.place = "eisenhower_q1"
            st.rerun()


def render_backpack_1():
    st.sidebar.progress(20)

    st.sidebar.markdown(f"""
            <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p>
            <p style="line-height: 100%; font-size: 1.1vw;">First Quest</p>
            <p style="padding-left: 30px; line-height:100%; font-size: 1.3vw;"><strong>Backpack</strong></p>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/backpack_items_1.png")
    with col2:
        st.markdown(
            f""" <p style="line-height:130%; font-size: 1.5vw; color: white"><br><br><br>Great!<br><br>You collected 
            the first item in your backpack. You can use the wood later to patch up the holes in your boat.<br><br>Good 
            job!</p>""",
            unsafe_allow_html=True
        )
        st.image("../pictures/shelly_without.png")

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("Continue"):
            st.session_state.place = "eisenhower_method"
            st.rerun()


def render_backpack_2():
    st.sidebar.progress(30)

    st.sidebar.markdown(f"""
                <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower First Try</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Method</p>
                <p style="padding-left: 30px; line-height:100%; font-size: 1.3vw;"><strong>Backpack</strong></p>
            """, unsafe_allow_html=True)

    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/backpack_items_2.png")
    with col2:
        st.markdown(
            f""" <p style="line-height:130%; font-size: 1.5vw; color: white"><br><br><br>Fantastic!<br><br>You 
            collected the second item in your backpack. You can use the nails for the wood you received with your last 
            quest.<br><br>Keep up the good work!</p>""",
            unsafe_allow_html=True
        )
        st.image("../pictures/shelly_without.png")

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("Continue"):
            st.session_state.place = "eisenhower_q2"
            st.rerun()


def render_backpack_3():
    st.sidebar.progress(40)

    st.sidebar.markdown(f"""
                <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower First Try</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Method</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Applied</p>
                <p style="padding-left: 30px; line-height:100%; font-size: 1.3vw;"><strong>Backpack</strong></p>
            """, unsafe_allow_html=True)

    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/backpack_items_3.png")
    with col2:
        st.markdown(
            f""" <p style="line-height:130%; font-size: 1.5vw; color: white">Amazing!<br><br>You 
            collected the third item in your backpack. What good are nails, without a hammer am I right?<br><br>Let's 
            keep going to see what else you can get!<br><br>Oh no wait I hear something. I think someone is approaching 
            us. How weird I thought this island was completely deserted. Lets see who else is here. Maybe they can 
            help you!</p>""",
            unsafe_allow_html=True
        )
        st.image("../pictures/shelly_without.png")

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("Continue"):
            st.session_state.place = "pirate"
            st.rerun()


def render_backpack_4():
    st.sidebar.progress(50)

    st.sidebar.markdown(f"""
                <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower First Try</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Method</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Applied</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Cornell Method</p>
                <p style="padding-left: 30px; line-height:100%; font-size: 1.3vw;"><strong>Backpack</strong></p>
            """, unsafe_allow_html=True)

    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/backpack_items_4.png")
    with col2:
        st.markdown(
            f""" <p style="line-height:130%; font-size: 1.5vw; color: white"><br><br><br>Awesome!<br><br>You 
            collected the fourth item in your backpack. Its a saw that you can use to cut the wood to 
            size. I guess you have everything to start with the woodwork?<br><br>Way to go!</p>""",
            unsafe_allow_html=True
        )
        st.image("../pictures/shelly_without.png")

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("Continue"):
            st.session_state.place = "blurting_method"
            st.rerun()


def render_backpack_5():
    st.sidebar.progress(60)

    st.sidebar.markdown(f"""
                <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower First Try</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Method</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Applied</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Cornell Method</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Blurting Method</p>
                <p style="padding-left: 30px; line-height:100%; font-size: 1.3vw;"><strong>Backpack</strong></p>
            """, unsafe_allow_html=True)

    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/backpack_items_5.png")
    with col2:
        st.markdown(
            f""" <p style="line-height:130%; font-size: 1.5vw; color: white"><br><br><br>Extraordinary!<br><br>You 
            collected the fifth item in your backpack. It's white, it's soft, it's... fabric! You can use it to fix 
            your sails.<br><br>Wow! You are really becoming a pro.</p>""",
            unsafe_allow_html=True
        )
        st.image("../pictures/shelly_without.png")

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("Continue"):
            st.session_state.place = "pomodoro_q1"
            st.rerun()


def render_backpack_6():
    st.sidebar.progress(70)

    st.sidebar.markdown(f"""
                <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower First Try</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Method</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Applied</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Cornell Method</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Blurting Method</p>
                <p style="line-height: 100%; font-size: 1.1vw;">Quest First Try</p>
                <p style="padding-left: 30px; line-height:100%; font-size: 1.3vw;"><strong>Backpack</strong></p>
            """, unsafe_allow_html=True)

    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/backpack_items_6.png")
    with col2:
        st.markdown(
            f""" <p style="line-height:130%; font-size: 1.5vw; color: white"><br><br><br>Excellent!<br><br>You 
            collected the sixth item in your backpack. This needle and thread will be helpful to sew the fabric for 
            your new sails. Just be careful to not prick your fingers! <br><br>You are nearly there!</p>""",
            unsafe_allow_html=True
        )
        st.image("../pictures/shelly_without.png")

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("Continue"):
            st.session_state.place = "pomodoro_method"
            st.rerun()


def render_backpack_7():
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
                <p style="padding-left: 30px; line-height:100%; font-size: 1.3vw;"><strong>Backpack</strong></p>
            """, unsafe_allow_html=True)

    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/backpack_items_7.png")
    with col2:
        st.markdown(
            f""" <p style="line-height:130%; font-size: 1.5vw; color: white"><br><br><br>Wonderful!<br><br>You collected 
                    the seventh item in your backpack. Its a rope that you can use to set and adjust the 
                    sails. <br><br>Only one more quest to go. You can do it!</p>""",
            unsafe_allow_html=True
        )
        st.image("../pictures/shelly_without.png")

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("Continue"):
            st.session_state.place = "pomodoro_q2"
            st.rerun()


def render_backpack_8():
    st.sidebar.progress(90)

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
            <p style="padding-left: 30px; line-height:100%; font-size: 1.3vw;"><strong>Backpack</strong></p>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns((5, 3), gap='large')
    with col1:
        st.image("../pictures/backpack_items_8.png")
    with col2:
        st.markdown(
            f""" <p style="line-height:130%; font-size: 1.5vw; color: white"><br><br><br>Terrific!<br><br>You got a 
            bucket of paint. You can use it to put the finishing touches to your boat and make it look 
            pretty.<br><br>You filled you backpack all the way.<br>Good work! Your boat is now finally completely 
            repaired and you can sail away!</p>""",
            unsafe_allow_html=True
        )
        st.image("../pictures/shelly_without.png")

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("Sail Away"):
            st.session_state.place = "sail_away"
            st.rerun()