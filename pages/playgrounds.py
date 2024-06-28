import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
df_data = pd.read_csv("sample_data/house_clean.csv")

st.subheader('Menampilkan Tabel')
st.write('Menampilkan dataframe dengan:')
tab_df, tab_agg = st.tabs(['dataframe', 'ag-grid'])
with tab_df:
    st.dataframe(df_data, height=160, use_container_width=True)
with tab_agg:
    AgGrid(df_data, height=160, use_container_width=True)
st.subheader('Formulir')
with st.container(border=True):
    test_button = st.button('Hello!')
    if test_button:
        st.write('Hello too!')
    text_nama = st.text_input('Siapa nama Anda?')
    if str(text_nama).strip() != "":
        st.write(f"Hai, {text_nama}!")
    check_agree = st.checkbox('Apakah Anda setuju jika olahraga itu penting?')
    if check_agree:
        st.write('Anda setuju!')
    else:
        st.write('Ada TIDAK setuju!')
    radio_nilai = st.radio('Berapa kali Anda olahraga dalam seminggu?', [0, 1, 2, 3, 4, 5], horizontal=True)
    if radio_nilai > 2:
        st.write('Luar biasa! Pertahankan kebiasaan baik Anda!')
    elif radio_nilai > 0:
        st.write('Sudah bagus! Tapi dapat ditingkatkan!')
    else:
        st.write('Mulailah berolahraga hari ini!')
st.subheader('Gambar dalam kolom:')
cols_gambar = st.columns([1, 2, 1])
images = [[
    'https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    'https://images.pexels.com/photos/19640755/pexels-photo-19640755.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=279.825&fit=crop&h=453.05'
    'https://images.pexels.com/photos/1741205/pexels-photo-1741205.jpeg?auto=compress&cs=tinysrgb&w=600'
], [
    'https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg?auto=compress&cs=tinysrgb&w=600'
    'https://images.pexels.com/photos/1805164/pexels-photo-1805164.jpeg?auto=compress&cs=tinysrgb&w=600',
    'https://images.pexels.com/photos/58997/pexels-photo-58997.jpeg?auto=compress&cs=tinysrgb&w=600'
], [
    'https://images.pexels.com/photos/2013665/pexels-photo-2013665.jpeg?auto=compress&cs=tinysrgb&w=600',
    'https://images.pexels.com/photos/3586056/pexels-photo-3586056.jpeg?auto=compress&cs=tinysrgb&w=600',
    'https://images.pexels.com/photos/3432929/pexels-photo-3432929.jpeg?auto=compress&cs=tinysrgb&w=600'
]]
for colnum, col in enumerate(cols_gambar):
    with col:
        for image in images[colnum]:
            st.image(image)
with st.sidebar:
    st.metric(label='Temperature', value='70 °C', delta='-1.2 °C')

st.line_chart(df_data, x='grade', y='price')