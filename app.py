import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="AI CRM Intelligence",
    page_icon="📊",
    layout="wide"
)

# Application title
st.title("📊 AI CRM Intelligence")
st.subheader("AI-Powered CRM Data Quality & Intelligence Platform")

st.markdown("""
Welcome to AI CRM Intelligence.

Upload your CRM data to identify data quality issues,
detect duplicates, and generate actionable insights.
""")

st.divider()

# File upload
st.header("📁 Upload CRM Data")

uploaded_file = st.file_uploader(
    "Upload an Excel or CSV file",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success("File uploaded successfully!")

        st.header("📋 CRM Data Overview")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total Records", len(df))

        with col2:
            st.metric("Total Columns", len(df.columns))

        with col3:
            missing_values = int(df.isnull().sum().sum())
            st.metric("Missing Values", missing_values)

        st.subheader("Data Preview")
        st.dataframe(df.head(100), use_container_width=True)

        st.subheader("Data Quality Overview")

        missing_data = df.isnull().sum()

        quality_df = pd.DataFrame({
            "Column": missing_data.index,
            "Missing Values": missing_data.values
        })

        fig = px.bar(
            quality_df,
            x="Column",
            y="Missing Values",
            title="Missing Values by Column"
        )

        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"Error processing file: {e}")

else:
    st.info("Upload a CRM file to begin your data quality analysis.")