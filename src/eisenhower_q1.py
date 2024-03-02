import streamlit as st
# TODO: Formatting done -> Comments

line_height_sidebar = "100%"
font_size_sidebar = "1.1vw"
font_size_sidebar_current = "1.3vw"
line_height = "130%"
font_size_text = "1.5vw"

tasks = ["Search for a container (for food or water)",
         "Build a fire",
         "Build Shelter",
         "Collect Shells",
         "Collect Wood",
         "Watch the Sunset",
         "Search for drinking water",
         "Search for Food",
         "Build a Weapon",
         "Explore the surroundings"
         ]


def render_eisenhower_q1():
    st.sidebar.progress(10)

    st.sidebar.markdown(
        f"""
        <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar};">
            Introduction
        </p>
        <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar_current};">
            <strong>First Quest</strong>
        </p>
        """, unsafe_allow_html=True
    )

    col_1, col_2 = st.columns((1, 4))
    with col_1:
        st.image("pictures/shelly.png")
    with col_2:
        st.title("Arranging tasks!")
        st.markdown(
            f""" 
            <p style="line-height:{line_height}; font-size: {font_size_text};"> 
               You and your little brother are stranded on the deserted island. So, there are a lot of things you have 
               to do in order to survive. But how should you start?<br>Create an order of the tasks that you can see on 
               the left by choosing one of the boxes and selecting the task you would like to place there. You can 
               rearrange your tasks indefinitely until you are happy with your order. 
            </p>
            """, unsafe_allow_html=True
                    )

    st.divider()

    col3, colspace, colnumb, col4 = st.columns((2, 0.1, 0.18, 3))
    with col3:
        with st.expander(label="Here you can see all your tasks", expanded=True):
            st.markdown(
                f""" 
                <p style="line-height:150%; font-size: {font_size_sidebar};">
                    · Build a Fire<br>· Collect Shells<br>· Build a shelter<br>· Search for Food<br>· Build a Weapon<br>
                    · Collect Wood<br>· Watch the Sunset<br>· Search for drinking water<br>· Explore the surroundings
                    <br>· Search for a container (for food or water)
                </p>""", unsafe_allow_html=True
            )

            st.info("Keep in mind to not select the same task more than once.\nContinue once you are finished with "
                    "the button on the bottom right.", icon="❕")
    with colnumb:
        st.markdown(
            f""" 
            <p style="text-align:right; font-size:1.7vw; line-height: 194%;">  
                1.<br>  2.<br>  3.<br>  4.<br>  5.<br>  6.<br>  7.<br>  8.<br>  9.<br>  10.<br>
            </p>
            """, unsafe_allow_html=True
        )

    with col4:
        st.selectbox("1", tasks, index=None,
                     placeholder="Select what you would do first...", label_visibility="collapsed")
        st.selectbox("2", tasks, index=None,
                     placeholder="Select what you would do second...", label_visibility="collapsed")
        st.selectbox("3", tasks, index=None,
                     placeholder="Select what you would do third...", label_visibility="collapsed")
        st.selectbox("4", tasks, index=None,
                     placeholder="Select what you would do fourth...", label_visibility="collapsed")
        st.selectbox("5", tasks, index=None,
                     placeholder="Select what you would do fifth...", label_visibility="collapsed")
        st.selectbox("6", tasks, index=None,
                     placeholder="Select what you would do sixth...", label_visibility="collapsed")
        st.selectbox("7", tasks, index=None,
                     placeholder="Select what you would do seventh...", label_visibility="collapsed")
        st.selectbox("8", tasks, index=None,
                     placeholder="Select what you would do eighth...", label_visibility="collapsed")
        st.selectbox("9", tasks, index=None,
                     placeholder="Select what you would do ninth...", label_visibility="collapsed")
        st.selectbox("10", tasks, index=None,
                     placeholder="Select what you would do last...", label_visibility="collapsed")

    col_a, col_b = st.columns((8, 1))
    with col_b:
        if st.button("Continue"):
            st.session_state.place = "map_2"
            st.rerun()
