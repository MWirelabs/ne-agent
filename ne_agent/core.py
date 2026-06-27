from .lid import LanguageIdentifier
from .retriever import Retriever
from .llm import OllamaLLM

class NEAgent:
    def __init__(self, model: str = "qwen2.5:1.5b"):
        self.lid = LanguageIdentifier()
        self.retriever = Retriever()
        self.llm = OllamaLLM(model=model)

    def load_corpus(self, corpus: dict, n: int = 500):
        self.retriever.build(corpus, n=n)

    def run(self, query: str) -> dict:
        lang, score = self.lid.predict(query)
        docs = self.retriever.retrieve(query, lang, top_k=3)
        answer = self.llm.generate(query, docs)
        return {
            "query": query,
            "detected_lang": lang,
            "lang_score": score,
            "retrieved": docs,
            "answer": answer
        }
