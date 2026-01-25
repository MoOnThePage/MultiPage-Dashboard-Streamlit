import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="Analytics", layout="wide")

st.title("📈 Analytics")

# Generate sample data
np.random.seed(42)
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'] * 20,
    'Value': np.random.randn(100) * 10 + 50,
    'Group': np.random.choice(['X', 'Y', 'Z'], 100),
    'Score': np.random.uniform(0, 100, 100)
})

# Sidebar filters
st.sidebar.header("Filters")
categories = st.sidebar.multiselect(
    "Select Categories",
    options=data['Category'].unique(),
    default=data['Category'].unique()
)

groups = st.sidebar.multiselect(
    "Select Groups",
    options=data['Group'].unique(),
    default=data['Group'].unique()
)

# Filter data
filtered_data = data[
    (data['Category'].isin(categories)) &
    (data['Group'].isin(groups))
    ]

# Analysis tabs
tab1, tab2, tab3 = st.tabs(["Distribution", "Correlation", "Insights"])

with tab1:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Value Distribution")
        fig1 = go.Figure(data=[go.Histogram(x=filtered_data['Value'], nbinsx=20)])
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("Category Comparison")
        avg_by_category = filtered_data.groupby('Category')['Value'].mean().reset_index()
        fig2 = px.bar(avg_by_category, x='Category', y='Value')
        st.plotly_chart(fig2, use_container_width=True)

with tab2:
    st.subheader("Value vs Score Correlation")
    fig3 = px.scatter(
        filtered_data,
        x='Value',
        y='Score',
        color='Group',
        trendline="ols"
    )
    st.plotly_chart(fig3, use_container_width=True)

    # Correlation matrix
    st.subheader("Correlation Matrix")
    numeric_data = filtered_data.select_dtypes(include=[np.number])
    corr_matrix = numeric_data.corr()
    fig4 = px.imshow(corr_matrix, text_auto=True, aspect="auto")
    st.plotly_chart(fig4, use_container_width=True)

with tab3:
    st.subheader("Key Insights")

    col1, col2 = st.columns(2)

    with col1:
        st.info("**Top Categories by Value**")
        top_categories = filtered_data.groupby('Category')['Value'].mean().nlargest(3)
        for cat, val in top_categories.items():
            st.write(f"- {cat}: {val:.2f}")

    with col2:
        st.info("**Performance by Group**")
        group_stats = filtered_data.groupby('Group').agg({
            'Value': ['mean', 'std'],
            'Score': 'mean'
        }).round(2)
        st.dataframe(group_stats)

    # Summary statistics
    st.subheader("Summary Statistics")
    st.dataframe(filtered_data.describe())