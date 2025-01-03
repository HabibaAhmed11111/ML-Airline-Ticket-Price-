import joblib
import pandas as pd
import streamlit as st

<<<<<<< HEAD
=======


>>>>>>> d32994ff298d45f0ab0fe9d3aae1ed5ca290e8dc
# Load the model and input features
model = joblib.load("Third_Group.pkl")
inputs = joblib.load("Inputs.pkl")

<<<<<<< HEAD
# Define mappings for categorical features
airline_mapping = {
    "Air Asia": 0,
    "Air India": 1,
    "GoAir": 2,
    "IndiGo": 3,
    "Jet Airways": 4,
    "Multiple carriers": 5,
    "SpiceJet": 6,
    "Vistara": 7
}

source_mapping = {
    "Banglore": 0,
    "Kolkata": 1,
    "Delhi": 2,
    "Chennai": 3,
    "Mumbai": 4
}

destination_mapping = {
    "New Delhi": 0,
    "Banglore": 1,
    "Cochin": 2,
    "Kolkata": 3,
    "Delhi": 4,
    "Hyderabad": 5
}

stops_mapping = {
    "non-stop": 0,
    "1 stop": 1,
    "2 stops": 2,
    "3 stops": 3,
    "4 stops": 4
}

additional_info_mapping = {
    "No info": 0,
    "Business class": 1,
    "Economy class": 2
}

route_mapping = {
    "Direct": 0,
    "Indirect": 1
}

def prediction(Airline, Source, Destination, Route, Additional_Info,
               Journey_Day, Journey_Month, Dep_Hour, Dep_Minute,
               Arrival_Hour, Arrival_Minute, Duration_Minutes, Total_Stops):
    # Encode categorical features
    Airline = airline_mapping.get(Airline, -1)
    Source = source_mapping.get(Source, -1)
    Destination = destination_mapping.get(Destination, -1)
    Route = route_mapping.get(Route, -1)
    Additional_Info = additional_info_mapping.get(Additional_Info, -1)
    Total_Stops = stops_mapping.get(Total_Stops, -1)
    
    # Create DataFrame with encoded values in the correct order
    feature_values = [
        Airline,
        Source,
        Destination,
        Route,
        Additional_Info,
        Journey_Day,
        Journey_Month,
        Dep_Hour,
        Dep_Minute,
        Arrival_Hour,
        Arrival_Minute,
        Duration_Minutes,
        Total_Stops
    ]
    
    # Ensure the feature order matches the training
    df = pd.DataFrame([feature_values], columns=inputs)
    
    result = model.predict(df)[0]
    return result

def main():
    st.title("Flight Fare Prediction App")
    
    # Create two tabs
    tab1, tab2 = st.tabs(["About","Prediction"])
    
    with tab1:
        st.image("plane.jpg") 
        st.header("About the Model")
        st.write("""
            This application uses a machine learning model to predict airline ticket prices based on various parameters such as airline, source, destination, and more.
            
            **Features:**
            - **Airline:** The airline operating the flight.
            - **Source:** The departure city.
            - **Destination:** The arrival city.
            - **Route:** Direct or indirect flight.
            - **Additional Info:** Class of service.
            - **Journey Date:** Day and month of the journey.
            - **Departure and Arrival Times:** Hours and minutes.
            - **Duration:** Flight duration in minutes.
            - **Total Stops:** Number of stops during the journey.
        """)    
    
    with tab2:
    
        st.header("Predict Flight Fare")
        
        Airline = st.selectbox("Airline", list(airline_mapping.keys()))
        Source = st.selectbox("Source", list(source_mapping.keys()))
        Destination = st.selectbox("Destination", list(destination_mapping.keys()))
        Route = st.selectbox("Route", list(route_mapping.keys()))
        Additional_Info = st.selectbox("Additional Info", list(additional_info_mapping.keys()))
        Journey_Day = st.slider("Journey Day", 1, 31, 15)
        Journey_Month = st.slider("Journey Month", 1, 12, 6)
        Dep_Hour = st.slider("Departure Hour", 0, 23, 12)
        Dep_Minute = st.slider("Departure Minute", 0, 59, 30)
        Arrival_Hour = st.slider("Arrival Hour", 0, 23, 15)
        Arrival_Minute = st.slider("Arrival Minute", 0, 59, 45)
        Duration_Minutes = st.slider("Duration Minutes", 0, 2860, 30)
        Total_Stops = st.selectbox("Total Stops", list(stops_mapping.keys()))
        
        if st.button("Predict Fare"):
            result = prediction(
                Airline, Source, Destination, Route, Additional_Info,
                Journey_Day, Journey_Month, Dep_Hour, Dep_Minute,
                Arrival_Hour, Arrival_Minute, Duration_Minutes, Total_Stops
            )
            st.success(f"Estimated Ticket Price: ₹ {result:.2f}")
=======
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

>>>>>>> d32994ff298d45f0ab0fe9d3aae1ed5ca290e8dc
if __name__ == "__main__":
    main()
