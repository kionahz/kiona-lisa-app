import streamlit as st
# TODO: Formatting done -> Comments

line_height_sidebar = "100%"
font_size_sidebar = "1.1vw"
font_size_sidebar_current = "1.3vw"
line_height = "130%"
font_size_text = "1.5vw"
font_size_title = "2vw"

sections = ["Introduction",
            "Eisenhower First Try",
            "Eisenhower Method",
            "<strong>Eisenhower Applied</strong>"
            ]

tasks = ["Search for a container (for food or water)",
         "Build a fire",
         "Build Shelter",
         "Collect Shells",
         "Collect Wood",
         "Watch the Sunset",
         "Search for drinking water",
         "Search for Food",
         "Build a Weapon",
         "Explore the surroundings"]


def render_eisenhower_q2():
    st.sidebar.progress(30)

    # Use a loop to format and display the strings
    for section in sections:
        if "<strong>" in section:
            st.sidebar.markdown(f"""
                        <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar_current};">{section}
                        </p>
                        """, unsafe_allow_html=True)
        else:
            st.sidebar.markdown(f"""
                        <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar};">{section}
                        </p>
                        """, unsafe_allow_html=True)

    col_title, col_img = st.columns((3, 1))

    with col_title:
        st.title("It's your turn!")
        st.markdown(
            f""" 
            <p style="line-height:{line_height}; font-size: {font_size_text};">
                Now you know everything about the 
                Eisenhower matrix. Let's try to arrange your tasks on what you can do to survive on the island once 
                again. Do you think you can do it like Eisenhower?<br>Select the task you would like to sort into your 
                very own Eisenhower matrix by clicking on one of the boxes and selecting one or more tasks.
            </p>
            """, unsafe_allow_html=True
        )

    with col_img:
        st.image("pictures/em_empty.png")

    st.divider()

    col3, col4, col5 = st.columns((3, 4, 4))
    with col3:
        with st.expander(label="Here you can see your tasks again", expanded=True):
            st.markdown(
                f""" 
                <p style="line-height:150%; font-size: {font_size_sidebar};">
                    · Build a Fire<br>· Collect Shells<br>· Build a shelter<br>· Search for Food<br>· Build a Weapon<br>
                    · Collect Wood<br>· Watch the Sunset<br>· Search for drinking water<br>· Explore the surroundings
                    <br>· Search for a container (for food or water)
                </p>
                """, unsafe_allow_html=True)

            st.info("Keep in mind to not select the same task more than once.\nContinue once you are "
                    "finished with the button on the bottom right.",
                    icon="❕"
                    )

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
        selection_4 = st.multiselect("Not Urgent/Not Important", tasks, placeholder="Choose one or multiple options",
                                     label_visibility="collapsed")
        st.write(selection_4)

    col_a, col_b = st.columns((8, 1))
    with col_b:
        if st.button("Continue"):
            st.session_state.place = "map_4"
            st.rerun()
