import streamlit as st
import pandas as pd
import numpy as np
import math
import pickle
import os
import sys

filename = "C:/Users/jenil/OneDrive/Desktop/Jupyter/Run Predication/run.pkl"

model = pickle.load(open(filename, "rb"))

st.title("🏏 Cricket Match Prediction")

teams = ['Chennai Super Kings', 'Mumbai Indians', 'Delhi Capitals', 'Kolkata Knight Riders', 'Punjab Kings',                                                                'Royal Challengers Bengaluru', 'Sunrisers Hyderabad', 'Rajasthan Royals', 'Lucknow Super Giants', 'Gujarat Titans']

cities = ['Chandigarh', 'Delhi', 'Kolkata', 'Jaipur', 'Hyderabad', 'Chennai',
        'Mumbai', 'Cape Town', 'Durban', 'Port Elizabeth', 'Centurion',
       'East London', 'Johannesburg', 'Kimberley', 'Bloemfontein',
       'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala', 'Visakhapatnam',
       'Pune', 'Bangalore', 'Raipur', 'Abu Dhabi', 'Ranchi', 'Rajkot',
       'Kanpur', 'Indore', 'Dubai', 'Sharjah', 'Navi Mumbai', 'Lucknow',
       'Guwahati', 'Mohali', 'Bengaluru']


Batting_team = st.selectbox("Batting Team", teams)
Bowling_team = st.selectbox("Bowling Team", teams)
city = st.selectbox("City", cities)


col1, col2 = st.columns(2)
with col1:
    overs = st.number_input("Current Over", min_value = 5.1, max_value = 19.5, step = 0.1)
    if overs - math.floor(overs) > 0.5:
        st.error("Oner over has only 6 balls;")
with col2:
    runs = st.number_input("Current Runs", min_value = 0, max_value = 354, step = 1)


col3, col4 = st.columns(2)
with col3: 
    crr = st.number_input("Current Run Rate", min_value=0.0, max_value=20.0, step=0.1)
with col4:
    last_5_overs = st.number_input("Last 5 overs Run", min_value = 0, step = 1)

col5, col6 = st.columns(2)
with col5:
    total_runs = st.number_input("Total Runs by Bowling_team", min_value = 0, step = 1)

wicket = st.slider("Wicket Fallen", 0, 9)

full_over = math.floor(overs)
ball_in_overs = round((overs - full_over)*10)

ball_left = 120 - (full_over*6 + ball_in_overs)
wicket_left = 10 - wicket

prediction_array = np.array([Batting_team, Bowling_team, runs, city, ball_left, last_5_overs, crr, total_runs, wicket_left])
prediction_array = pd.DataFrame([prediction_array], columns = ['batting_team', 'bowling_team', 'current_run', 'city', 'ball_left', 'last_5_overs', 'crr', 'total_runs_x', 'wicket_left'])

if st.button('Predict Score'):
    predicted_score = int(round(model.predict(prediction_array)[0]))
    st.success(f"PREDICTED MATCH SCORE: {predicted_score-5} to {predicted_score+5}")

if __name__ == "__main__":
    os.system(f"streamlit run {sys.argv[0]}")