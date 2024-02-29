import streamlit as st


def render_eisenhower_q2():
    tasks = ["Search for a container (for food or water)", "Build a fire", "Build Shelter", "Collect Shells",
             "Collect Wood",
             "Watch the Sunset", "Search for drinking water", "Search for Food", "Build a Weapon",
             "Explore the surroundings"]

    col_1, col_2 = st.columns((2, 1))
    with col_1:
        st.title("Now it's your turn!")
        st.markdown(
            f""" <p style="line-height:130%; font-size: 1.5vw; color: white">Now you know everything about the 
                Eisenhower matrix. Let's try to arrange your tasks on what you can do to escape the island once again. Do 
                you think you can do it like Eisenhower? Select the task you would like to sort into your very own 
                Eisenhower matrix with the multi selects.</p>""",
            unsafe_allow_html=True
        )
    with col_2:
        st.image("../pictures/em_empty.png")

    st.divider()

    col3, col4, col5 = st.columns((2, 3, 3))
    with col3:
        with st.expander(label="Here you can see your tasks again", expanded=True):
            st.markdown(f""" <p style="line-height:150%; font-size: 1.1vw; color: white">· Build a Fire<br>· Collect 
            Shells<br>· Build a shelter<br>· Search for Food<br>· Build a Weapon<br>· Collect Wood<br>· Watch the 
            Sunset<br>· Search for drinking water<br>· Explore the surroundings<br>· Search for a container (for food 
            or water)</p>""",
                        unsafe_allow_html=True)

    with col4:
        st.subheader("Urgent/Important")
        selection_1 = st.multiselect("Urgent/Important", tasks, placeholder="Choose one or multiple options",
                                     label_visibility="collapsed")
        st.write(selection_1)

        st.subheader("Urgent/Not Important")
        selection_3 = st.multiselect("Urgent/Not Important", tasks, placeholder="Choose one or multiple options",
                                     label_visibility="collapsed")
        st.write(selection_3)

    with col5:
        st.subheader("Not Urgent/Important")
        selection_2 = st.multiselect("Not Urgent/Important", tasks, placeholder="Choose one or multiple options",
                                     label_visibility="collapsed")
        st.write(selection_2)

        st.subheader("Not Urgent/Not Important")
        selection_4 = st.multiselect("Not Urgent/Not Important", tasks, lplaceholder="Choose one or multiple options",
                                     label_visibility="collapsed")
        st.write(selection_4)

    cola, colb = st.columns((8, 1))
    with colb:
        # button to start the next quest
        if st.button("View map"):
            st.session_state.place = "map_4"
            st.rerun()



