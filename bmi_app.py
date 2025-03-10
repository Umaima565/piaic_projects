import streamlit as st
import pandas as pd

# Displaying the title of the BMI Calculator
title = "-----BMI Calculator-----"
st.title(title)

# User inputs height and weight using sliders
height = st.slider("Enter your height (in cm):", 100, 250, 175)  # Default height: 175 cm
weight = st.slider("Enter your weight (in kg):", 30, 200, 70)   # Default weight: 70 kg

# Calculating BMI using the standard formula
bmi = weight / ((height / 100) ** 2)

# Displaying the BMI value
st.write(f"Your BMI is: {bmi:.2f}")

# Providing BMI category information for reference
st.write("---BMI Categories---")
st.write("- Underweight: BMI is less than 18.5")
st.write("- Healthy weight: BMI is between 18.5 and 24.9")
st.write("- Overweight: BMI is between 25.0 and 29.9")
st.write("- Obesity: BMI is 30 or greater")
