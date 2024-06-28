import streamlit as st

def main():
    st.header('This is Header')
    st.subheader('This is Subheader')
    st.markdown('''
        # Rendering Markdown
        ## Markdown Subheader
        ### Sub Subheader''')
    st.write('Some Phytagorean Equation:')
    st.latex('c^2 = a^2+b^2')

if __name__ == '__main__':
    main()
