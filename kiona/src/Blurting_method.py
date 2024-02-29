import streamlit as st


def render_blurting_method():
    st.sidebar.progress(50)

    st.sidebar.markdown(f"""
    <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower First Try</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Method</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Applied</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Cornell Method</p>
        <p style="line-height: 100%; font-size: 1.3vw;"><strong>Blurting Method</strong></p>
    """, unsafe_allow_html=True)

    tab_titles = ["Blurting Method", "Blurting", "What you forgot", "Practice Questions", "Did you know?"]
    tab1, tab2, tab3, tab4, tab5 = st.tabs(tab_titles)

    with tab1:
        col1, col2, col3, col4 = st.columns((1, 3, 4, 1))
        with col2:
            st.image("../pictures/blurting.png")

        with col3:
            st.markdown(
                f""" <p style="line-height:130%; font-size:2vw; color:white">This is the Blurting Method</p> <p 
                style="line-height:130%; font-size: 1.5vw; color: white">I know you´ve listened closely to the Pirate 
                and wrote down all the important information he gave you. Now to remember all that information by 
                heart, you have to study it. For this the Blurting Method can be very helpful.<br><br>Have you ever 
                heard of it? If not here's how it works:</p>""",
                unsafe_allow_html=True
            )

    with tab2:
        col1, col2, col3, col4 = st.columns((1, 3, 4, 1))
        with col2:
            st.image("../pictures/blurting.png")

        with col3:
            st.markdown(
                f""" <p style="line-height:130%; font-size:2vw; color:white">Blurting</p> <p style="line-height:130%; 
                font-size: 1.5vw; color: white">If you want you can take a look at your notes you took before and 
                organize them, if you have a lot of notes. Skim quickly through the notes. And now its time to blurt! 
                Cover up your notes and start jotting down everything you can recall. Don´t worry about being perfect 
                and getting everything right-just get the ideas flowing, like the waves around you.</p>""",
                unsafe_allow_html=True
            )

    with tab3:
        col1, col2, col3, col4 = st.columns((1, 3, 4, 1))
        with col2:
            st.image("../pictures/blurting.png")

        with col3:
            st.markdown(
                f""" <p style="line-height:130%; font-size:2vw; color:white">What did you forget?</p> <p 
                style="line-height:130%; font-size: 1.5vw; color: white">You can now take a moment to review. Check 
                your notes with your blurted ideas to see if you missed something.<br><br>Add this extra info in a 
                different to color.</p>""",
                unsafe_allow_html=True
            )

    with tab4:
        col1, col2, col3, col4 = st.columns((1, 3, 4, 1))
        with col2:
            st.image("../pictures/blurting.png")

        with col3:
            st.markdown(
                f""" <p style="line-height:130%; font-size:2vw; color:white">Practice Questions</p> <p 
                style="line-height:130%; font-size: 1.5vw; color: white">To help you remember everything even better, 
                you can additionally add Questions to test your knowledge and exam technique.</p>""",
                unsafe_allow_html=True
            )

    with tab5:
        col1, col2, col3, col4 = st.columns((1, 3, 4, 1))
        with col2:
            st.image("../pictures/blurting.png")

        with col3:
            st.markdown(
                f""" <p style="line-height:130%; font-size:2vw; color:white">Did you know?</p> <p 
                style="line-height:130%; font-size: 1.5vw; color: white">The blurting method is often used in 
                improvisational comedy to generate quick and spontaneous humor.<br><br>In improvisation, 
                blurting refers to the act of saying the first thing that comes to mind without filtering it. This 
                can lead to unexpected and hilarious outcomes as performers react in the moment.<br><br>What do you 
                think? Can you just blurt down notes and information from your memory like an improvisation 
                performer?</p>""",
                unsafe_allow_html=True
            )

        cola, colb = st.columns((8, 1))
        with colb:
            # button to start the next quest
            if st.button("Continue"):
                st.session_state.place = "map_6"
                st.rerun()