import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
df_data = pd.read_csv("sample_data/house_clean.csv")
def main():
    st.header('Halaman Streamlit Dhipo Alam')
    st.subheader('This is Subheader')
    st.markdown('''
        # Rendering Markdown
        ## Markdown Subheader
        ### Sub Subheader''')
    st.write('Some Phytagorean Equation:')
    st.latex('c^2 = a^2+b^2')
    st.write('Menampilkan dataframe dengan:')
    tab_df, tab_agg = st.tabs(['dataframe', 'ag-grid'])
    with tab_df:
        st.dataframe(df_data, height=160, use_container_width=True)
    with tab_agg:
        AgGrid(df_data, height=160, use_container_width=True)
    st.metric(label='Temperature', value='70 °C', delta='-1.2 °C')
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
    radio_nilai = st.radio('Berapa kali Anda olahraga dalam seminggu?', [1, 2, 3, 4, 5])
    if radio_nilai > 2:
        st.write('Luar biasa! Pertahankan kebiasaan baik Anda!')
    elif radio_nilai > 0:
        st.write('Sudah bagus! Tapi dapat ditingkatkan!')
    else:
        st.write('Mulailah berolahraga hari ini!')
if __name__ == '__main__':
    main()
