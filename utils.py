import pandas as pd
import numpy as np
import streamlit as st

def load_sample_data():
    """Load sample data for the dashboard"""
    dates = pd.date_range('2024-01-01', periods=100, freq='D')
    data = pd.DataFrame({
        'Date': dates,
        'Sales': np.random.randn(100).cumsum() + 100,
        'Visitors': np.random.randint(1000, 2000, 100),
        'Conversion': np.random.uniform(0.02, 0.05, 100),
        'Category': np.random.choice(['A', 'B', 'C', 'D'], 100),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], 100)
    })
    return data

def format_currency(value):
    """Format number as currency"""
    return f"${value:,.2f}"

def format_percentage(value):
    """Format number as percentage"""
    return f"{value:.2%}"

@st.cache_data
def get_summary_stats(df):
    """Calculate summary statistics"""
    return {
        'total_sales': df['Sales'].sum(),
        'avg_visitors': df['Visitors'].mean(),
        'avg_conversion': df['Conversion'].mean(),
        'total_days': len(df)
    }