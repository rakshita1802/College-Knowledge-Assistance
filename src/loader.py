from langchain_community.document_loaders import PyPDFLoader

class Loader:
    def load_pdf(self, path):
        return PyPDFLoader(path).load()