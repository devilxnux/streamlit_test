import streamlit as st
import pandas as pd

def main():
    st.header('This is Header')
    st.subheader('This is Subheader')
    st.markdown('''
        # Rendering Markdown
        ## Markdown Subheader
        ### Sub Subheader''')
    st.write('Some Phytagorean Equation:')
    st.latex('c^2 = a^2+b^2')
    df_data = pd.read_csv("sample_data/house_clean.csv")
    st.table(df_data)

if __name__ == '__main__':
    main()
