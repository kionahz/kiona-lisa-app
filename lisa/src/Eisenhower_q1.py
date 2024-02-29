import streamlit as st
import time



def render_eisenhower_q1():
    st.sidebar.progress(10)

    st.sidebar.markdown(f"""
        <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p>
        <p style="line-height: 100%; font-size: 1.3vw;"><strong>First Quest</strong></p>
    """, unsafe_allow_html=True)

    tasks = ["Search for a container (for food or water)", "Build a fire", "Build Shelter", "Collect Shells",
             "Collect Wood",
             "Watch the Sunset", "Search for drinking water", "Search for Food", "Build a Weapon",
             "Explore the surroundings"]

    col_1, col_2 = st.columns((1, 4))
    with col_1:
        st.image("../pictures/shelly.png")
    with col_2:
        st.title("Arranging tasks!")
        st.markdown(
            f""" <p style="line-height:130%; font-size: 1.5vw; color: white">You and your little brother are now stranded on 
            the deserted island. There are a lot of things you have to do in order to survive. But how should you 
            start?<br>Create an order of the tasks that you can see on the left by choosing on of the boxes and 
            selecting the task you would like to place there. You can rearrange your tasks indefinitely until you are 
            happy with your order.</p>""",
            unsafe_allow_html=True
        )


    st.divider()

    col3, colspace, colnumb,col4 = st.columns((2, 0.1, 0.18, 3))
    #col3, colnumb, col4, col5 = st.columns((2, 0.1, 3, 2))

    with col3:
        with st.expander(label="Here you can see all your tasks", expanded=True):
            st.markdown(f""" <p style="line-height:150%; font-size: 1.1vw; color: white">· Build a Fire<br>· Collect 
            Shells<br>· Build a shelter<br>· Search for Food<br>· Build a Weapon<br>· Collect Wood<br>· Watch the 
            Sunset<br>· Search for drinking water<br>· Explore the surroundings<br>· Search for a container (for food 
            or water)</p>""",
                        unsafe_allow_html=True)

            st.info("Keep in mind to not select the same task more than once.\nContinue once you are "
                    "finished with the button on the bottom right.", icon="❕") # TODO
    with colnumb:
        st.markdown(f"""
    <p style="text-align:right; font-size:1.7vw; line-height: 194%;">  1.<br>  2.<br>  3.<br>  4.<br>  5.<br>  6.<br>  7.<br>  8.<br>  9.<br>  10.<br></p>""",
                    unsafe_allow_html=True)
        #st.subheader("1.")
        #st.subheader("2.")
        #st.subheader("3.")
        #st.subheader("4.")
        #st.subheader("5.")
        #st.subheader("6.")
        #st.subheader("7.")
        #st.subheader("8.")
        #st.subheader("9.")
        #st.subheader("10.")

    with col4:
        select_1 = st.selectbox("1", tasks, index=None,
                                placeholder="Select what you would do first...", label_visibility="collapsed")
        select_2 = st.selectbox("2", tasks, index=None,
                                placeholder="Select what you would do second...", label_visibility="collapsed")
        select_3 = st.selectbox("3", tasks, index=None,
                                placeholder="Select what you would do third...", label_visibility="collapsed")
        select_4 = st.selectbox("4", tasks, index=None,
                                placeholder="Select what you would do fourth...", label_visibility="collapsed")
        select_5 = st.selectbox("5", tasks, index=None,
                                placeholder="Select what you would do fifth...", label_visibility="collapsed")
        select_6 = st.selectbox("6", tasks, index=None,
                                placeholder="Select what you would do sixth...", label_visibility="collapsed")
        select_7 = st.selectbox("7", tasks, index=None,
                                placeholder="Select what you would do seventh...", label_visibility="collapsed")
        select_8 = st.selectbox("8", tasks, index=None,
                                placeholder="Select what you would do eighth...", label_visibility="collapsed")
        select_9 = st.selectbox("9", tasks, index=None,
                                placeholder="Select what you would do ninth...", label_visibility="collapsed")
        select_10 = st.selectbox("10", tasks, index=None,
                                 placeholder="Select what you would do last...", label_visibility="collapsed")

    #with col5:
     #   st.write("1: ", select_1)
      #  st.write("2: ", select_2)
       # st.write("3: ", select_3)
        #st.write("4: ", select_4)
        #st.write("5: ", select_5)
       # st.write("6: ", select_6)
       # st.write("7: ", select_7)
       # st.write("8: ", select_8)
        #st.write("9: ", select_9)
        #st.write("10: ", select_10)

    cola, colb = st.columns((8, 1))
    with colb:
        # button to return to the map
        if st.button("Continue"):  # TODO
            st.session_state.place = "map_2"
            st.rerun()
