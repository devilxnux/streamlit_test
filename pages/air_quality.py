import pickle
import streamlit as st

with open('../knn_model.pkl', mode='rb') as file:
    loaded_model = pickle.load(file=file)

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
    val_wind
    