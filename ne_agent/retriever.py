import faiss
import numpy as np
from ne_embed import NEEmbed

class Retriever:
    def __init__(self):
        self.model = NEEmbed()
        self.index = None
        self.sentences = []
        self.langs = []

    def build(self, corpus: dict, n: int = 500):
        import random
        random.seed(42)
        for lang, sents in corpus.items():
            cleaned = [s.strip() for s in sents if isinstance(s, str) and len(s.strip()) > 10]
            sampled = random.sample(cleaned, min(n, len(cleaned)))
            self.sentences.extend(sampled)
            self.langs.extend([lang] * len(sampled))
        embeddings = self.model.encode(self.sentences, batch_size=64).astype(np.float32)
        self.index = faiss.IndexFlatIP(embeddings.shape[1])
        self.index.add(embeddings)
        print(f"Index built: {self.index.ntotal} vectors")

    def retrieve(self, query: str, lang: str, top_k: int = 3) -> list:
        qe = self.model.encode([query]).astype(np.float32)
        scores, indices = self.index.search(qe, 50)
        results = []
        for score, idx in zip(scores[0], indices[0]):
            if self.langs[idx] == lang:
                results.append({
                    "text": self.sentences[idx],
                    "lang": self.langs[idx],
                    "score": round(float(score), 4)
                })
            if len(results) == top_k:
                break
        return results
