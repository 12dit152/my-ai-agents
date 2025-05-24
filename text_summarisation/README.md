# 🧠 Text Summarisation Agent

A simple, local text summarization tool using LLMs (Mistral, Phi-2) via Ollama. Reads `.txt` or `.md` files and generates concise summaries.

---

## 📁 Structure

```
summarize.py           # Main script
input/
  sample.txt           # Input file to summarize
output/
  summary.txt          # Output summary
model/
  local/               # Local model cache (optional)
```

---

## ⚡ Quickstart

1. **Install Python dependencies:**
   ```bash
   pip install -r ../requirements.txt
   ```
2. **Install Ollama and pull a model:**
   ```bash
   ollama pull mistral
   # or
   ollama pull phi
   ```
3. **Add your text to summarize:**
   - Place your file in `input/sample.txt`
4. **Run the summarizer:**
   ```bash
   python summarize.py
   ```
5. **Check the summary:**
   - Output will be in `output/summary.txt`

---

## 🌐 Try in the Web App

You can use the text summarizer from the web interface as well! Just run:

```bash
uvicorn app:app --reload
```

Then open [http://localhost:8000](http://localhost:8000) and select "Text Summarizer" from the home page.

---

## ✨ Extending
- Add CLI with [Typer](https://typer.tiangolo.com/)
- Support for PDF, DOCX, or Markdown
- Chunk long files for summarization
- Multiple summary lengths (short, medium, long)

---

## 👨‍💻 Author
Developed with ❤️ by [Samar Dash](https://github.com/samardash)

