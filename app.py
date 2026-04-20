import streamlit as st

st.title("Mi Aplicacion Python")

st.sidebar.title("Parametros")

st.write("Elaborado por Gustavo Struve")


with st.container():
    st.write("Subir Lead Nuevo")
    st.button("Click para subir")
