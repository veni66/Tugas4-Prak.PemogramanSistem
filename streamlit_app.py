import streamlit as st
import pandas as pd

# Title of the app
st.title("Tampilkan Grafik Kolom Dataset")

# Upload CSV file
uploaded_file = st.file_uploader("Unggah file CSV", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    
    # Show dataset preview
    st.write("Dataset:")
    st.dataframe(df.head())
    
    # Select type of chart
    chart_type = st.selectbox(
        "Pilih jenis grafik",
        ("Line Chart", "Bar Chart", "Area Chart")
    )
    
    # Select columns from dataset
    columns = df.columns.tolist()
    selected_columns = st.multiselect("Pilih kolom untuk ditampilkan", columns)
    
    # Show checkbox to activate/deactivate charts
    for column in selected_columns:
        if st.checkbox(f"Tampilkan grafik untuk kolom: {column}"):
            st.write(f"Grafik untuk kolom: {column}")
            
            # Display the selected chart type
            if chart_type == "Line Chart":
                st.line_chart(df[[column]])
            elif chart_type == "Bar Chart":
                st.bar_chart(df[[column]])
            elif chart_type == "Area Chart":
                st.area_chart(df[[column]])
