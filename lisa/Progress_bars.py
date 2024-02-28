import streamlit as st
import time

# Main/ Introduction
progress_0 = st.sidebar.progress(0)
for percent_complete_0 in range(0):
    time.sleep(0.01)
    progress_0.progress(percent_complete_0)

# Map1
progress_10 = st.sidebar.progress(0)
for percent_complete_10 in range(1, 10):
    time.sleep(0.01)
    progress_10.progress(percent_complete_10)

# Backpack empty/ Eisenhower Q1
st.sidebar.progress(10)

#  Map2
progress_20 = st.sidebar.progress(0)
for percent_complete_20 in range(1, 20):
    time.sleep(0.01)
    progress_20.progress(percent_complete_20)

# Backpack1/ Eisenhower Method
st.sidebar.progress(20)

# / Map3/
progress_30 = st.sidebar.progress(0)
for percent_complete_30 in range(1, 30):
    time.sleep(0.01)
    progress_30.progress(percent_complete_30)

#Backpack2/ Eisenhower Q2
st.sidebar.progress(30)

# / Map4/
progress_40 = st.sidebar.progress(0)
for percent_complete_40 in range(1, 40):
    time.sleep(0.01)
    progress_40.progress(percent_complete_40)

# Backpack3/ Cornell Method
st.sidebar.progress(40)

# / Map5/
progress_50 = st.sidebar.progress(0)
for percent_complete_50 in range(1, 50):
    time.sleep(0.01)
    progress_50.progress(percent_complete_50)

# Blurting Method/ Backpack4
st.sidebar.progress(50)

#  Map6/
progress_60 = st.sidebar.progress(0)
for percent_complete_60 in range(1, 60):
    time.sleep(0.01)
    progress_60.progress(percent_complete_60)

# Pomodoro Q1/ Backpack5
st.sidebar.progress(60)

#  Map7/
progress_70 = st.sidebar.progress(0)
for percent_complete_70 in range(1, 70):
    time.sleep(0.01)
    progress_70.progress(percent_complete_70)

# Pomodoro Method/ Backpack6
st.sidebar.progress(70)

#  Map8/
progress_80 = st.sidebar.progress(0)
for percent_complete_80 in range(1, 80):
    time.sleep(0.01)
    progress_80.progress(percent_complete_80)

# Pomodoro Q2/ Backpack7
st.sidebar.progress(80)

#  Map9/
progress_90 = st.sidebar.progress(0)
for percent_complete_90 in range(1, 90):
    time.sleep(0.01)
    progress_90.progress(percent_complete_90)

# Backpack8 /
st.sidebar.progress(90)

# Sail away
progress_100 = st.sidebar.progress(0)
for percent_complete_100 in range(0, 101):
    time.sleep(0.01)
    progress_100.progress(percent_complete_100)

st.sidebar.progress(100)


time.sleep(1)
