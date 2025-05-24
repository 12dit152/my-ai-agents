# 📊 Sentiment Analysis Agent

Analyze the sentiment (positive/negative/neutral) of a text file or pasted text using a local LLM (Mistral, Phi-2) via Ollama.

---

## 📁 Structure
```
sentiment_analysis/
  api.py                # FastAPI router for web interface
  templates/
    sentiment.html      # Web UI for sentiment analysis
  input/
    sample.txt          # Example input file (optional)
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
3. **Run the web app:**
   ```bash
   uvicorn app:app --reload
   ```
4. **Open your browser:**
   - Go to [http://localhost:8000](http://localhost:8000) and select "Sentiment Analysis" from the home page.

---

## 👨‍💻 Author
Developed with ❤️ by [Samar Dash](https://github.com/12dit152)

