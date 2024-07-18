import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('Lung_Cancer_Model_Trained.pkl')

# Define the numeric columns
numeric_columns = [
    'Tumor_Size_mm', 'Alanine_Aminotransferase_Level', 
    'Aspartate_Aminotransferase_Level', 'Creatinine_Level', 
    'LDH_Level', 'Calcium_Level', 'Phosphorus_Level', 'Glucose_Level',
    'Potassium_Level', 'Sodium_Level'
]

# Streamlit app
st.title('Cancer Stage Prediction')

# Create input fields for the numeric columns
input_data = []
for col in numeric_columns:
    value = st.number_input(f'Enter {col}', min_value=0.0, format="%.2f")
    input_data.append(value)

# Convert input data to a DataFrame
input_df = pd.DataFrame([input_data], columns=numeric_columns)

# Predict the stage using the model
if st.button('Predict'):
    prediction = model.predict(input_df)
    st.write(f'The predicted cancer stage is: {prediction[0]}')

