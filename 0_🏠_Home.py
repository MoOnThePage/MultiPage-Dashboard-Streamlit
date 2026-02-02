import streamlit as st

# Page Configuration
st.set_page_config(
    page_title = "Multi Page Dashboard",
    page_icon = "🔻",
    layout = "wide",
    initial_sidebar_state = "expanded",
)

# Custom CSS for Styling
st.markdown("""
    <style>
        .main-header {
            font-size: 2.5rem;
            color: #1f77b4;
            text-align: center;
            padding: 1rem;
        }
        
        .card {
            background-color: #f0f2f6;
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1rem 0;
        }
    </style>
    """, unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.title("🚀 Dashboard Navigation")
    st.divider()

    # Display current page info
    st.info("Select a page from the sidebar to explore different features.")

    # Add some useful widgets in sidebar
    st.subheader("Quick Settings")
    theme = st.selectbox("Theme", ["dark", "light"])
    st.divider()

    st.subheader("About")
    st.markdown("This is a multipage Streamlit dashboard template.")

# Main content
st.markdown('<div class="main-header">📊 Multi Page Dashboard</div>', unsafe_allow_html=True)

st.write("# Welcome to Streamlit! 👋")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)

# Welcome section
col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.metric(label="Total Users", value="1,234", delta="12%")

with col2:
    with st.container(border=True):
        st.metric(label="Revenue", value="$56,789", delta="8%")

with col3:
    with st.container(border=True):
        st.metric(label="Conversion Rate", value="3.4%", delta="-0.2%")

# Quick links to pages
st.markdown("---")
st.markdown("### 📁 Pages Overview")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown("#### 📊 Dashboard")
        st.markdown("View key metrics and visualizations")
        if st.button("Go to Dashboard", key="btn1"):
            st.switch_page("pages/1_📊_Dashboard.py")

with col2:
    with st.container(border=True):
        st.markdown("#### 📈 Analytics")
        st.markdown("Detailed analysis and insights")
        if st.button("Go to Analytics", key="btn2"):
            st.switch_page("pages/2_📈_Analytics.py")

with col3:
    with st.container(border=True):
        st.markdown("#### ⚙️ Settings")
        st.markdown("Configure your preferences")
        if st.button("Go to Settings", key="btn3"):
            st.switch_page("pages/3_⚙️_Settings.py")

# Footer
st.markdown("---")
st.markdown("*Built with Streamlit* • v1.0.0")

# import streamlit as st
#
#
# def run():
#     st.set_page_config(
#         page_title="Hello",
#         page_icon="👋",
#     )
#
#     st.write("# Welcome to Streamlit! 👋")
#
#     st.sidebar.success("Select a demo above.")
#
#     st.markdown(
#         """
#         Streamlit is an open-source app framework built specifically for
#         Machine Learning and Data Science projects.
#         **👈 Select a demo from the sidebar** to see some examples
#         of what Streamlit can do!
#         ### Want to learn more?
#         - Check out [streamlit.io](https://streamlit.io)
#         - Jump into our [documentation](https://docs.streamlit.io)
#         - Ask a question in our [community
#           forums](https://discuss.streamlit.io)
#         ### See more complex demos
#         - Use a neural net to [analyze the Udacity Self-driving Car Image
#           Dataset](https://github.com/streamlit/demo-self-driving)
#         - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
#     """
#     )
#
#
# if __name__ == "__main__":
#     run()
