import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("---Simple Data Dashboard---")

uploaded_file = st.file_uploader("Select a CSV file", type = "csv")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)

  st.subheader("Data Preview")
  st.write(df.head())

  st.subheader("Data Summary")
  st.write(df.describe())

  st.subheader("Filter Data")
  columns = df.columns.tolist()
  selected_columns = st.selectbox("Select the column to select by", columns)
  unique_values = df[selected_columns].unique()
  selected_value = st.selectbox("select value",unique_values)

  filtered_df = df[df[selected_columns] == selected_value]
  st.write(filtered_df)

  st.subheader("Plot Data")
  x_column = st.selectbox("Select x-columns", columns)
  y_column = st.selectbox("Select y-columns", columns)

  if st.button("Generate Plot"):
    if x_column == y_column:
      st.write("⚠️ X and Y cannot be the same column. Please select different columns.")
    else:
      st.line_chart(filtered_df.set_index(x_column)[y_column])
      

else:
  st.write("Waiting for file upload...")