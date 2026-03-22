from langchain_community.vectorstores import Chroma
from src.embedder import Embedder

class DBManager:
    def __init__(self, path="vectordb"):
        self.embedder = Embedder()
        self.db = Chroma(
            persist_directory=path,
            embedding_function=self.embedder.get_model()
        )

    def add_docs(self, docs):
        self.db.add_documents(docs)

    def search(self, query, k=5):
        return self.db.similarity_search(query, k=k)