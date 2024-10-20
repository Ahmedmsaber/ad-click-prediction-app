import streamlit as st
import pandas as pd
import joblib  # If you're using joblib to load the model

# Load the trained model
model = joblib.load('ad_click_model.pkl')  # Replace with the path to your model file

st.title("Ad Click Prediction")
st.write("This app predicts whether a user will click on an ad based on user data.")

# Collect user input
user_data = {
    'age': st.slider('Age', 18, 70, 25),
    'gender': st.radio('Gender', ['Male', 'Female','Non-Binary','Unknown']),
    'device_type': st.selectbox('Device Type', ['Mobile', 'Desktop', 'Tablet', 'Other']),
    'ad_position': st.selectbox('Ad Position', ['Top', 'Bottom', 'Sidebar']),
    'browsing_history': st.selectbox('Browsing History', ['Shopping','Education','Entertainment','Social Media','News']),
    'time_of_day': st.selectbox('Time of Day', ['Morning', 'Afternoon', 'Evening', 'Night'])
}


# Convert input to DataFrame
df = pd.DataFrame([user_data])


# Now predict using the model
if st.button('Predict'):
    try:
        # The model should handle encoding for categorical features if it's part of a pipeline
        prediction = model.predict(df)
        if prediction == 1:
            st.success("The user is predicted to click on the ad.")
        else:
            st.warning("The user is predicted not to click on the ad.")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")

