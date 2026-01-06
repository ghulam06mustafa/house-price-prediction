import streamlit as st
import joblib
import numpy as np


model=joblib.load('house.pkl')

st.title("House Proce Prediction")

st.divider()

numberofBedrooms=st.number_input("number of bedrooms", min_value=0, value=0)
numberofbathrooms=st.number_input("number of bathrooms", min_value=0, value=0)
livingArea=st.number_input("living area", min_value=0, value=2000)
conditionofHouse=st.number_input("condition of the house", min_value=0, value=3)
numberofSchools=st.number_input("Number of schools nearby", min_value=0, value=0)

# 'number of bedrooms', 'number of bathrooms', 'living area',
#        'condition of the house', 'Number of schools nearby'

st.divider()
x=[[numberofBedrooms,numberofbathrooms,livingArea,conditionofHouse,numberofSchools]]

predictionButton=st.button("Predict")

if predictionButton:
    # asd
    x_array=np.array(x)
    prediction=model.predict(x_array)[0]
    st.write(f"House Price is {prediction}")
else:
    # 
    st.write(f"Please use predict button ")
