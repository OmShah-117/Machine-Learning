import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import pickle
import os

# Define model path
MODEL_PATH = "A:/Machine Learning/Add/.vscode/advertising_sales_model.pkl"


# Load model with error handling
try:
    if os.path.exists(MODEL_PATH):
        model = pickle.load(open(MODEL_PATH, 'rb'))
    else:
        st.error(f"Model file not found at: {MODEL_PATH}")
        st.stop()
except Exception as e:
    st.error(f"Error loading model: {str(e)}")
    st.stop()

# ...existing code...
st.title("Advertising Sales Prediction")
tv=st.text_input("Enter TV Advertising Budget")
radio=st.text_input("Enter Radio Advertising Budget")
newspaper=st.text_input("Enter Newspaper Advertising Budget")

if st.button("Predict Sales"):
    features = np.array([[tv, radio, newspaper]],dtype=np.float64)
    results=model.predict(features).reshape(1,-1)
    st.write(f"Predicted Sales:", results[0])