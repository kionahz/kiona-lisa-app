import streamlit as st
from Eisenhower_Q2 import Eisenhower_quest2
from Eisenhower_Q3 import Eisenhower_quest3

finished_quests = []


def set_up_sidebar():
    # Create the sidebar radio buttons
    current_quest = st.sidebar.radio("Quests", ["Home", "Backpack"])
    if current_quest == "Home":
        st.write("Welcome to the game!")
    elif current_quest == "Backpack":
        st.write("Your backpack is empty.")

    # Check if Quest 1 is finished
    if current_quest == "Home" and "Quest 1" not in finished_quests:
        quest_1_status = st.sidebar.radio("Quest 1", ["Not Completed", "Completed"])
        # If Quest 1 is completed, add it to the finished quests list
        if quest_1_status == "Completed":
            finished_quests.append("Quest 1")
            Eisenhower_quest2()
            # Add Quest 2 to the sidebar
            quest_2_status = st.sidebar.radio("Quest 2", ["Not Completed", "Completed"])
            # If Quest 2 is completed, add it to the finished quests list
            if quest_2_status == "Completed":
                finished_quests.append("Quest 2")
                Eisenhower_quest3()
                # Add Quest 3 to the sidebar
                quest_3_status = st.sidebar.radio("Quest 3", ["Not Completed", "Completed"])
                # If Quest 3 is completed, add it to the finished quests list
                if quest_3_status == "Completed":
                    finished_quests.append("Quest 3")
                    # Add Quest 4 to the sidebar
                    quest_4_status = st.sidebar.radio("Quest 4", ["Not Completed", "Completed"])
                    # If Quest 4 is completed, add it to the finished quests list
                    if quest_4_status == "Completed":
                        finished_quests.append("Quest 4")
                        # Add Quest 5 to the sidebar
                        quest_5_status = st.sidebar.radio("Quest 5", ["Not Completed", "Completed"])
                        # If Quest 5 is completed, add it to the finished quests list
                        if quest_5_status == "Completed":
                            finished_quests.append("Quest 5")
                            # Add Quest 6 to the sidebar
                            quest_6_status = st.sidebar.radio("Quest 6", ["Not Completed", "Completed"])
                            # If Quest 6 is completed, add it to the finished quests list
                            if quest_6_status == "Completed":
                                finished_quests.append("Quest 6")


set_up_sidebar()
