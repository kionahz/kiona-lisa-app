import streamlit as st
import time


def render_cornell_method():
    st.sidebar.progress(40)

    st.sidebar.markdown(f"""
    <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower First Try</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Method</p>
    <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Applied</p>
        <p style="line-height: 100%; font-size: 1.3vw;"><strong>Cornell Method</strong></p>
    """, unsafe_allow_html=True)

    tab_titles = ["Strange Encounter", "Cornell Method", "Main Notes", "Side", "Summary", "Did you know?"]
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(tab_titles)

    with tab1:
        col1, col2 = st.columns((3, 5), gap='large')
        with col1:
            st.markdown(f""" <p style="line-height:130%; font-size: 1.3vw; color: 
                    white"><br><br></p>""", unsafe_allow_html=True)
            st.image("pictures/shelly_without.png")

        with col2:
            st.markdown(
                f""" <p style="line-height:130%; font-size: 2vw; color: white">Wow, what a strange encounter!</p><p 
                style="line-height:130%; font-size: 1.5vw; color: white">He was rambling quite a lot, right? But he 
                also said some very helpful things. Did you remember any of them?<br><br>In this next part I will 
                show you another method. This one is quiet helpful for writing down notes and keeping them 
                structured. I´m already starting to forget what the pirate said... was it food or water 
                first?<br><br>Let´s quickly start with this method, so you will know how to structure your notes and 
                not be so forgetful as me.</p>""",
                unsafe_allow_html=True
            )

    with tab2:
        col1, col2, col3, col4 = st.columns((1, 3, 4, 1))
        with col2:
            st.image("pictures/cornell.png")

        with col3:
            st.markdown(
                f""" <p style="line-height:130%; font-size:2vw; color:white">This is the Cornell Method</p> <p 
                style="line-height:130%; font-size: 1.5vw; color: white">As I said, its great for organizing and 
                understanding information better and keeping it structured.<br><br>First divide your paper into three 
                sections. On the left side you have a narrow column for Keywords and Questions, the right side is for 
                taking notes and a bottom part for a summary. At the top you can add a title and date so it is easier 
                for you to associate your notes.</p>""",
                unsafe_allow_html=True
            )

    with tab3:
        col1, col2, col3, col4 = st.columns((1, 3, 4, 1))
        with col2:
            st.image("pictures/cornell.png")

        with col3:
            st.markdown(
                f""" <p style="line-height:130%; font-size:2vw; color:white">Key Notes</p> <p 
                style="line-height:130%; font-size: 1.5vw; color: white">As you are reading or listening to new 
                information, write down the key points, details and explanations in the large right column.<br><br>Try to 
                use your own words and keep them as short as possible, so you understand the information better.</p>""",
                unsafe_allow_html=True
            )

    with tab4:
        col1, col2, col3, col4 = st.columns((1, 3, 4, 1))
        with col2:
            st.image("pictures/cornell.png")

        with col3:
            st.markdown(
                f""" <p style="line-height:130%; font-size:2vw; color:white">Side</p> <p style="line-height:130%; 
                font-size: 1.5vw; color: white">On the left side you can focus on writing down the most important 
                key points that summarize your key notes, as well as questions about what you are learning.<br><br>This will 
                help you to stay even more focused and find the most important keywords at a glance.</p>""",
                unsafe_allow_html=True
            )

    with tab5:
        col1, col2, col3, col4 = st.columns((1, 3, 4, 1))
        with col2:
            st.image("pictures/cornell.png")

        with col3:
            st.markdown(
                f""" <p style="line-height:130%; font-size:2vw; color:white">Summary</p> <p style="line-height:130%; 
                font-size: 1.5vw; color: white">After you finished taking all your notes, write a short summary at 
                the bottom of the page. This will help you review everything at once.<br><br>When you finished 
                writing everything down, you can use the paper to see what you remember and review it. For that you 
                can cover up the right side, where your notes are, and try to answer the questions or explain the 
                main ideas only using the left column.<br><br>If you use this method before a test or exam, 
                you can review the summaries at the bottom to remember all your key points.</p>""",
                unsafe_allow_html=True
            )

    with tab6:
        col1, col2, col3, col4 = st.columns((1, 3, 4, 1))
        with col2:
            st.image("pictures/cornell.png")

        with col3:
            st.markdown(
                f""" <p style="line-height:130%; font-size:2vw; color:white">Did you know?</p> <p 
                style="line-height:130%; font-size: 1.5vw; color: white">This method was developed at the Cornell 
                University by a professor for their students, so they could take better notes and encourage active 
                studying.<br><br>So, if you are already learning this method right now, it will be super easy for 
                you at university. Very impressive!</p>""",
                unsafe_allow_html=True
            )

        cola, colb = st.columns((8, 1))
        with colb:
            if st.button("Continue"):
                st.session_state.place = "map_5"
                st.rerun()
