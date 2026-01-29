import ollama
import streamlit as st

st.set_page_config(page_title="Local IA", page_icon="🤖")
st.title("IA assist")

pergunta = st.text_input("faça uma pergunta:")

if st.button("Perguntar"):
    if pergunta:
        with st.spinner("Pensando....."):
            response = ollama.chat(model='phi3', messages=[
                {
                    'role': 'user',
                    'content': pergunta
                }
            ])

            st.subheader("Resposta:")
            st.write(response['message']['content'])
    else:
            st.warning("Por favor, Digite algo")