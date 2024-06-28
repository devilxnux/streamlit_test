import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
df_data = pd.read_csv("sample_data/house_clean.csv")
def main():
    st.header('This is Header')
    st.subheader('This is Subheader')
    st.markdown('''
        # Rendering Markdown
        ## Markdown Subheader
        ### Sub Subheader''')
    st.write('Some Phytagorean Equation:')
    st.latex('c^2 = a^2+b^2')
    AgGrid(df_data, height=160, use_container_width=True)
    st.metric(label='Temperature', value='70 °C', delta='-1.2 °C')
if __name__ == '__main__':
    main()
