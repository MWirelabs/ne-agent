from .lid import LanguageIdentifier
from .retriever import Retriever
from .llm import OllamaLLM
from .tools import Translator, Transcriber

class NEAgent:
    def __init__(self, model: str = "qwen2.5:1.5b"):
        self.lid = LanguageIdentifier()
        self.retriever = Retriever()
        self.llm = OllamaLLM(model=model)
        self.translator = Translator()
        self.transcriber = Transcriber()

    def load_corpus(self, corpus: dict, n: int = 500):
        self.retriever.build(corpus, n=n)

    def route(self, query: str) -> str:
        prompt = f"""You are a tool router. Available tools: search, translate, transcribe
Query: {query}
Reply with only the tool name."""
        tool = self.llm.generate_raw(prompt).strip().lower()
        return tool if tool in ["search", "translate", "transcribe"] else "search"

    def run(self, query: str, audio_path: str = None) -> dict:
        if audio_path:
            answer = self.transcriber.transcribe(audio_path)
            return {
                "query": query or "[audio input]",
                "detected_lang": None,
                "lang_score": None,
                "tool": "transcribe",
                "retrieved": [],
                "answer": answer
            }

        lang, score = self.lid.predict(query)
        tool = self.route(query)

        if tool == "translate":
            clean_query = query.lower().replace("translate this:", "").replace("translate:", "").strip()
            answer = self.translator.translate(clean_query, lang)
            return {
                "query": query,
                "detected_lang": lang,
                "lang_score": score,
                "tool": "translate",
                "retrieved": [],
                "answer": answer
            }

        docs = self.retriever.retrieve(query, lang, top_k=3)
        answer = self.llm.generate(query, docs)
        return {
            "query": query,
            "detected_lang": lang,
            "lang_score": score,
            "tool": "search",
            "retrieved": docs,
            "answer": answer
        }
