import streamlit as st
import pickle, re

def preprocess_text(text):
    new_text = re.sub(r'\W', ' ', text) # buang karakter non alphanumeric
    return new_text

def predict(pipeline, text):
    preprocessed_text = preprocess_text(text)
    predicted_topic = pipeline.predict([preprocessed_text])[0]
    return predicted_topic

pipeline = pickle.load(open('models/category_pipeline.pkl', 'rb'))

input_text = st.text_area('Judul Berita')
button_predict = st.button('Klasifikasikan Topik')
if button_predict:
    if input_text.strip() == '':
        st.warning('Judul berita kosong!')
    predicted_topic = predict(pipeline, input_text)
    st.write(f"Prediksi Topik: {predicted_topic}")