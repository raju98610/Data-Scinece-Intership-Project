import streamlit as st
import joblib

st.title('Welcome to My Amazing Mart Profit Prediction App')
st.write('Enter the Sales and Actual Discount to predict Profit')

# Sidebar inputs
sales = st.sidebar.number_input('Sales', min_value=0.0)
actual_discount = st.sidebar.number_input('Actual Discount', min_value=0.0)

# Load your trained model
model = joblib.load('C:\Users\RAJU\OneDrive\Desktop\streamlit file')

# Predict
features = [[sales, actual_discount]]
predicted_profit = model.predict(features)[0]

st.write(f'Predicted Profit: ${predicted_profit:.2f}')
