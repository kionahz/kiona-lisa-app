import streamlit as st



def homepage():
    st.title("Homepage")
    if st.sidebar.button("Play"):
        st.session_state.sidebar_expanded = True

def quest_page(quest_number):
    st.title(f"Quest {quest_number}")
    if st.button("Continue"):
        st.session_state.sidebar_expanded = True

def main():
    st.session_state.sidebar_expanded = False

    if not st.session_state.sidebar_expanded:
        homepage()
    else:
        with st.sidebar:
            st.title("Navigation")
            page = st.radio("Go to", ["Home", "Quest 1", "Quest 2", "Quest 3", "Quest 4", "Quest 5", "Quest 6"])

        if page == "Home":
            st.session_state.sidebar_expanded = False
        elif page.startswith("Quest"):
            quest_number = int(page.split()[-1])
            quest_page(quest_number)

if __name__ == "__main__":
    main()
