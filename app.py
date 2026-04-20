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


col1, col2, col3 = st.columns(3)
col1.metric("Ingresos", "$12K", "8%")
col2.metric("Usuario", "1,204", "12%")
col3.metric("Latencia", "42ms", "-3%")



import streamlit as st
import time

tab1, tab2 = st.tabs(["Chart", "Data"], on_change="rerun")

if tab1.open:
    with st.spinner("Loading Tab 1..."):
        time.sleep(2)
    with tab1:
        st.line_chart({"data": [1, 5, 2, 6]})

if tab2.open:
    with st.spinner("Loading Tab 2..."):
        time.sleep(2)
    with tab2:
        st.dataframe({"col1": [1, 2, 3]})
