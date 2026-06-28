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

NE-Agent is a terminal-based agentic assistant that speaks Northeast India's indigenous languages. It automatically detects the input language, retrieves relevant context from a multilingual corpus, and generates responses — all running locally with no API keys required.

---

## Powered by NE-Stack

| Component | Role | Model |
|---|---|---|
| NE-LID | Language identification | fastText, 11 languages, 99.09% accuracy |
| NE-Embed | Multilingual embeddings | LaBSE fine-tuned, 768-dim |
| FAISS | Vector retrieval | IndexFlatIP, cosine similarity |
| Ollama | Local LLM | qwen2.5:1.5b (default) |

---

## Supported Languages

Assamese · Khasi · Garo · Mizo · Meitei · Bodo · Kokborok · Nyishi · Nagamese · English

---

## Bring Your Own Corpus

The default corpus ships 500 monolingual sentences each for Assamese, Khasi, Mizo, and Garo. To use your own documents, replace the txt files in `ne_agent/data/` with your own — one sentence per line.

---

## Requirements

- Python 3.9+
- [Ollama](https://ollama.com) with `qwen2.5:1.5b` pulled
- 4GB RAM minimum for CPU inference

---

## Links

- PyPI: [pypi.org/project/ne-agent](https://pypi.org/project/ne-agent/)
- NE-Embed: [huggingface.co/MWirelabs/ne-embed](https://huggingface.co/MWirelabs/ne-embed)
- NE-LID: [huggingface.co/MWirelabs/ne-lid](https://huggingface.co/MWirelabs/ne-lid)
- MWire Labs: [mwirelabs.com](https://mwirelabs.com)

---

## License

CC-BY-4.0 — MWire Labs, Shillong, Meghalaya.
