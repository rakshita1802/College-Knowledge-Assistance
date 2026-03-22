from src.db_manager import DBManager

class Retriever:
    def __init__(self):
        self.db = DBManager()

    def get_docs(self, query):
        return self.db.search(query, k=5)