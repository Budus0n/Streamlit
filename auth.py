import streamlit as st

def authenticate():
    # Check if the user is already authenticated
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False

    # If the user is not authenticated, ask for username and password
    if not st.session_state.authenticated:
        st.sidebar.header("Login")
        username = st.sidebar.text_input("Username", "")
        password = st.sidebar.text_input("Password", type="password")

        # Predefined credentials (you can replace this with a more secure method)
        correct_username = "phil"
        correct_password = "123456"  # Example password (use a more secure method in production)

        if st.sidebar.button("Login"):
            if username == correct_username and password == correct_password:
                st.session_state.authenticated = True
                st.sidebar.success("Logged in successfully")
            else:
                st.sidebar.error("Incorrect username or password")
    else:
        st.sidebar.success("You are already logged in")
