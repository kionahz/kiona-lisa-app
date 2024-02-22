import streamlit as st

def Eisenhower_quest3():
    col1, col2 = st.columns(2)

    with col1:
        st.image("../pictures/em_empty.png")

    with col2:
        st.markdown(
            "Now you know how the matrix works. Now arrange the same tasks as before in the matrix. Does it make "
            "a difference to you in the decision-making process?")

    col3, col4 = st.columns(2)
    col5, col6 = st.columns(2)

    with col3:
        st.multiselect(
            "Urgent/Important",
            ["Search for a container (for food or water)", "Build a fire", "Build Shelter", "Collect Shells",
             "Collect Wood",
             "Watch the Sunset", "Search for drinking water", "Search for Food", "Build a Weapon",
             "Explore the surroundings"]
        )

    with col4:
        st.multiselect(
            "Not Urgent/Important",
            ["Search for a container (for food or water)", "Build a fire", "Build Shelter", "Collect Shells",
             "Collect Wood",
             "Watch the Sunset", "Search for drinking water", "Search for Food", "Build a Weapon",
             "Explore the surroundings"]
        )

    with col5:
        st.multiselect(
            "Urgent/Not Important",
            ["Search for a container (for food or water)", "Build a fire", "Build Shelter", "Collect Shells",
             "Collect Wood", "Watch the Sunset", "Search for drinking water", "Search for Food", "Build a Weapon",
             "Explore the surroundings"]
        )

    with col6:
        st.multiselect(
            "Not Urgent/Not Important",
            ["Search for a container (for food or water)", "Build a fire", "Build Shelter", "Collect Shells",
             "Collect Wood", "Watch the Sunset", "Search for drinking water", "Search for Food", "Build a Weapon",
             "Explore the surroundings"]
        )


