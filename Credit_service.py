from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import documentAnalysisClient
from azure.ai.documentintelligence.models import AnalyzeResultRequest
from utils.config import config

def analyze_credit_card(card_url):
    
    credential = AzureKeyCredential(Config.KEY)

    document_client = DocumentIntelligenceClient(Config.ENDPOINT, credential)

    card_info = document_client.begin_analyze_document(
    "prebuilt-creditCard", AnalyzeDocumentRequest(url_source=card_url)
)
result = card_info.result()

for document in result.documents:
    fields = document.get('fields', ())
    return {
        "card_name": fields.get("CardHolderName", ()).get('content'),
        "card_number": fields.get("CardNumber", ()).get('content'),
        "expiry_date": fields.get("ExpirationDate", ()).get('content'),
        "bank_name": fields.get("IssuingBank", ()).get('content'),
    }





