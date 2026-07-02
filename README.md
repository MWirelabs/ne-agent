# NE-Agent
**Open-source AI agent for Northeast Indian languages.**
Built on the NE-Stack by [MWire Labs](https://mwirelabs.com), Shillong.

---

## Quickstart

```bash
pip install ne-agent
```

Install [Ollama](https://ollama.com) and pull a model:

```bash
ollama pull qwen2.5:1.5b
ollama serve
```

Then run:

```bash
ne-agent
```

---

## What is NE-Agent?

NE-Agent is a terminal-based agentic assistant that speaks Northeast India's indigenous languages. It automatically detects the input language, then routes each query to the right tool — retrieval-augmented search, Khasi-English translation, or speech transcription — and generates responses, all running locally with no API keys required.

---

## Powered by NE-Stack

| Component | Role | Model |
|---|---|---|
| NE-LID | Language identification | fastText, 11 languages, 99.09% accuracy |
| Tool Router | Dynamic tool selection | qwen2.5:1.5b (search / translate / transcribe) |
| NE-Embed | Multilingual embeddings | LaBSE fine-tuned, 768-dim |
| FAISS | Vector retrieval | IndexFlatIP, cosine similarity |
| NLLB (Khasi) | Khasi-English translation | Fine-tuned NLLB |
| NE-ASR | Speech transcription | Whisper-medium, 8 languages |
| Ollama | Local LLM | qwen2.5:1.5b (default) |

---

## Supported Languages

Assamese · Khasi · Garo · Mizo · Meitei · Bodo · Kokborok · Nyishi · Nagamese · English

Translation currently supports Khasi. Transcription supports Khasi, Garo, Mizo, Nagamese, Kokborok, Assamese, Chakma, and Wancho.

---

## Bring Your Own Corpus

The default corpus ships 500 monolingual sentences each for Assamese, Khasi, Mizo, and Garo. To use your own documents, replace the txt files in `ne_agent/data/` with your own — one sentence per line.

---

## Requirements

- Python 3.9+
- [Ollama](https://ollama.com) with `qwen2.5:1.5b` pulled
- GPU recommended for translation/transcription tools; search works on CPU

---

## Links

- PyPI: [pypi.org/project/ne-agent](https://pypi.org/project/ne-agent/)
- NE-Embed: [huggingface.co/MWirelabs/ne-embed](https://huggingface.co/MWirelabs/ne-embed)
- NE-LID: [huggingface.co/MWirelabs/ne-lid](https://huggingface.co/MWirelabs/ne-lid)
- NE-ASR: [huggingface.co/MWirelabs/ne-asr](https://huggingface.co/MWirelabs/ne-asr)
- MWire Labs: [mwirelabs.com](https://mwirelabs.com)

---

## License

CC-BY-4.0 — MWire Labs, Shillong, Meghalaya.
