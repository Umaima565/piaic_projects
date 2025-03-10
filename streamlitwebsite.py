import streamlit as st  # Import Streamlit for UI
import pandas as pd  # Import Pandas for data handling
import matplotlib.pyplot as plt  # Import Matplotlib for visualizations

# Title of the web application
st.title("--- Simple Data Dashboard ---")

# File uploader to allow users to upload a CSV file
uploaded_file = st.file_uploader("Select a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)  # Read the uploaded CSV file

    # Display the first few rows of the dataset
    st.subheader("Data Preview")
    st.write(df.head())

    # Show statistical summary of the dataset
    st.subheader("Data Summary")
    st.write(df.describe())

    # Filtering data based on user input
    st.subheader("Filter Data")
    columns = df.columns.tolist()  # Get all column names
    selected_columns = st.selectbox("Select the column to filter by:", columns)
    unique_values = df[selected_columns].unique()  # Get unique values from the column
    selected_value = st.selectbox("Select a value:", unique_values)

    # Filter the dataframe based on user selection
    filtered_df = df[df[selected_columns] == selected_value]  
    st.write(filtered_df)  # Show filtered data

    # Visualization section
    st.subheader("Plot Data")
    x_column = st.selectbox("Select X-axis column:", columns)
    y_column = st.selectbox("Select Y-axis column:", columns)

    # Generate a plot when button is clicked
    if st.button("Generate Plot"):
        if x_column == y_column:
            st.write("⚠️ X and Y cannot be the same column. Please select different columns.")
        else:
            st.line_chart(filtered_df.set_index(x_column)[y_column])  # Display a line chart

else:
    st.write("Waiting for file upload...")  # Display message when no file is uploaded
