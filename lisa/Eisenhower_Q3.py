import streamlit as st

def Eisenhower_quest3():

    tasks = ["Search for a container (for food or water)", "Build a fire", "Build Shelter", "Collect Shells",
             "Collect Wood",
             "Watch the Sunset", "Search for drinking water", "Search for Food", "Build a Weapon",
             "Explore the surroundings"]

    st.title("Now it's your turn!")
    col1, col2 = st.columns(2)

    with col1:
        st.image("../pictures/em_empty.png")

    with col2:
        st.markdown(
            "Now you know everything about the Eisenhower matrix. Let's try to arrange what you can do to escape the "
            "island once again. Do you think you can do it like Eisenhower? Select the task you would like to sort "
            "into your very own Eisenhower matrix with with the multiselects.")

    sel_urgent_important, sel_noturgent_important = st.columns(2)
    sel_urgent_notimportant, sel_noturgent_notimportant = st.columns(2)

    with sel_urgent_important:
        st.subheader("Urgent/Important")

        # Create the multi-select box
        selections_urgent_important = st.multiselect("Urgent/Important",tasks, label_visibility="hidden")
        st.write(selections_urgent_important)


    with sel_noturgent_important:
        selections_noturgent_important = st.multiselect("Not Urgent/Important", tasks, label_visibility="hidden")
        st.write(selections_noturgent_important)


    with sel_urgent_notimportant:
        selections_urgent_notimportant = st.multiselect(
            "Urgent/Not Important", tasks
        )


    with sel_noturgent_notimportant:
        selections_noturgent_notimportant = st.multiselect(
            "Not Urgent/Not Important", tasks
        )
    with tab_noturgent_notimportant:
        st.markdown("Not Urgent/Not Important")
        st.markdown(selections_noturgent_notimportant)


