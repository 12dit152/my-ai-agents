# 👨‍💻 Author

Developed with ❤️ by [Samar Dash](https://github.com/12dit152)

# 🧩 Project Overview

This repository contains multiple AI-powered tools:

- **text_summarisation/**: A local text summarisation agent using LLMs (Mistral, Phi-2) via Ollama. Reads `.txt` or `.md` files and generates concise summaries. See `text_summarisation/README.md` for details.
- **my_chat_bot/**: A retrieval-augmented chatbot that uses your personal info from `info.yaml` to answer questions contextually. See `my_chat_bot/README.md` for details.
- **sentiment_analysis/**: Analyze the sentiment (positive/negative/neutral) of a text file or pasted text using a local LLM. See `sentiment_analysis/README.md` for details.

---

> **Note:**
> To use these tools with local LLMs, you should first learn about [Ollama](https://ollama.com), which makes it easy to run large language models on your own machine.
>
> - **Ollama Documentation:** https://ollama.com/
> - **Quick Start:**
>   1. Download and install Ollama from their website.
>   2. Pull a model (e.g., `mistral` or `phi`):
>      ```bash
>      ollama pull mistral
>      # or
>      ollama pull phi
>      ```
>   3. Run a model interactively:
>      ```bash
>      ollama run mistral
>      ```
>   4. Use the provided Python scripts or web interface to interact with the model for summarisation, chat, or sentiment analysis.

---

## 🌐 Try All Tools in a Web Page

You can try all AI tools in a single web interface. To launch the web app locally, run:

```bash
uvicorn app:app --reload
```

Then open [http://localhost:8000](http://localhost:8000) in your browser. Use the home page to access each tool. Input and output remain as before, but now everything is available in one place!

---

## 📄 License
TBC

---
