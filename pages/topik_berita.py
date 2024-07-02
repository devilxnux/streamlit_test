import streamlit as st
import pickle, re

TOPIK_BERITA_URL='https://dhipo-ku.streamlit.app/topik_berita'

MODELS={
'Random Forrest': 'rf',
'Multinomial NB': 'nb',
'SVM Classification': 'svm',
'SVM + SMOTE': 'svm_smote',
}

def preprocess_text(text):
    new_text = re.sub(r'\W', ' ', text) # buang karakter non alphanumeric
    return new_text

def predict(pipeline, text):
    preprocessed_text = preprocess_text(text)
    predicted_topic = pipeline.predict([preprocessed_text])[0]
    return predicted_topic

pipeline = pickle.load(open('category_pipeline.pkl', 'rb'))
pages = ['Judul', 'Analisis Topik', 'Data Sumber', 'Penyiapan Data', 'Pemodelan', 'Demo']
page = st.query_params.get('page')
def page_0():
    st.subheader('Tugas Kelompok DJP II')
    st.header('Klasifikasi Topik atas Judul Berita')
    st.subheader('Memanfaatkan Teknik NLP')

def page_1():
    st.header('Analisis Topik')
    st.markdown('''
    ## Kategori Analisis Topik
    ![Modelling vs Classification](https://cdn.prod.website-files.com/5fb24a974499e90dae242d98/63317613765082e144c40ff8_Topic%20Modeling%20vs%20Text%20Classification.png)
    
    ## Manfaat
    - Pengelolaan dokumen tidak terstruktur
    - Otomasi pekerjaan kantor
    - Analisa feedback stakeholder
    ''')

def page_2():
    st.header('Data Sumber')
    st.markdown('''
    ## URL
    [Indosum Google Drive](https://drive.google.com/file/d/1OgYbPfXFAv3TbwP1Qcwt_CC9cVWSJaco/view)
    ## Deskripsi
    Dataset Indosum merupakan corpus hasil scrapping berita dari beberapa sumber berita daring (e.g.: CNN Indonésia, Merdeka, dll).



    Referensi:

    Kurniawan, K., & Louvan, S. (2018). IndoSum: A New Benchmark Dataset for Indonesian Text Summarization. In 2018 International Conference on Asian Language Processing (IALP) (pp. 215–220). Bandung, Indonesia: IEEE. https://doi.org/10.1109/IALP.2018.8629109
    ''')

def page_3():
    st.header('Penyiapan Data')
    st.subheader('Eksplorasi')
    "---"
    st.subheader('Pembersihan')
    "---"
    st.subheader('Standardisasi')

def page_4():
    st.header('Pemodelan')
    st.markdown('''
    ## Alur Umum
    Teks &rarr; Vektorisasi &rarr; Training
    
    ## Algoritma Random Forrest
    ## Algoritma SVM
    ## Algoritma Multinomial NB

    ## Class Imbalance &rarr; SMOTE
    
    ''')

def page_5():
    select_model = st.selectbox('Model yang akan dijalankan', MODELS.keys())
    input_text = st.text_area('Judul Berita')
    button_predict = st.button('Klasifikasikan Topik')
    if button_predict:
        if input_text.strip() == '':
            st.warning('Judul berita kosong!')
        predicted_topic = predict(pipeline, input_text)
        st.write(f"Prediksi Topik: {predicted_topic}")


with st.sidebar:
    selected_style = 'style="font-weight: bolder; text-decoration: underline;"'
    for idx, judul in enumerate(pages):
        st.page_link(f"{TOPIK_BERITA_URL}?page={ idx }", label=judul)

page_func = locals().get(f"page_{page}")
if not page_func is None:
    page_func()
else:
    page_0()