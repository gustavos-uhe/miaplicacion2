import streamlit as st

st.title("Mi Aplicacion Python")

st.sidebar.title("Parametros")

st.write("Elaborado por Gustavo Struve")


with st.container():
    st.write("Text inside the container")
    st.button("A button inside the container")
