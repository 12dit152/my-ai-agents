# 👨‍💻 Author

Developed with ❤️ by [Samar Dash](https://github.com/samardash)

# 🧠 Local Text Summarization Agent

A simple, fast, and meaningful proof-of-concept for summarizing `.txt` or `.md` files using a local LLM (like Mistral or Phi-2) via [Ollama](https://ollama.com).

---

## 🚀 Features
- Summarize local text files with a single command
- Uses local LLMs (no cloud required)
- Output saved to a file for easy review
- Easily extensible (add PDF, DOCX, CLI, etc.)

---

## 📁 Project Structure

```
text_summarisation/
├── summarize.py           # Main script
├── input/
│   └── sample.txt         # Input file to summarize
├── output/
│   └── summary.txt        # Output summary
└── model/
    └── local/             # Local model cache (optional)
```

---

## 🛠️ Requirements
- Python 3.8+
- [Ollama](https://ollama.com) (for local LLMs)
- See `requirements.txt` for Python dependencies

---

## ⚡ Quickstart

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install Ollama and pull a model:**
   ```bash
   # Download and install Ollama from https://ollama.com
   ollama pull mistral
   # or
   ollama pull phi
   ```

3. **Add your text to summarize:**
   - Place your file in `text_summarisation/input/sample.txt`

4. **Run the summarizer:**
   ```bash
   python text_summarisation/summarize.py
   ```

5. **Check the summary:**
   - Output will be in `text_summarisation/output/summary.txt`

---

## ✨ Extending
- Add CLI with [Typer](https://typer.tiangolo.com/)
- Support for PDF, DOCX, or Markdown
- Chunk long files for summarization
- Multiple summary lengths (short, medium, long)

---

## 📄 License
TBC

---
