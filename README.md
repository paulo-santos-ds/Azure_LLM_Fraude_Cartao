
# Validador de Cartão de Crédito com Azure e Streamlit

## Descrição do Projeto

Este projeto consiste em uma aplicação web que utiliza Azure Computer Vision e Streamlit para verificar e validar informações de cartões de crédito em imagens.

## 📋 Funcionalidades

- Upload de imagens (PNG, JPG, JPEG)
- Armazenamento automático no Azure Blob Storage
- Análise de cartões de crédito usando serviços Azure
- Validação e exibição das informações encontradas

## 🔍 Detalhes da Implementação

O código está estruturado em duas funções principais:

### 1. Configuração da interface
- Cria a interface do usuário com Streamlit
- Gerencia o upload de arquivos
- Processa o envio para o Azure Blob Storage
- Inicia o processo de análise do cartão

### 2. Validação da imagem
Exibe os resultados da análise, incluindo:
- Imagem enviada
- Status da validação (Válido/Inválido)
- Informações do cartão:
 - Nome do titular
 - Banco emissor
 - Data de validade

## 🛠️ Tecnologias Utilizadas

- Python
- Streamlit
- Azure Blob Storage
- Azure Computer Vision

## 💻 Integração com Azure

O projeto utiliza dois serviços principais do Azure:
1. **Blob Storage**: para armazenamento das imagens
2. **Computer Vision**: para análise e extração de informações dos cartões

## 🚀 Como Executar

1. Clone este repositório
2. Configure as credenciais do Azure
3. Instale as dependências listadas acima
4. Execute o aplicativo:
5. Execute o aplicativo Streamlit:
```bash
streamlit run app.py
