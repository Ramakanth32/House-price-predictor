## Creating Web-user interface for machine learning model
import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("house_price_model.pkl")

st.title("🏠 House Price Prediction")

# List of features
numeric_features = ['area', 'bedrooms', 'bathrooms', 'stories', 'parking']
binary_features = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']
multi_features = ['furnishingstatus']

user_input = {}

# Numeric features
st.header("📏 Numeric Inputs")
for feature in numeric_features:
    user_input[feature] = st.number_input(f"Enter {feature}", min_value=0.0)

# Binary categorical features (Yes/No)
st.header("✅ Yes/No Inputs")
for feature in binary_features:
    user_input[feature] = st.selectbox(f"Does the house have {feature}?", ["Yes", "No"])
    user_input[feature] = 1 if user_input[feature] == "Yes" else 0

# Multi-category feature
st.header("🛋️ Furnishing Status")
furnishing = st.selectbox("Select furnishing status", ["furnished", "semi-furnished", "unfurnished"])
if furnishing == "furnished":
    user_input['furnishingstatus'] = 2
elif furnishing == "semi-furnished":
    user_input['furnishingstatus'] = 1
else:
    user_input['furnishingstatus'] = 0

# Prediction button
if st.button("Predict Price"):
    features_list = numeric_features + binary_features + multi_features
    features = np.array([[user_input[feature] for feature in features_list]])
    prediction = model.predict(features)
    st.success(f"💰 Predicted House Price: {prediction[0]:,.2f}")
