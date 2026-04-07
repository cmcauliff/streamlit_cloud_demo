import streamlit as st
import joblib
import pandas as pd

st.title("App Title")

st.write("this is my streamlit app")
st.markdown("### *this is bold text*")

my_name = st. text_input("enter your name")
st.write(my_name)

col1, col2 = st.columns(2)

with col1:
    car_weight = st.slider("Select weight of car", 1000, 5000, value=1500)
    st.write(f"my car weight is {car_weight}")
    
with col2:

    car_displacement = st.slider("Select car engine displacement", 100, 400, value=250)
    st.write(f"my car displacement is {car_displacement }")
    
cars_df = pd.read_csv("data/cars.csv")

model_joblib = joblib.load("car_model.joblib")

model_pipeline = model_joblib['pipeline']

input_dict = {
    "weight": [car_weight],
    "displacement": [car_displacement]
}

input_frame = pd.DataFrame(input_dict)
 
predictions = model_pipeline.predict(input_frame)

st.title(predictions[0])

