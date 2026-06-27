from ne_lid import NELID

class LanguageIdentifier:
    def __init__(self):
        self.model = NELID()

    def predict(self, text: str) -> tuple[str, float]:
        result = self.model.predict(text)
        return result["lang"], round(result["score"], 4)
