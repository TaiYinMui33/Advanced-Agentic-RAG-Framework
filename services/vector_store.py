from langchain.vectorstores import Qdrant
from langchain.embeddings import HuggingFaceEmbeddings
from qdrant_client import QdrantClient
from core.config import settings

class VectorStoreManager:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-large-en-v1.5")
        self.client = QdrantClient(host=settings.QDRANT_HOST, port=settings.QDRANT_PORT)
        
    def get_retriever(self, collection_name: str = "enterprise_docs"):
        return Qdrant(
            client=self.client, 
            collection_name=collection_name, 
            embeddings=self.embeddings
        ).as_retriever(search_kwargs={"k": 5})
