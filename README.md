# 🏏 IPL Run Prediction - Streamlit App

This project predicts the **final score of an IPL match** based on current match data using **XGBoost** and **Streamlit**.  
The model is trained on **ball-by-ball IPL data** sourced from **Kaggle**.

---

## 🚀 Features
- Select **Batting Team**, **Bowling Team**, and **City**
- Enter **Current Overs**, **Runs Scored**, **Wickets Fallen**, **Last 5 Overs Runs**, and **Bowling Team Total Runs**
- Predict the **Final Score Range** for the batting team
- Interactive **Streamlit web interface** for real-time predictions

## ⚙️ Dependencies
- Python
- streamlit  
- pandas  
- numpy  
- scikit-learn  
- xgboost  

*(Listed in `requirements.txt`)*

---

## 📊 Model & Dataset
- **Model:** XGBoost regressor trained on IPL ball-by-ball data  
- **Dataset:** Kaggle IPL dataset (2008–2024)  
- Predicts the final score using features like overs left, current runs, wickets, and run rate.

---

## 🙌 Credits
- **Kaggle** – IPL ball-by-ball dataset  
- **XGBoost** – Machine Learning library for prediction  
- **Streamlit** – Web interface for interactive app  

---

