import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

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

# Instructions for clients to upload data
st.markdown("""
## Instructions for Clients
1. Prepare your data in a CSV file with the following columns:
    - Substance: The name of the substance.
    - EC50_nM: The EC50 value of the substance in nanomolar (nM).
    - Potency: The potency of the substance relative to DAMGO.
2. Upload the CSV file using the file uploader below.
3. The app will automatically perform the modeling and display the results.
4. Enter the EC50 value in the input box to predict the potency.
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
    X = df['EC50_nM']
    y = df['Potency']
    
    # Create interpolation function
    interpolation_function = interp1d(X, y, fill_value="extrapolate")
    
    # Plot EC50 vs Potency
    plt.style.use('ggplot')
    fig, ax = plt.subplots()
    ax.plot(X, y, 'o', label='Data Points', color='blue')
    
    # Interpolation line
    X_new = np.linspace(X.min(), X.max(), 500)
    y_new = interpolation_function(X_new)
    y_new = np.clip(y_new, 0, None)  # Ensure predicted potency is not negative
    ax.plot(X_new, y_new, '--', label='Predictive Model', color='orange')
    
    # Customize plot
    ax.set_xlabel('EC50 (nM)')
    ax.set_ylabel('Potency')
    ax.set_title('EC50 vs Potency')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    st.pyplot(fig)
    
    # Input for prediction
    st.markdown("""
    ### Input EC50 Value for Prediction
    Please enter the EC50 value in nM (nanomolar). The EC50 value helps us understand the concentration required to achieve half of the substance's maximal effect.
    """)
    ec50_value = st.text_input('Enter EC50 value in nM', value="", placeholder="Enter a value greater than 0")

    if ec50_value:
        try:
            ec50_value = float(ec50_value)
            if ec50_value > 0:
                if st.button('Predict Potency'):
                    prediction = interpolation_function(ec50_value)
                    prediction = np.clip(prediction, 0, None)  # Ensure predicted potency is not negative
                    st.write(f'The predicted potency relative to DAMGO is: {prediction:.2f}x')
            else:
                st.write("Please enter a valid EC50 value greater than 0.")
        except ValueError:
            st.write("Please enter a valid numerical value.")

# Footer with additional information
st.markdown("""
## Additional Information
This prediction is based on an interpolation model trained on a dataset of various opioid adulterants. The model predicts the relative potency of an adulterant based on its EC50 value.
The model and web app are able to predict the potency of opioids as the data evolves and we have more data to make predictions based on them. It is an interactive dashboard that can be easily worked with by providing updated data.
**Data should be in CSV format with the following columns: `Substance`, `EC50_nM`, `Potency`.**
""")
