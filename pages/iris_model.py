import streamlit as st
import pandas as pd
from tensorflow.keras import models

sepal_length = st.slider('Panjang Kelopak', min_value=4.0, max_value=6.0, step=0.1)
sepal_width = st.slider('Lebar Kelopak', min_value=2.0, max_value=5.0, step=0.1)
petal_length = st.slider('Panjang Mahkota', min_value=0.0, max_value=3.0, step=0.1)
petal_width = st.slider('Lebar Mahkota', min_value=1.0, max_value=7.0, step=0.1)
button_predict = st.button('Prediksi')

loaded_model = models.load_model('../iris_model.h5')
if button_predict:
    features = {
        'sepal_length': sepal_length,
        'sepal_width': sepal_width,
        'petal_width': petal_width,
        'petal_length': petal_length,
    }
    df_features = pd.DataFrame([features])
    df_result = loaded_model.predict(df_features)
    