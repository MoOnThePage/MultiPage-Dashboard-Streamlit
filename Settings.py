import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

st.title("⚙️ Settings")

# User settings
st.header("User Preferences")

with st.form("user_settings"):
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Name", value="John Doe")
        email = st.text_input("Email", value="john@example.com")
        timezone = st.selectbox(
            "Timezone",
            ["UTC", "EST", "PST", "GMT", "CET"]
        )

    with col2:
        notification_email = st.checkbox("Email Notifications", value=True)
        notification_push = st.checkbox("Push Notifications", value=False)
        data_refresh = st.slider(
            "Data Refresh Rate (minutes)",
            min_value=1,
            max_value=60,
            value=15
        )

    # Submit button
    submitted = st.form_submit_button("Save Settings")
    if submitted:
        st.success("Settings saved successfully!")
        st.rerun()

# Dashboard settings
st.header("Dashboard Configuration")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Theme")
    theme = st.radio(
        "Select Theme",
        ["Light", "Dark", "Auto"],
        horizontal=True
    )

    st.subheader("Chart Defaults")
    default_chart_type = st.selectbox(
        "Default Chart Type",
        ["Line", "Bar", "Scatter", "Area"]
    )

    chart_animation = st.toggle("Enable Chart Animations", value=True)

with col2:
    st.subheader("Data Display")
    rows_per_page = st.number_input(
        "Rows per Table",
        min_value=5,
        max_value=100,
        value=20
    )

    number_format = st.selectbox(
        "Number Format",
        ["Standard (1,234.56)", "Compact (1.23K)", "Percent (12.34%)"]
    )

    date_format = st.selectbox(
        "Date Format",
        ["YYYY-MM-DD", "MM/DD/YYYY", "DD/MM/YYYY", "Month D, YYYY"]
    )

# Export/Import settings
st.header("Data Management")

tab1, tab2 = st.tabs(["Export", "Import"])

with tab1:
    st.write("Export your settings and data")
    export_format = st.radio(
        "Export Format",
        ["JSON", "CSV", "Excel"],
        horizontal=True
    )

    if st.button("Export Settings"):
        st.info("Export functionality would save settings to a file")

with tab2:
    st.write("Import settings from file")
    uploaded_file = st.file_uploader(
        "Choose a file",
        type=['json', 'csv', 'xlsx']
    )

    if uploaded_file is not None:
        st.success(f"File {uploaded_file.name} uploaded successfully!")
        if st.button("Apply Imported Settings"):
            st.warning("Note: This is a demo. In production, this would apply settings from the file.")

# Reset section
st.header("Reset")
with st.expander("Reset to Defaults"):
    st.warning("This will reset all settings to their default values.")
    if st.button("Reset All Settings", type="secondary"):
        st.error("Reset functionality would be implemented here")
        st.info("Demo: This would reset all settings in a real application")

# Footer
st.markdown("---")
st.caption("Settings are stored locally in your browser")