import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

# Title
st.title("Opioid Adulterant Potency Prediction")

# Introduction
st.markdown("""
## Introduction
This application predicts the potency of opioid adulterants based on their EC50 values. 
Understanding the potency of these substances is crucial for public health and safety.
""")

# Explanation of EC50
st.markdown("""
### What is EC50?
EC50 (half maximal effective concentration) is a measure of the concentration of a drug that produces 50% of its maximum response or effect. It is commonly used in pharmacology to indicate the potency of a substance.
""")

# Explanation of Potency
st.markdown("""
### What is Potency?
Potency refers to the amount of a substance required to produce a specific effect of given intensity. In this context, it is measured relative to DAMGO, a synthetic peptide used as a standard.
""")

# Note about model applicability
st.markdown("""
### Important Note
**This model is specifically designed for predicting the potency of opioid adulterants.** It should not be used for predicting the potency of substances outside this category.
""")

# File upload
st.markdown("""
### Upload CSV File
Please upload the CSV file containing the data with columns 'Substance', 'EC50_nM', and 'Potency'.
""")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    
    # Display the data
    st.write("### Data Preview")
    st.write(df.head())
    
    # Features and target
    X = df[['EC50_nM']]
    y = df['Potency']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Save the model
    model_path = os.path.expanduser('potency_prediction_model.pkl')
    joblib.dump(model, model_path)
    st.write(f"Model saved to {model_path}")
    
    # Predictions
    y_pred = model.predict(X_test)
    
    # Evaluation
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    st.write(f'Mean Squared Error: {mse}')
    st.write(f'R-squared: {r2}')
    
    # Input for prediction
    st.markdown("""
    ### Input EC50 Value for Prediction
    Please enter the EC50 value in nM (nanomolar). The EC50 value helps us understand the concentration required to achieve half of the substance's maximal effect.
    """)
    ec50_value = st.number_input('Enter EC50 value in nM', min_value=0.0, step=0.001)
    
    if st.button('Predict Potency'):
        prediction = model.predict(np.array([[ec50_value]]))
        st.write(f'The predicted potency relative to DAMGO is: {prediction[0]:.2f}x')
    
    # Footer with additional information
    st.markdown("""
    ## Additional Information
    This prediction is based on a linear regression model trained on a dataset of various opioid adulterants. The model predicts the relative potency of an adulterant based on its EC50 value.
    For more detailed information on the data and methodology, please refer to the documentation.
    """)

# Instructions for clients to upload data
st.markdown("""
## Instructions for Clients
1. Prepare your data in a CSV file with the following columns:
    - Substance: The name of the substance.
    - EC50_nM: The EC50 value of the substance in nanomolar (nM).
    - Potency: The potency of the substance relative to DAMGO.
2. Upload the CSV file using the file uploader above.
3. The app will automatically perform the modeling and display the results.
4. Enter the EC50 value in the input box to predict the potency.
""")
