import streamlit as st
tasks = ["Search for a container (for food or water)", "Build a fire", "Build Shelter", "Collect Shells",
         "Collect Wood", "Watch the Sunset", "Search for drinking water", "Search for Food", "Build a Weapon",
         "Explore the surroundings"]

sel_urgent_important, sel_noturgent_important = st.columns(2)
sel_urgent_notimportant, sel_noturgent_notimportant = st.columns(2)

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

with sel_noturgent_important:
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
    selections_noturgent_notimportant = st.multiselect("Not Urgent/Not Important", tasks_copy, label_visibility="hidden")
    st.write(selections_noturgent_notimportant)
