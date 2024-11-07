import streamlit as st 

def configure_interface():
    st.title("Upload de arquivo Azure Documentos falsos")
    upload_file = st.file_uploader("Escolha um Arquivo", type= ["png", "jpg", "jpeg"])

if __name__ == "__main__":
    configure_interface()
