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
    st.navigation([
        st.Page('streamlit_app.py', title='Home', icon=':material/home:'),
        st.Page('playgrounds.py', title='Demo', icon=':material/family_link:'),
    ])
if __name__ == '__main__':
    main()
