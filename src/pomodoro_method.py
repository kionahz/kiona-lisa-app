import streamlit as st


def render_pomodoro_method():
    st.sidebar.progress(70)

    st.sidebar.markdown(f"""
    <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower First Try</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Method</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Applied</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Cornell Method</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Blurting Method</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Pomodoro First Try</p>
        <p style="line-height: 100%; font-size: 1.3vw;"><strong>Pomodoro Method</strong></p>
    """, unsafe_allow_html=True)

    st.title("Pomodoro Technique")

    tab_titles = ["Tomatoes", "Pomodoro Method", "Did you know?"]
    tab1, tab2, tab3 = st.tabs(tab_titles)

    with tab1:
        col1, col2, col3, col4 = st.columns((1, 3, 4, 1))
        with col2:
            st.image("pictures/tomato.png")
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
        col1, col2, col3, col4 = st.columns((1, 3, 4, 1))
        with col2:
            st.image("pictures/pomodoro.png")
        with col3:
            st.markdown("Pomodoro Method")

    with tab3:
        col1, col2, col3, col4 = st.columns((1, 3, 4, 1))
        with col2:
            st.image("pictures/pomodoro.png")
        with col3:
            st.markdown("Did you know?")

        cola, colb = st.columns((10, 1))
        with colb:
            if st.button("Continue"):
                st.session_state.place = "map_8"
                st.rerun()
