import joblib
import pandas as pd
import streamlit as st



# Load the model and input features
model = joblib.load("Third_Group.pkl")
inputs = joblib.load("Inputs.pkl")

# Function for prediction
# In app.py, modify the prediction function
def prediction(Airline, Source, Destination, Total_Stops, Journey_Day, Journey_Month, Duration_Minutes, Dep_Hour, Dep_Minute):
    df = pd.DataFrame(columns=inputs)
    df.at[0, "Airline"] = Airline
    df.at[0, "Source"] = Source
    df.at[0, "Destination"] = Destination
    df.at[0, "Total_Stops"] = Total_Stops
    df.at[0, "Journey_Day"] = Journey_Day
    df.at[0, "Journey_Month"] = Journey_Month
    df.at[0, "Duration_Minutes"] = Duration_Minutes
    df.at[0, "Dep_Hour"] = Dep_Hour
    df.at[0, "Dep_Minute"] = Dep_Minute
    result = model.predict(df)[0]
    return result
# Main application
def main():
    st.markdown(
        """
        <style>
        body {
            font-family: 'Press Start 2P', cursive;
            color: #FFFFFF;
            background-color: #1E1E1E;
        }
        .stButton>button {
            background-color: #00BFFF;
            color: #FFFFFF;
            font-size: 18px;
            border-radius: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Flight Fare Prediction")

    # Tabs for navigation
    tab1, tab2 = st.tabs(["About the App", "Prediction"])

    with tab1:
        st.image("plane.jpg")
        st.write(
            "Welcome to the Flight Fare Prediction App! This application helps users estimate flight ticket prices "
            "based on various travel factors such as airline, source, destination, and journey details."
        )
        st.write(
            "### About the Developer\n"
            "Passionate about data science and machine learning, my goal is to leverage technology to create solutions that matter."
        )

    with tab2:
        st.header("Flight Fare Prediction")

        # Input fields
        Airline = st.selectbox("Airline", [0, 1, 2])
        Source = st.selectbox("Source", [0, 1, 2])
        Destination = st.selectbox("Destination", [0, 1, 2])
        Total_Stops = st.selectbox("Total Stops", [0, 1, 2])
        Journey_Day = st.slider("Journey Day", min_value=1, max_value=31, step=1)
        Journey_Month = st.slider("Journey Month", min_value=1, max_value=12, step=1)
        Duration_Minutes = st.slider("Duration Minutes", min_value=0, max_value=59, step=1)
        Dep_Hour = st.slider("Departure Hour", min_value=0, max_value=23, step=1)
        Dep_Minute = st.slider("Departure Minute", min_value=0, max_value=59, step=1)

        if st.button("Predict Fare"):
            result = prediction(Airline, Source, Destination, Total_Stops, Journey_Day, Journey_Month, Duration_Minutes, Dep_Hour, Dep_Minute)
            st.success(f"Estimated Ticket Price: {result:.2f}")

if __name__ == "__main__":
    main()
