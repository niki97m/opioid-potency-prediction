# Opioid Adulterant Potency Prediction

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Data Requirements](#data-requirements)
6. [Model Description](#model-description)
7. [Web Application](#web-application)
8. [Code Structure](#code-structure)
9. [Contact](#contact)

## Introduction

The Opioid Adulterant Potency Prediction tool is a web application designed to predict the potency of opioid adulterants based on their EC50 (half maximal effective concentration) values. This tool is crucial for public health and safety professionals, researchers, and law enforcement agencies working to combat the opioid crisis.

Understanding the potency of opioid adulterants is vital for:
- Assessing the danger of new synthetic opioids
- Developing appropriate harm reduction strategies
- Informing medical treatment protocols for overdose cases
- Guiding policy decisions and public health interventions

This application uses a data-driven approach to provide quick and reliable potency estimates, potentially saving lives by offering timely information about new and emerging opioid threats.

## Features

1. **Data Upload**: Users can upload their own CSV files containing data on opioid adulterants.
2. **Interactive Visualization**: The app generates a plot showing the relationship between EC50 values and potency.
3. **Potency Prediction**: Users can input an EC50 value to receive a predicted potency relative to DAMGO (a standard synthetic opioid).
4. **Responsive Design**: The web app is built with Streamlit, ensuring a responsive and user-friendly interface across devices.
5. **Educational Content**: Includes explanations of key concepts like EC50 and potency.

## Installation

To run this application locally, follow these steps:

1. Clone the repository:
   
  - git clone https://github.com/niki97m/opioid-potency-prediction.git
  - cd opioid-potency-prediction

2. Create a virtual environment (optional but recommended):
  - python -m venv venv
  - source venv/bin/activate  # On Windows, use venv\Scripts\activate

3. Install the required packages:
  - pip install -r requirements.txt

## Usage

To run the application:

1. Navigate to the project directory.
2. Run the Streamlit app: streamlit run app.py
3. Open a web browser and go to `http://localhost:8501` (or the address provided in the terminal).

## Data Requirements

The application expects a CSV file with the following columns:
- `Substance`: The name of the opioid adulterant
- `EC50_nM`: The EC50 value of the substance in nanomolar (nM)
- `Potency`: The known potency of the substance relative to DAMGO

## Model Description

The prediction model uses scipy's `interp1d` function to perform interpolation between known data points. This approach allows for:

1. **Flexibility**: The model adapts to the provided data, making it useful as new opioid adulterants are discovered.
2. **Interpretability**: The relationship between EC50 and potency is visualized, allowing users to understand the prediction process.
3. **Extrapolation**: The model can make predictions outside the range of provided data, though these should be interpreted cautiously.

The model performs the following steps:
1. Reads the uploaded CSV file
2. Extracts EC50 and Potency values
3. Creates an interpolation function
4. Uses this function to predict potency for new EC50 values

Note: The model ensures that predicted potency values are non-negative by using numpy's `clip` function.

## Web Application

The web application is built using Streamlit and consists of several sections:

1. **Title and Introduction**: Explains the purpose and importance of the tool.
2. **Explanations**: Provides definitions for EC50 and potency.
3. **Important Note**: Clarifies the specific use case for the model (opioid adulterants only).
4. **Instructions**: Guides users on how to prepare and upload their data.
5. **File Upload**: Allows users to upload their CSV file.
6. **Data Preview**: Displays the first few rows of the uploaded data.
7. **Visualization**: Shows a plot of EC50 vs Potency, including both data points and the interpolation line.
8. **Prediction Input**: Provides a text input for users to enter an EC50 value for prediction.
9. **Prediction Output**: Displays the predicted potency based on the entered EC50 value.
10. **Additional Information**: Offers context about the model and its limitations.

## Code Structure

The main application code (`app.py`) is structured as follows:

1. **Import Statements**: Importing necessary libraries (Streamlit, Pandas, NumPy, Matplotlib, SciPy).
2. **Title and Introduction**: Setting up the app's title and introductory text.
3. **Explanations**: Providing markdown text to explain key concepts.
4. **File Upload**: Implementing file upload functionality.
5. **Data Processing**: Reading and displaying the uploaded CSV file.
6. **Model Creation**: Creating the interpolation function.
7. **Visualization**: Generating the EC50 vs Potency plot.
8. **Prediction Interface**: Implementing the input field for EC50 and the prediction button.
9. **Prediction Logic**: Calculating and displaying the predicted potency.
10. **Footer**: Adding additional information about the model and data requirements.


## Contact

For questions, suggestions, or collaborations, please contact:

[Niki Mahmoodzadeh]
Email: [niki.mahmoodzadeh@mail.mcgill.ca]

Project Link: [https://github.com/niki97m/opioid-potency-prediction](https://github.com/niki97m/opioid-potency-prediction)

Live Application: [https://opioid-potency-prediction.streamlit.app](https://opioid-potency-prediction.streamlit.app)
