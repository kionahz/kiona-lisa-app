import streamlit as st
import time
# TODO copy all as is

def render_cornell_method():
    st.sidebar.progress(40)

    st.sidebar.markdown(f"""
    <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower First Try</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Method</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Applied</p>
        <p style="line-height: 100%; font-size: 1.3vw;"><strong>Cornell Method</strong></p>
    """, unsafe_allow_html=True)

    tab_titles = ["Cornell Method", "Main Notes", "Side", "Summary", "Did you know?"]
    tab1, tab2, tab3, tab4, tab5 = st.tabs(tab_titles)

    with tab1:
        col1, col2, col3, col4 = st.columns((1, 3, 4, 1))
        with col2:
            st.image("../pictures/cornell.png")

        with col3:
            st.markdown("Cornell Method")

    with tab2:
        col1, col2, col3, col4 = st.columns((1, 3, 4, 1))
        with col2:
            st.image("../pictures/cornell.png")

        with col3:
            st.markdown("Notes")

    with tab3:
        col1, col2, col3, col4 = st.columns((1, 3, 4, 1))
        with col2:
            st.image("../pictures/cornell.png")

        with col3:
            st.markdown("Keywords & Questions")

    with tab4:
        col1, col2, col3, col4 = st.columns((1, 3, 4, 1))
        with col2:
            st.image("../pictures/cornell.png")

        with col3:
            st.markdown("Summary")

    with tab5:
        col1, col2, col3, col4 = st.columns((1, 3, 4, 1))
        with col2:
            st.image("../pictures/cornell.png")

        with col3:
            st.markdown("Did you know?")

        cola, colb = st.columns((8, 1))
        with colb:
            # button to start the next quest
            if st.button("Continue"):
                st.session_state.place = "map_5"
                st.rerun()
