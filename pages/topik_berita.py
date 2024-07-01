import streamlit as st
import pickle, re

def preprocess_text(text):
    new_text = re.sub(r'\W', ' ', text) # buang karakter non alphanumeric
    return new_text

def predict(pipeline, text):
    preprocessed_text = preprocess_text(text)
    predicted_topic = pipeline.predict([preprocessed_text])[0]
    return predicted_topic

pipeline = pickle.load(open('category_pipeline.pkl', 'rb'))
page = st.query_params['page']
def page_1():
    st.subheader('Tugas Kelompok DJP II')
    st.header('Klasifikasi Topik atas Judul Berita')
    st.subheader('Memanfaatkan Teknik NLP')

def page_2():
    st.header('Analisis Topik')
    st.markdown('''
    ## Analisis Topik
    ![Modelling vs Classification](https://cdn.prod.website-files.com/5fb24a974499e90dae242d98/63317613765082e144c40ff8_Topic%20Modeling%20vs%20Text%20Classification.png)
    
    ## Manfaat
    - Pengelolaan dokumen tidak terstruktur
    - Otomasi pekerjaan kantor
    - Analisa feedback stakeholder
    ''')

def page_6():
    input_text = st.text_area('Judul Berita')
    button_predict = st.button('Klasifikasikan Topik')
    if button_predict:
        if input_text.strip() == '':
            st.warning('Judul berita kosong!')
        predicted_topic = predict(pipeline, input_text)
        st.write(f"Prediksi Topik: {predicted_topic}")

with st.sidebar:
    selected_style = 'style="font-weight: bolder; text-decoration: underline;"'
    st.html(f"<a {selected_style if page == '1' else ''} href=\"?page=1\">Judul</a>")
    st.html(f"<a {selected_style if page == '2' else ''} href=\"?page=2\">Analisis Topik</a>")
    st.html(f"<a {selected_style if page == '3' else ''} href=\"?page=3\">Data Sumber</a>")
    st.html(f"<a {selected_style if page == '4' else ''} href=\"?page=4\">Eksplorasi Data</a>")
    st.html(f"<a {selected_style if page == '5' else ''} href=\"?page=5\">Pemodelan</a>")
    st.html(f"<a {selected_style if page == '6' else ''} href=\"?page=6\">Demo</a>")

if page == '2':
    page_2()
else:
    page_1()