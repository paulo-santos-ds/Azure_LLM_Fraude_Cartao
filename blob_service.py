import os 
from azure.storage.blob import BlobServiceClient
import streamlit as st
from utils.config import config

def upload_blob(file, file_name):
    try:
        # Cria um cliente para o serviço de blob storage do Azure usando a string de conexão
        blob_service_client = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONNECTION_STRING)

        # Obtém um cliente para o blob específico dentro do container
        blob_client = blob_service_client.get_blob_client(container=Config.CONTAINER_NAME, blob=file_name)

        # Envia o arquivo para o blob, sobrescrevendo se já existir
        blob_client.upload_blob(file, overwrite=True)

        # Retorna a URL do blob
        return blob_client.url
    except Exception as ex:
        # Exibe uma mensagem de erro no Streamlit
        st.error(f"Erro ao enviar o arquivo para o Azure Blob Storage: {ex}")
        return None