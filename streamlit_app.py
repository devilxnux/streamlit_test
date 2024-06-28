import streamlit as st
from st_aggrid import AgGrid
st.set_page_config(page_title='Home', page_icon=':material/home:')

def main():
    st.header('Halaman Streamlit Dhipo Alam')
    st.subheader('This is Subheader')
    st.markdown('''
        # Rendering Markdown
        ## Markdown Subheader
        ### Sub Subheader''')
    st.write('Some Phytagorean Equation:')
    st.latex('c^2 = a^2+b^2')
if __name__ == '__main__':
    main()
