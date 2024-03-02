import streamlit as st
# TODO: Formatting done -> Comments

line_height_sidebar = "100%"
line_height_blurting = "130%"
font_size_sidebar = "1.1vw"
font_size_sidebar_current = "1.3vw"
font_size_blurting = "1.5vw"
font_size_blurting_title = "2vw"
x = 1
y = 3
z = 4

sections = ["Introduction",
            "Eisenhower First Try",
            "Eisenhower Method",
            "Eisenhower Applied",
            "Pirate Encounter",
            "Cornell Method",
            "<strong>Blurting Method</strong>"]

tab_titles = ["Blurting Method",
              "Blurting",
              "What you forgot",
              "Practice Questions",
              "Did you know?"]


def render_blurting_method():
    st.sidebar.progress(50)

    # Use a loop to format and display the strings
    for section in sections:
        if "<strong>" in section:
            st.sidebar.markdown(f"""
                        <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar_current};">{section}</p>
                        """, unsafe_allow_html=True)
        else:
            st.sidebar.markdown(f"""
                        <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar};">{section}</p>
                        """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5 = st.tabs(tab_titles)

    with tab1:
        col1, col2, col3, col4 = st.columns((x, y, z, x))
        with col2:
            st.image("pictures/blurting.png")

        with col3:
            st.markdown(
                f""" 
                <p style="line-height:{line_height_blurting}; font-size:{font_size_blurting_title};">
                    This is the Blurting Method
                </p> 
                <p style="line-height:{line_height_blurting}; font-size: {font_size_blurting};">
                    I know you´ve listened closely to the Pirate and wrote down all the important information he gave 
                    you. Now to remember all that information by heart, you have to study it. For this the Blurting 
                    Method can be very helpful.<br><br>Have you ever heard of it? If not here's how it works:
                </p>
                """, unsafe_allow_html=True
            )

    with tab2:
        col1, col2, col3, col4 = st.columns((x, y, z, x))
        with col2:
            st.image("pictures/blurting.png")

        with col3:
            st.markdown(
                f""" 
                <p style="line-height:{line_height_blurting}; font-size:{font_size_blurting_title};">
                    Blurting
                </p> 
                <p style="line-height:{line_height_blurting}; font-size: {font_size_blurting};">
                    If you want you can take a look at your notes you took before and organize them, if you have a lot 
                    of notes. Skim quickly through the notes. And now its time to blurt! Cover up your notes and start 
                    jotting down everything you can recall. Don´t worry about being perfect and getting everything 
                    right - just get the ideas flowing, like the waves around you.
                </p>
                """, unsafe_allow_html=True
            )

    with tab3:
        col1, col2, col3, col4 = st.columns((x, y, z, x))
        with col2:
            st.image("pictures/blurting.png")

        with col3:
            st.markdown(
                f""" 
                <p style="line-height:{line_height_blurting}; font-size:{font_size_blurting_title};">
                    What did you forget?
                </p> 
                <p style="line-height:{line_height_blurting}; font-size: {font_size_blurting};">
                    You can now take a moment to review. Check your notes with your blurted ideas to see if you missed 
                    something.<br><br>Add this extra info in a different to color.
                </p>
                """, unsafe_allow_html=True
            )

    with tab4:
        col1, col2, col3, col4 = st.columns((x, y, z, x))
        with col2:
            st.image("pictures/blurting.png")

        with col3:
            st.markdown(
                f""" 
                <p style="line-height:{line_height_blurting}; font-size:{font_size_blurting_title};">
                    Practice Questions
                </p> 
                <p style="line-height:{line_height_blurting}; font-size: {font_size_blurting};">
                    To help you remember everything even better, you can additionally add Questions to test your 
                    knowledge and exam technique.
                </p>
                """, unsafe_allow_html=True
            )

    with tab5:
        col1, col2, col3, col4 = st.columns((x, y, z, x))
        with col2:
            st.image("pictures/blurting.png")

        with col3:
            st.markdown(
                f""" 
                <p style="line-height:{line_height_blurting}; font-size:{font_size_blurting_title};">
                    Did you know?
                </p> 
                <p style="line-height:{line_height_blurting}; font-size: {font_size_blurting};">
                The blurting method is often used in improvisational comedy to generate quick and spontaneous humor.
                <br><br>In improvisation, blurting refers to the act of saying the first thing that comes to mind 
                without filtering it. This can lead to unexpected and hilarious outcomes as performers react in the 
                moment.<br><br>What do you think? Can you just blurt down notes and information from your memory like an 
                improvisation performer?
                </p>
                """, unsafe_allow_html=True
            )

        # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
        col_a, col_b = st.columns((8, 1))
        with col_b:
            # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
            # Rerunning the app when the button is clicked to continues the game
            if st.button("Continue"):
                st.session_state.place = "map_6"
                st.rerun()