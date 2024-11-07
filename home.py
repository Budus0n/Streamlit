import streamlit as st
from PIL import Image

# Define the function for the home page (no need for set_page_config here)
def home_page():
    # Title and Subtitle with Styling
    st.title("Telco Churn Classification Project")
    st.subheader("Using Machine Learning to Predict Customer Churn")
    st.markdown(
        """
        <hr style="border-top: 3px solid #bbb; margin-top: 0px; margin-bottom: 20px;">
        """, unsafe_allow_html=True
    )

    # Main Content Section
    with st.container():
        st.header("Overview")
        st.write(
            "Welcome to the **Telco Churn Classification Project**. This application leverages machine learning "
            "to help identify customers who are likely to churn. By using customer data, businesses can make "
            "data-driven decisions to improve customer retention."
        )

    # Instructions Section with Icons for Visual Interest
    st.header("Instructions")
    st.write("Follow these steps to classify customer churn probability:")
    st.markdown(
        """
        1. 📂 **Upload a CSV file** with customer data.
        2. 🎛️ **Select features** you want to include in the classification.
        3. 🤖 **Choose a machine learning model** from the dropdown menu.
        4. 📊 **Click 'Classify'** to view the prediction results.
        5. 📈 The app provides a performance report with metrics like **F1 score**, **recall**, **precision**, and **accuracy**.
        """
    )

    # Features Section
    st.header("App Features")
    features = [
        ("Data View", "Explore and filter customer data."),
        ("Predict View", "Choose a model and run predictions."),
        ("Dashboard", "View insightful data visualizations."),
    ]
    for title, desc in features:
        st.write(f"### - {title}: {desc}")

    # Benefits Section
    st.header("User Benefits")
    benefits = [
        ("Data-Driven Decisions", "Make informed business decisions using insights from churn predictions."),
        ("Machine Learning Access", "Leverage the power of machine learning models without the complexity."),
    ]
    for title, desc in benefits:
        st.write(f"### - {title}: {desc}")

    # How to Run the App Section
    st.header("How to Run the Application")
    st.code(""" 
    # Activate the virtual environment
    env/scripts/activate

    # Run the App
    streamlit run app.py
    """, language="bash")

    # Video (Optional) - Add a video URL if you have one
    # st.video("URL_or_path_to_video.mp4")

    # Contact Information Section with Divider and Contact Button
    st.markdown(
        """
        <hr style="border-top: 3px solid #bbb; margin-top: 20px; margin-bottom: 20px;">
        """, unsafe_allow_html=True
    )
    st.subheader("Need Help?")
    st.write("If you have any questions, feel free to reach out on [GitHub](https://github.com/Budus0n).")
    st.markdown(
        """
        <style>
            .stButton button {
                background-color: #0073e6;
                color: white;
                border-radius: 5px;
                font-weight: bold;
            }
        </style>
        """, unsafe_allow_html=True
    )
    st.button("Contact Me")
