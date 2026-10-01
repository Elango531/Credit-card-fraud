import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fraud_model.pkl")
scaler = joblib.load("amount_scaler.pkl")

st.title("Credit Card Fraud")

st.write("Enter the transaction details below.")

amount = st.number_input("Transaction Amount" min_value = 0.0, value = 100.00")

st.subheader("Transaction Features")

values = {}

for i in range(1, 29):
    values = [f"V{i}"] = st.number_input(f"V{i}"), values = 0.0

if st.button("Predict"):
    amount_scaled = scaler.transform([[amount]])[0][0]
    input_data = { **values, 'Amount scaled:' : amount_scaled }
    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.error("fraud")
    else:
        st.success("Normal Transaction")
    
