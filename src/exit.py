import streamlit as st
import time
# TODO: Formatting & Comments done


# Function to render the exit message
def render_exit():
    # Creating a progress bar in the sidebar
    progress_60 = st.sidebar.progress(0)
    # Loop to update the progress bar
    for percent_complete_60 in range(1, 60):
        time.sleep(0.01)
        progress_60.progress(percent_complete_60)

    # Creating three columns for layout
    col1, col2, col3 = st.columns((1, 5, 1))

    # Display the logo banner and the exit message inside the middle column (col2)
    with col2:
        st.markdown(
            f""" 
            <p style="font-family: serif; font-size:2vw; text-align:center;">
                Thanks for playing!<br>See you next time ☺︎<br><br>You can close the window now.<br>
            </p>
            """, unsafe_allow_html=True)
        st.image("pictures/logo_banner.png")
