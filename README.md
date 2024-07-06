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
9. [Future Improvements](#future-improvements)
10. [Contributing](#contributing)
11. [Contact](#contact)

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
