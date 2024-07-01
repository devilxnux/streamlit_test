import pickle
import pandas as pd
import streamlit as st

loaded_model = pickle.load(open('knn_model.pkl', mode='rb'))

st.subheader('Kualitas Udara')
val_aqi = st.slider('Air Quality Index', min_value=0.0, max_value=500.0, step=0.1)
st.subheader('Konsentrasi Zat/Partikulat')
with st.container(border=True):
    val_pm10 = st.slider('PM 10μm', min_value=0.0, max_value=300.0, step=0.1)
    val_pm25 = st.slider('PM 2.5μm', min_value=0.0, max_value=300.0, step=0.1)
    val_no2 = st.slider('NO2', min_value=0.0, max_value=200.0, step=0.1)
    val_so2 = st.slider('SO2', min_value=0.0, max_value=100.0, step=0.1)
    val_o3 = st.slider('Ozon (O3)', min_value=0.0, max_value=300.0, step=0.1)

st.subheader('Cuaca')
with st.container(border=True):
    val_temp = st.slider('Temperatur', min_value=-10.0, max_value=40.0, step=0.1)
    val_humd = st.slider('Kelembaban', min_value=10.0, max_value=100.0, step=0.1)
    val_wind = st.slider('Kecepatan Angin', min_value=0.0, max_value=20.0, step=0.1)

button_predict = st.button('Prediksi')

if button_predict:
    features = {
    'AQI': val_aqi, 
    'PM10': val_pm10, 
    'PM2_5': val_pm25, 
    'NO2': val_no2, 
    'SO2': val_so2, 
    'O3': val_o3, 
    'Temperature': val_temp,
    'Humidity': val_humd, 
    'WindSpeed': val_wind, 
    'RespiratoryCases': 12, 
    'CardiovascularCases': 7,
    'HospitalAdmissions': 6,
    }
    df_features = pd.DataFrame([features])
    
    