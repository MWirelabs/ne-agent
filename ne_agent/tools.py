import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, WhisperProcessor, WhisperForConditionalGeneration


class Translator:
    def __init__(self, device: str = "cuda"):
        self.device = device
        self.tok = AutoTokenizer.from_pretrained("Badnyal/kha-en-nllb-v0.4")
        self.tok.src_lang = "kha_Latn"
        self.model = AutoModelForSeq2SeqLM.from_pretrained("Badnyal/kha-en-nllb-v0.4").to(device)

    def translate(self, text: str, lang: str) -> str:
        if lang != "khasi":
            return f"[translate not supported for {lang}]"
        inputs = self.tok(text, return_tensors="pt").to(self.device)
        output = self.model.generate(**inputs, max_length=128)
        return self.tok.decode(output[0], skip_special_tokens=True)


class Transcriber:
    def __init__(self, device: str = "cuda"):
        self.device = device
        self.processor = WhisperProcessor.from_pretrained("MWirelabs/ne-asr")
        self.model = WhisperForConditionalGeneration.from_pretrained("MWirelabs/ne-asr").to(device)

    def transcribe(self, audio_path: str) -> str:
        import soundfile as sf
        import librosa

        audio, sr = sf.read(audio_path)
        if sr != 16000:
            audio = librosa.resample(audio, orig_sr=sr, target_sr=16000)
        inputs = self.processor(audio, sampling_rate=16000, return_tensors="pt").to(self.device)
        with torch.no_grad():
            predicted_ids = self.model.generate(
                inputs.input_features, language="welsh", task="transcribe"
            )
        return self.processor.decode(predicted_ids[0], skip_special_tokens=True)
