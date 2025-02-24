import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO  # Corrected import

def show_converter():
    st.title("✨Data Sweeper By Talha Mehmood")
    st.write("Transform your files between OSV and Excel formats with built-in data cleaning and visualization!")
    
    uploaded_files = st.file_uploader("Upload your file (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)
    
    if uploaded_files:
        for file in uploaded_files:
            file_ext = os.path.splitext(file.name)[-1].lower()

            if file_ext == ".csv":
                df = pd.read_csv(file)
            elif file_ext == ".xlsx":
                df = pd.read_excel(file, engine="openpyxl")
            else:
                st.error(f"Unsupported file type: {file_ext}")
                continue

            st.write(f"**File Name:** {file.name}")
            st.write(f"**File Size:** {file.size / 1024:.2f} KB")

            st.write("Preview the Head of the Dataframe")
            st.dataframe(df.head())

            st.subheader("📊 Data Visualization")
            numeric_columns = df.select_dtypes(include=['number']).columns
            if not numeric_columns.empty:
                chart_type = st.selectbox("Select chart type:", ["Histogram", "Scatter Plot"], key=file.name)
                selected_column = st.selectbox("Select a numeric column:", numeric_columns, key=f"num_{file.name}")
                
                if st.button(f"Generate {chart_type} for {file.name}"):
                    fig, ax = plt.subplots()
                    if chart_type == "Histogram":
                        sns.histplot(df[selected_column], kde=True, ax=ax)
                    elif chart_type == "Scatter Plot":
                        second_column = st.selectbox("Select another numeric column:", numeric_columns, key=f"num2_{file.name}")
                        sns.scatterplot(x=df[selected_column], y=df[second_column], ax=ax)
                    
                    st.pyplot(fig)
            else:
                st.warning("No numeric columns found for visualization.")
            
            st.subheader("Data Cleaning Options")
            if st.checkbox(f"Clean Data for {file.name}"):
                col1, col2 = st.columns(2)

                with col1:
                    if st.button(f"Remove Duplicates from {file.name}"):
                        df.drop_duplicates(inplace=True)
                        st.write("Duplicates Removed!!!")

                with col2:
                    if st.button(f"Fill Missing Value for {file.name}"):
                        numeric_cols = df.select_dtypes(include=['number']).columns  
                        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                        st.write("Missing Values Filled!")

            st.subheader("⚙️ Conversion Options")
            conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
            
            if st.button(f"Convert {file.name}"):
                buffer = BytesIO()
                
                if conversion_type == "CSV":
                    df.to_csv(buffer, index=False)
                    file_name = file.name.replace(".xlsx", ".csv")
                    mime_type = "text/csv"
                
                elif conversion_type == "Excel":
                    df.to_excel(buffer, index=False, engine="openpyxl")
                    file_name = file.name.replace(".csv", ".xlsx")
                    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                
                buffer.seek(0)
            
                st.download_button(
                    label=f"⬇️ Download {file.name} as {conversion_type}",
                    data=buffer,
                    file_name=file_name,
                    mime=mime_type
                )
                
st.success("All Files Processed Successfully!!!!")
