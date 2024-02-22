import streamlit as st


def Eisenhower_quest2():
    tab_titles = ["Do", "Schedule", "Delegate", "Delete"]
    tab1, tab2, tab3, tab4 = st.tabs(tab_titles)

    with tab1:
        st.header("Urgent/Important")

    with tab2:
        st.header("Not Urgent/ Important")

    with tab3:
        st.header("Urgent/Not Important")

    with tab4:
        st.header("Not Urgent/Not Important")

