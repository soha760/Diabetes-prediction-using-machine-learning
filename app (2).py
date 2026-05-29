import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("Diabetes Prediction App")

st.write("Enter patient information to predict diabetes.")

# User Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=1, max_value=120, value=30)

hypertension = st.selectbox("Hypertension", [0, 1])
heart_disease = st.selectbox("Heart Disease", [0, 1])

smoking_history = st.selectbox(
    "Smoking History",
    ["never", "No Info", "current", "former", "ever", "not current"]
)

bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)

HbA1c_level = st.number_input("HbA1c Level", min_value=3.0, max_value=15.0, value=5.5)

blood_glucose_level = st.number_input(
    "Blood Glucose Level",
    min_value=50,
    max_value=300,
    value=100
)

# Convert categorical data
gender_male = 1 if gender == "Male" else 0

smoking_dict = {
    "No Info": 0,
    "current": 1,
    "ever": 2,
    "former": 3,
    "never": 4,
    "not current": 5
}

smoking_encoded = smoking_dict[smoking_history]

# Create dataframe
input_data = pd.DataFrame({
    'age': [age],
    'hypertension': [hypertension],
    'heart_disease': [heart_disease],
    'bmi': [bmi],
    'HbA1c_level': [HbA1c_level],
    'blood_glucose_level': [blood_glucose_level],
    'gender_Male': [gender_male],
    'smoking_history': [smoking_encoded]
})

# Scale input
input_scaled = scaler.transform(input_data)

# Prediction
if st.button("Predict"):

    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("The patient is likely to have diabetes.")
    else:
        st.success("The patient is unlikely to have diabetes.")