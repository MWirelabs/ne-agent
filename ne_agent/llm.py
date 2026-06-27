import requests

class OllamaLLM:
    def __init__(self, model: str = "qwen2.5:1.5b", host: str = "http://127.0.0.1:11434"):
        self.model = model
        self.host = host

    def generate(self, query: str, context_docs: list) -> str:
        context = "\n".join([f"[{d['lang']}] {d['text']}" for d in context_docs])
        prompt = f"""You are NE-Agent, an AI assistant for Northeast Indian languages.
Use the following retrieved context to answer the query.

Context:
{context}

Query: {query}

Answer:"""
        response = requests.post(f"{self.host}/api/generate", json={
            "model": self.model,
            "prompt": prompt,
            "stream": False
        })
        return response.json()["response"]
