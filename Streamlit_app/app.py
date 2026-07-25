import streamlit as st
import pandas as pd
import joblib

# Load assets
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "log_reg_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))
feature_columns = joblib.load(os.path.join(BASE_DIR, "feature_columns.pkl"))

# Page title
st.title("📉 Customer Churn Prediction")

st.write(
    "Predict whether a customer is likely to churn."
)
st.subheader("Customer Information")

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=35
)

tenure = st.number_input(
    "Tenure (Months)",
    min_value=0,
    max_value=120,
    value=12
)

monthly_charge = st.number_input(
    "Monthly Charge",
    min_value=0.0,
    value=70.0
)

satisfaction_score = st.slider(
    "Satisfaction Score",
    min_value=1,
    max_value=5,
    value=3
)
married = st.selectbox(
    "Married",
    ["No", "Yes"]
)

dependents = st.selectbox(
    "Dependents",
    ["No", "Yes"]
)

internet_service = st.selectbox(
    "Internet Service",
    ["No", "Yes"]
)

contract = st.selectbox(
    "Contract",
    ["Month-to-Month", "One Year", "Two Year"]
)
predict_button = st.button(
    "Predict Churn"
)
if predict_button:

    # Create customer record
    customer_data = {
        "Age": age,
        "TenureinMonths": tenure,
        "MonthlyCharge": monthly_charge,
        "SatisfactionScore": satisfaction_score,
    }

    # Convert to DataFrame
    customer_df = pd.DataFrame([customer_data])

    # Translation rules (one-hot encoding)

    customer_df["Married_Yes"] = (
        1 if married == "Yes" else 0
    )

    customer_df["Dependents_Yes"] = (
        1 if dependents == "Yes" else 0
    )

    customer_df["InternetService_Yes"] = (
        1 if internet_service == "Yes" else 0
    )

    customer_df["Contract_One Year"] = (
        1 if contract == "One Year" else 0
    )

    customer_df["Contract_Two Year"] = (
        1 if contract == "Two Year" else 0
    )

    # Add missing columns expected by model

    for col in feature_columns:
        if col not in customer_df.columns:
            customer_df[col] = 0

    # Reorder columns to match training

    customer_df = customer_df.reindex(
        columns=feature_columns,
        fill_value=0
    )

    # Scale data

    scaled_data = scaler.transform(
        customer_df
    )

    # Prediction

    prediction = model.predict(
        scaled_data
    )

    prediction_proba = model.predict_proba(
        scaled_data
    )

    churn_probability = (
        prediction_proba[0][1] * 100
    )

    # Results

    st.subheader("Prediction Results")

    st.metric(
        "Churn Risk",
        f"{churn_probability:.1f}%"
    )

    if prediction[0] == 1:

        st.error(
            "⚠️ Customer is likely to churn"
        )

        st.info(
            "Recommendation: Consider a retention offer or proactive customer engagement."
        )

    else:

        st.success(
            "✅ Customer is likely to stay"
        )

        st.info(
            "Recommendation: Continue standard customer engagement strategy."
        )