import streamlit as st


def Eisenhower_quest3():
    tasks = ["Search for a container (for food or water)", "Build a fire", "Build Shelter", "Collect Shells",
             "Collect Wood",
             "Watch the Sunset", "Search for drinking water", "Search for Food", "Build a Weapon",
             "Explore the surroundings"]

    col_title, col_img = st.columns((2, 1))

    with col_title:
        st.title("Now it's your turn!")
        st.markdown(
            f""" <p style="line-height:130%; font-size: 1.5vw; color: white">Now you know everything about the 
            Eisenhower matrix. Let's try to arrange your tasks on what you can do to escape the island once again. Do 
            you think you can do it like Eisenhower? Select the task you would like to sort into your very own 
            Eisenhower matrix with the multiselects.</p>""",
            unsafe_allow_html=True
        )

    with col_img:
        st.image("../pictures/em_empty.png")

    sel_urgent_important, sel_noturgent_notimportant = st.columns(2)

    with sel_urgent_important:
        st.subheader("Urgent/Important")

        # Create the multi-select box
        selections_urgent_important = st.multiselect("Urgent/Important", tasks.copy(), label_visibility="hidden")
        st.write(selections_urgent_important)
        st.subheader("Urgent/Not Important")
        # Remove the tasks selected in the first multi-select box
        tasks_copy = tasks.copy()
        for task in selections_urgent_important:
            tasks_copy.remove(task)
        selections_urgent_notimportant = st.multiselect("Urgent/Not Important", tasks_copy, label_visibility="hidden")
        st.write(selections_urgent_notimportant)

    with sel_noturgent_notimportant:
        st.subheader("Not Urgent/Important")
        # Remove the tasks selected in the first two multi-select boxes
        tasks_copy = tasks.copy()
        for task in selections_urgent_important:
            tasks_copy.remove(task)
        for task in selections_urgent_notimportant:
            tasks_copy.remove(task)
        selections_noturgent_important = st.multiselect("Not Urgent/Important", tasks_copy, label_visibility="hidden")
        st.write(selections_noturgent_important)
        st.subheader("Not Urgent/Not Important")
        # Remove the tasks selected in all multi-select boxes
        tasks_copy = tasks.copy()
        for task in selections_urgent_important:
            tasks_copy.remove(task)
        for task in selections_urgent_notimportant:
            tasks_copy.remove(task)
        for task in selections_noturgent_important:
            tasks_copy.remove(task)
        selections_noturgent_notimportant = st.multiselect("Not Urgent/Not Important", tasks_copy,
                                                           label_visibility="hidden")
        st.write(selections_noturgent_notimportant)
