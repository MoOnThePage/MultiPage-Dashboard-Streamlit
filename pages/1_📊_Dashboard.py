import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Dashboard", layout="wide")

# Title
st.title("📊 Dashboard")

# Sample data
@st.cache_data
def load_data():
    dates = pd.date_range('2024-01-01', periods=100, freq='D')
    data = pd.DataFrame({
        'Date': dates,
        'Sales': np.random.randn(100).cumsum() + 100,
        'Visitors': np.random.randint(1000, 2000, 100),
        'Conversion': np.random.uniform(0.02, 0.05, 100)
    })
    return data

# Load data
df = load_data()

# Filters
col1, col2, col3 = st.columns(3)
with col1:
    start_date = st.date_input("Start Date", value=df['Date'].min())
with col2:
    end_date = st.date_input("End Date", value=df['Date'].max())
with col3:
    metric = st.selectbox("Select Metric", ["Sales", "Visitors", "Conversion"])

# Filter data
mask = (df['Date'] >= pd.Timestamp(start_date)) & (df['Date'] <= pd.Timestamp(end_date))
filtered_df = df.loc[mask]

# Charts
tab1, tab2, tab3 = st.tabs(["📈 Line Chart", "📊 Bar Chart", "📋 Data Table"])

with tab1:
    fig = px.line(filtered_df, x='Date', y=metric, title=f'{metric} Over Time')
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    # Weekly aggregation
    filtered_df['Week'] = filtered_df['Date'].dt.isocalendar().week
    weekly_data = filtered_df.groupby('Week')[metric].mean().reset_index()
    fig2 = px.bar(weekly_data, x='Week', y=metric, title=f'Weekly {metric}')
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.dataframe(filtered_df, use_container_width=True)
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="dashboard_data.csv",
        mime="text/csv"
    )

# KPI Cards
st.subheader("Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Sales", f"${filtered_df['Sales'].sum():,.0f}")

with col2:
    st.metric("Avg Visitors", f"{filtered_df['Visitors'].mean():,.0f}")

with col3:
    st.metric("Avg Conversion", f"{filtered_df['Conversion'].mean():.2%}")

with col4:
    st.metric("Days", len(filtered_df))