import streamlit as st

# TODO copy all as is

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

    tab_titles = ["Blurting Method", "Blurting", "Practice Questions", "What you forgot", "Did you know?"]
    tab1, tab2, tab3, tab4, tab5 = st.tabs(tab_titles)

    with tab1:
        col1, col2, col3, col4 = st.columns((1, 3, 4, 1))
        with col2:
            st.image("../pictures/blurting.png")

        with col3:
            st.markdown("Blurting Method")

    with tab2:
        col1, col2, col3, col4 = st.columns((1, 3, 4, 1))
        with col2:
            st.image("../pictures/blurting.png")

        with col3:
            st.markdown("Blurting")

    with tab3:
        col1, col2, col3, col4 = st.columns((1, 3, 4, 1))
        with col2:
            st.image("../pictures/blurting.png")

        with col3:
            st.markdown("Practice Questions")

    with tab4:
        col1, col2, col3, col4 = st.columns((1, 3, 4, 1))
        with col2:
            st.image("../pictures/blurting.png")

        with col3:
            st.markdown("What you forgot")

    with tab5:
        col1, col2, col3, col4 = st.columns((1, 3, 4, 1))
        with col2:
            st.image("../pictures/blurting.png")

        with col3:
            st.markdown("Did you know?")

        cola, colb = st.columns((8, 1))
        with colb:
            # button to start the next quest
            if st.button("Continue"):  # TODO
                st.session_state.place = "map_6"
                st.rerun()