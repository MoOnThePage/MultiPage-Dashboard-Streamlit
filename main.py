import streamlit as st

# Define the pages
Home = st.Page("home.py", title = "Home", icon = "🏠")
Dashboard = st.Page("Dashboard.py", title = "Dashboard", icon = "📊")
Analytics = st.Page("Analytics.py", title = "Analytics", icon = "📈")
Plotting = st.Page("Plotting.py", title = "Plotting", icon = "📈")
Mapping = st.Page("Mapping.py", title = "Mapping", icon = "🌍")
DataFrame = st.Page("DataFrame.py", title = "Data Frame", icon = "📊")
Webcam = st.Page("Webcam.py", title = "Webcam", icon = "📷")
Settings = st.Page("Settings.py", title = "Settings", icon = "⚙️")

# Set up navigation
nav = st.navigation([
    Home,
    Dashboard,
    Analytics,
    Plotting,
    Mapping,
    DataFrame,
    Webcam,
    Settings,
])

# Run the selected page
nav.run()
