# NE-Agent

**First open-source AI agent for Northeast Indian languages.**

Built on the NE-Stack by [MWire Labs](https://mwirelabs.com), Shillong.

---

## What is NE-Agent?

NE-Agent is a terminal-based agentic assistant that speaks Northeast India's indigenous languages. It automatically detects the input language, retrieves relevant context from a multilingual corpus, and generates responses — all running locally with no API keys required.

---

## Powered by NE-Stack

| Component | Role | Model |
|---|---|---|
| NE-LID | Language identification | fastText, 11 languages, 99.09% accuracy |
| NE-Embed | Multilingual embeddings | LaBSE fine-tuned, 768-dim |
| FAISS | Vector retrieval | IndexFlatIP |
| Ollama | Local LLM | qwen2.5:1.5b (default) |

---

## Supported Languages

Assamese · Khasi · Garo · Mizo · Meitei · Bodo · Kokborok · Nyishi · Nagamese · English

---

## Quickstart

```bash
pip install ne-agent
```

Add your corpus to `data/` and run:

```bash
python run.py
```

Type in any Northeast Indian language. Type `exit` or `:q` to quit.

---

## License

CC-BY-4.0 — MWire Labs, Shillong, Meghalaya.
