import streamlit as st
# TODO: Input!!!

# Setting up some constants for styling
line_height_sidebar = "100%"
line_height_pomodoro = "130%"
font_size_sidebar = "1.1vw"
font_size_sidebar_current = "1.3vw"
font_size_pomodoro = "1.5vw"
font_size_pomodoro_title = "2vw"

# Variables for column sizing
x = 1
y = 3
z = 4

# List of sections until current page
sections = [
    "Introduction",
    "Eisenhower First Try",
    "Eisenhower Method",
    "Eisenhower Applied",
    "Pirate Encounter",
    "Cornell Method",
    "Blurting Method",
    "Pomodoro First Try",
    "<strong>Pomodoro Method</strong>"
]

# List of tab titles to display
tab_titles = ["Tomatoes",
              "Pomodoro Method",
              "Did you know?"]


# Function to render the Pomodoro Method page
def render_pomodoro_method():
    # Creating a progress bar in the sidebar
    st.sidebar.progress(70)

    # Displaying sections in the sidebar using a loop
    for section in sections:
        if "<strong>" in section:
            st.sidebar.markdown(
                f"""
                <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar_current};">
                    {section}
                </p>
                """, unsafe_allow_html=True)
        else:
            st.sidebar.markdown(
                f"""
                <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar};">
                    {section}
                </p>
                """, unsafe_allow_html=True)

    # Page title
    st.title("Pomodoro Technique")

    # Creating tabs for the different sections
    tab1, tab2, tab3 = st.tabs(tab_titles)

    # Tab 1: Introduction to Pomodoro Method with image and markdown
    with tab1:
        col1, col2, col3, col4 = st.columns((x, y, z, x))
        with col2:
            st.image("pictures/tomato.png")
        with col3:
            st.markdown(
                f""" 
                <p style="line-height:{line_height_pomodoro}; font-size:{font_size_pomodoro_title};">
                    Pasta Bolognese, Pasta Arrabiata, Pasta Pomodoro...Wait what? We are not talking about food?
                </p>
                <p style="line-height:{line_height_pomodoro}; font-size: {font_size_pomodoro};"> 
                    In fact the Pomodoro Technique has not much to do with the pasta dish or tomatoes. Even though 
                    pomodoro means tomato in Italian.<br><br>It actually is a helpful method to stay concentrated and 
                    think about time-management. Continue clicking through the tabs above to learn more about foo..I 
                    mean the technique. Wow, all this talk about tomatoes made me hungry...
                </p>
                """, unsafe_allow_html=True)


    with tab2:
        col1, col2, col3, col4 = st.columns((x, y, z, x))
        with col2:
            st.image("pictures/pomodoro.png")
        with col3:
            st.markdown("Pomodoro Method")

    with tab3:
        col1, col2, col3, col4 = st.columns((x, y, z, x))
        with col2:
            st.image("pictures/pomodoro.png")
        with col3:
            st.markdown("Did you know?")

        # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
        col_a, col_b = st.columns((8, 1))
        with col_b:
            # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
            # Rerunning the app when the button is clicked to continues the game
            if st.button("Continue"):
                st.session_state.place = "map_8"
                st.rerun()
