## "House Price Prediction App

This project is a Machine Learning web application that predicts house prices based on various features such as area, number of bedrooms, bathrooms, parking, and other amenities.
It is built using Streamlit for the web interface and Scikit-learn for the machine learning model.

==> Project Structure
house_price_app/
│
├── app.py                   # Streamlit web app (UI + prediction)
├── main.ipynb               # Model training & data exploration
├── house_price_model.pkl    # Trained ML model
├── requirements.txt         # Dependencies for Streamlit
└── README.md                # Project documentation

## Features
Interactive web UI built with Streamlit
Predicts house prices instantly based on user input
Uses a Gradient Boosting Regressor model trained on real housing data
Easy to deploy on Streamlit Cloud or Render

## Tech Stack
Python
Streamlit – Web framework
Scikit-learn – Machine learning
Joblib – Model saving/loading
NumPy,pandas – Data handling
seaborn - visuals

## Deployment (Streamlit Cloud)
Push your project to GitHub.
Go to Streamlit Cloud
Click “New app” → Select your repo.
Set Main file path as app.py.
Click Deploy 

##
streamlit generates url:
https://your-username-house-price-predictor.streamlit.app

## Model Input Features
Feature	Description	Example
area	Total area of the house (sq ft)	2500
bedrooms	Number of bedrooms	3
bathrooms	Number of bathrooms	2
stories	Number of stories	2
mainroad	1 if connected to main road, else 0	1
guestroom	1 if available, else 0	0
basement	1 if available, else 0	1
hotwaterheating	1 if available, else 0	0
airconditioning	1 if available, else 0	1
parking	Number of parking spaces	2
prefarea	1 if preferred area, else 0	0
furnishingstatus	Encoded status (0 = unfurnished, 1 = semi, 2 = furnished)	2

## Example Output
When the user enters all feature values and clicks Predict,
the app will display:
✅ Predicted Price: 125.47 Lakhs
