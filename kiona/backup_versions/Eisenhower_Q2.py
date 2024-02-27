import streamlit as st
import game_def_test


def Eisenhower_quest2():
    initial_sidebar_state = "collapsed"
    st.title("Eisenhower Matrix")
    tab_titles = ["Eisenhower Matrix", "(1) Do", "(2) Schedule", "(3) Delegate", "(4) Delete", "Did you know?"]
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(tab_titles)

    with tab1:
        col1, col2 = st.columns((2,1))
        with col1:
            st.image("../pictures/em_empty.png")
        with col2:
            st.markdown(
                f""" <p style="line-height:130%; font-size:2vw; color:white">This is the Eisenhower matrix.</p>
                <p style="line-height:130%; font-size: 1.5vw; color: white">It's 
                great for organizing and prioritizing tasks. The tasks are divided into important and unimportant, 
                as well as urgent and non-urgent. This results in a table with 4 fields.<br><br>
                Continue clicking through the tabs above to learn more about each field</p>""",
                unsafe_allow_html=True
            )


    with tab2:
        col1, col2 = st.columns((2, 1))
        with col1:
            st.image("../pictures/em_do.png")
        with col2:
            st.markdown(
                f""" <p style="line-height:130%; font-size: 2vw; color: white">Field number 1:<br>Urgent and 
                Important</p> <p style="line-height:130%; font-size: 1.5vw; color: white">These are tasks that you 
                should complete immediately, otherwise there are consequences, such as you could die of thirst 
                without clean drinking water. </p> """,
                unsafe_allow_html=True
            )

    with tab3:
        col1, col2 = st.columns((2, 1))
        with col1:
            st.image("../pictures/em_schedule.png")
        with col2:
            st.markdown(
                f""" <p style="line-height: 130%; font-size: 2vw; color: white">Field number 2:<br>Not Urgent but 
                Important</p> <p style="line-height:130%; font-size: 1.5vw; color: white">These are tasks that you 
                definitely have to complete, but not as the very first thing. You can postpone these tasks to a later 
                date, but you still have to complete them because they are important in the long term, 
                such as building a weapon.</p>""",
                unsafe_allow_html=True
            )

    with tab4:
        col1, col2 = st.columns((2, 1))
        with col1:
            st.image("../pictures/em_delegate.png")
        with col2:
            st.markdown(
                f""" <p style="line-height: 130%; font-size: 2vw; color: white">Field number 3:<br>Urgent but not 
                Important</p> 
                <p style="line-height:130%; font-size: 1.5vw; color: white">These are tasks that need to 
                be done urgently, but are not so important that you absolutely have to do them. Perhaps you can pass 
                the tasks on, in this case to your little brother. Finding wood, for example, is urgent for fires, 
                shelters and weapons, but doesn't necessarily require your skills and can also be done by him.</p>""",
                unsafe_allow_html=True
            )

    with tab5:
        col1, col2 = st.columns((2, 1))
        with col1:
            st.image("../pictures/em_delete.png")
        with col2:
            st.markdown(
                f""" <p style="line-height: 130%; font-size: 2vw; color: white">Field number 4:<br>Not Urgent and not 
                Important</p> <p style="line-height:130%; font-size: 1.5vw; color: white">These tasks are often 
                unnecessary tasks. Like watching the sunset, for example. This activity does not bring you any closer 
                to your goal and should only be done when everything else has already been ticked off.</p>""",
                unsafe_allow_html=True
            )

    with tab6:
        col1, col2 = st.columns(2)
        with col1:
            st.image("../pictures/Dwight_D._Eisenhower.jpg")
        with col2:
            st.markdown(
                f"""<p style="line-height: 130%; font-size: 2vw; color: white">Did you know?</p> <p 
                style="line-height:130%; font-size: 1.5vw; color: white"> Back in 1954, US President Dwight D. 
                Eisenhower mentioned in one of his speeches that he has a problem with time management, 
                where he always encounters the same problems: "I have two kinds of problems, the urgent and the 
                important. The urgent ones are not important, and the important ones are never urgent." Does it sound 
                familiar to you?<br><br>Now, fast forward a bit to Stephen Covey, the genius behind a book called 
                "The 7 Habits of Highly Effective People" took Eisenhower's words and turned it into what we now call 
                the Eisenhower Matrix. Also, it goes by a few other names like the Eisenhower Principle or the 
                Urgent-Important Matrix.<br><br>Cool, huh? So even a president was struggling with the same problem 
                as you might be. </p>""",
                unsafe_allow_html=True
            )
        # while Schleife
        if st.button("Next Quest"):
            # st.session_state["scenes_counter"]["intro_counter"] += 1
            st.session_state.place = "Eisenhower_Q3"
            game_def_test.temp_clear()
            st.rerun()


