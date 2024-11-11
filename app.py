import streamlit as st
from home import home_page  # Import the home_page function from home.py
from data import data_page
from predict import predict_page
from dashboard import dashboard_page
from auth import authenticate

# Set page configuration
st.set_page_config(page_title="Telco Churn Classification", page_icon="📊", layout="centered")

def main():
    authenticate()  # Check user credentials
    if st.session_state.get('authenticated', False):
        st.sidebar.title("Navigator")
        st.sidebar.write("Use this to select between pages")
        page = st.sidebar.selectbox("Navigate", ["Home", "Data", "Predict", "Dashboard"])

        if page == "Home":
            home_page()  
        elif page == "Data":
            data_page()
        elif page == "Predict":
            predict_page()
        elif page == "Dashboard":
            dashboard_page()
    else:
        st.warning("You are not authenticated. Please log in to access the app.")

if __name__ == "__main__":
    main()
