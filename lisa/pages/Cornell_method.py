import streamlit as st


def cornell_method():
    st.title("Cornell Method")

    tab_titles = ["Cornell", "Method"]
    tab1, tab2 = st.tabs(tab_titles)

    with tab1:
        st.markdown("Cornell Method")

    with tab2:
        col1, col2, col3, col4 = st.columns((1, 3, 4, 1))
        with col2:
            st.image("../pictures/cornell.png")

        with col3:
            st.markdown("test")
