import streamlit as st


def render_pomodoro_method():
    st.title("Pomodoro Technique")

    tab_titles = ["Tomatoes", "Pomodoro"]
    tab1, tab2 = st.tabs(tab_titles)

    with tab1:
        col1, col2, col3, col4 = st.columns((1, 3, 4, 1))
        with col2:
            st.image("../pictures/tomato.png")
        with col3:
            st.markdown(f""" <p style="line-height:130%; font-size:2vw; color:white"> Pasta Bolognese, 
            Pasta Arrabiata, Pasta Pomodoro...Wait what? We are not talking about food?</p><p 
            style="line-height:130%; font-size: 1.5vw; color: white"> In fact the Pomodoro Technique has not much to 
            do with the pasta dish or tomatoes. Even though pomodoro means tomato in Italian.<br><br>It actually is a 
            helpful method to stay concentrated and think about time-management. Continue clicking through the tabs 
            above to learn more about foo..I mean the technique. Wow, all this talk about tomatoes made me 
            hungry...</p>""",
                        unsafe_allow_html=True)
    with tab2:
        col5, col6 = st.columns(2)
        with col5:
            st.image("../pictures/pomodoro.png")
        with col6:
            st.markdown("test")

        cola, colb = st.columns((10, 1))
        with colb:
            # button to start the next quest
            if st.button("View map"):
                st.session_state.place = "map_8"
                st.rerun()
