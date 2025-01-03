import joblib
import pandas as pd
import streamlit as st

# Load the model and input features
model = joblib.load("Third_Group.pkl")
inputs = joblib.load("Inputs.pkl")

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
if __name__ == "__main__":
    main()
