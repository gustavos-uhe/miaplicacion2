import streamlit as st

st.title("Mi Aplicacion Python")

st.sidebar.title("Parametros")

st.write("Elaborado por Gustavo Struve")


with st.container():
    st.write("Subir Lead Nuevo")
    st.button("Click para subir")

st.sidebar.selectbox("Escoge el Modelo de IA", ["GPT-4", "Claude", "Gemini"])
st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)

st.write("Main content area")
