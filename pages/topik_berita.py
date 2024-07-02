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

def switch_page_cb(number):
    def inner_switch_page():
        page_number = number
        st.query_params.page = page_number
    return inner_switch_page


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
    st.subheader('Alur Umum')
    st.markdown('Teks &rarr; Vektorisasi &rarr; Training')
    st.write('Algoritma vektorisasi yang digunakan: Tf-Idf')
    st.subheader('Algoritma Random Forrest')
    st.code('''
     cat_pipe_rf = Pipeline([
        ('vectorizer', TfidfVectorizer()),
        ('clf', RandomForestClassifier())
    ])

    cat_pipe_rf.fit(cat_x_train, cat_y_train)
    print(classification_report(cat_y_test, cat_pipe_rf.predict(cat_x_test)))

    Hasil:

                  precision    recall  f1-score   support
     hiburan       1.00      1.00      1.00      1803
   inspirasi       1.00      1.00      1.00       130
    olahraga       1.00      1.00      1.00      4768
     showbiz       1.00      1.00      1.00      2578
 tajuk utama       1.00      1.00      1.00      7192
   teknologi       1.00      1.00      1.00      2303

    accuracy                           1.00     18774
   macro avg       1.00      1.00      1.00     18774
weighted avg       1.00      1.00      1.00     18774
    ''')
    st.subheader('Algoritma Multinomial NB')
    st.code('''
    cat_pipe_nb = Pipeline([
        ('vectorizer', TfidfVectorizer()),
        ('clf', MultinomialNB())
    ])
    cat_pipe_nb.fit(cat_x_train, cat_y_train)
    print(classification_report(cat_y_test, cat_pipe_nb.predict(cat_x_test)))

    Hasil:
              precision    recall  f1-score   support

     hiburan       0.92      0.65      0.76      1803
   inspirasi       0.00      0.00      0.00       130
    olahraga       0.99      0.98      0.99      4768
     showbiz       0.91      0.94      0.92      2578
 tajuk utama       0.90      0.98      0.94      7192
   teknologi       0.96      0.94      0.95      2303

    accuracy                           0.93     18774
   macro avg       0.78      0.75      0.76     18774
weighted avg       0.93      0.93      0.93     18774
    ''')
    st.subheader('Algoritma SVM Classification')
    st.code('''
    cat_pipe_svm = Pipeline([
        ('vectorizer', TfidfVectorizer()),
        ('clf', LinearSVC(dual=True))
    ])

    cat_pipe_svm.fit(cat_x_train, cat_y_train)
    print(classification_report(cat_y_dev, cat_pipe.predict(cat_x_dev)))


    Hasil:

              precision    recall  f1-score   support

     hiburan       1.00      1.00      1.00       347
   inspirasi       1.00      1.00      1.00        21
    olahraga       1.00      1.00      1.00       928
     showbiz       1.00      1.00      1.00       495
 tajuk utama       1.00      1.00      1.00      1445
   teknologi       1.00      1.00      1.00       507

    accuracy                           1.00      3743
   macro avg       1.00      1.00      1.00      3743
weighted avg       1.00      1.00      1.00      3743

    ''')

def page_5():
    select_model = st.selectbox('Model yang akan dijalankan', MODELS.keys())
    input_text = st.text_area('Judul Berita')
    button_predict = st.button('Klasifikasikan Topik')
    if button_predict:
        if input_text.strip() == '':
            st.warning('Judul berita kosong!')
            return
        pipeline = pickle.load(open(f"category_pipeline_{MODELS.get(select_model)}.pkl", 'rb'))
        predicted_topic = predict(pipeline, input_text)
        st.write(f"Judul Berita: {input_text}")
        st.write(f"Prediksi Topik:")
        st.success(predicted_topic)


with st.sidebar:
    for idx, judul in enumerate(pages):
        st.button(judul, on_click=switch_page_cb(idx), use_container_width=True)

page_func = locals().get(f"page_{page}")
if not page_func is None:
    page_func()
else:
    page_0()