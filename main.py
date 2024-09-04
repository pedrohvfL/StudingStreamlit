import streamlit as st

col1, col2, col3 = st.columns(3)

st.sidebar.title('Menu')

pageselect = st.sidebar.selectbox('selecione a pagina: ', ['Pagina 1', 'Pagina 2'])

with col1:
    st.header("Gato")
    st.write('meu gtonho')
    st.button('click')


with col2:
    st.header("Cachorro")
    st.write('meu cachorro')

with col3:
    st.header("Coruja")
    st.write('minha corruuujjaa')