import streamlit as st

# Define the options for the multiselects
options = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Create a session state to store the selected options
session_state = st.session_state

# Initialize the selected options if they don't exist in the session state
if "selected_options" not in session_state:
    session_state.selected_options = {}

# Create four multiselects with the same options
selected_options = []
for i in range(4):
    selected_options.append(st.multiselect(f"Multiselect {i+1}", options=options))

    # Update the session state with the selected options
    session_state.selected_options[i] = selected_options[i]

# Remove selected options from other multiselects
for i in range(4):
    for j in range(4):
        if i != j:
            selected_options[i] = [option for option in selected_options[i] if option not in session_state.selected_options[j]]

# Display the selected options
for i, select in enumerate(selected_options):
    st.write(f"Selected options for Multiselect {i+1}: {select}")
