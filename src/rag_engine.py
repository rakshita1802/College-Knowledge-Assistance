from langchain_community.llms import Ollama
from src.retriever import Retriever

class RAGEngine:
    def __init__(self):
        self.retriever = Retriever()
        self.llm = Ollama(model="phi3")

    def ask(self, query):
        docs = self.retriever.get_docs(query)

        context = "\n\n".join([d.page_content for d in docs])

        prompt = f"""
You are a College Knowledge Assistant.

Rules:
- Answer ONLY from context
- Be short
- If not found, say "Not found in documents"

Context:
{context}

Question: {query}

Answer:
"""

        answer = self.llm.invoke(prompt)

        return answer, docs