import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fraud_model.pkl")
scaler = joblib.load("amount_scaler.pkl")

st.title("Credit Card Fraud")

amount = st.number_input("Transaction Amount", min_value = 0.0, value = 100.00)

st.subheader("Transaction Features")

values = {}

for i in range(1, 29):
    values[f"V{i}"] = 0.0

if st.button("Predict"):
    amount_scaled = scaler.transform([[amount]])[0][0]
    feature_names = [
    "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8",
    "V9", "V10", "V11", "V12", "V13", "V14", "V15",
    "V16", "V17", "V18", "V19", "V20", "V21", "V22",
    "V23", "V24", "V25", "V26", "V27", "V28",
    "Amount_scaled"
    ]
    input_data = { **values, 'Amount scaled:' : amount_scaled }
    input_df = pd.DataFrame([[values[f"V{i}"] for i in range(1, 29)] + [amount_scaled]], columns = feature_names)

    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.error("fraud")
    else:
        st.success("Normal Transaction")
    
