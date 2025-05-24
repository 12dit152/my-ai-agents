# 🗨️ My Chat Bot (RAG)

A retrieval-augmented chatbot that answers questions based on your personal info stored in `data/info.yaml` (YAML format).

---

## 📁 Structure
```
my_chat_bot/
  chat.py          # Main chatbot script
  data/
    info.yaml      # Your personal/contextual information (YAML)
```

---

## 🚀 Features
- Answers questions using only the info in `info.yaml`
- Local, private, and fast
- Extensible for more advanced RAG workflows

---

## ⚡ Quickstart
1. **Add your personal info:**
   - Edit `my_chat_bot/data/info.yaml` with facts, preferences, or any context you want the chatbot to use (in YAML format).
2. **Run the chatbot:**
   ```bash
   python my_chat_bot/chat.py
   ```
3. **Ask questions:**
   - The bot will answer using only your info. If it doesn't know, it will say so.

---

## 🌐 Try in the Web App

You can use the chatbot from the web interface as well! Just run:

```bash
uvicorn app:app --reload
```

Then open [http://localhost:8000](http://localhost:8000) and select "My Chat Bot" from the home page.

---

## 🛠️ Implementation
- Uses a local LLM (via Ollama) to generate answers.
- Loads your info from `data/info.yaml` and restricts answers to that context.
- Simple terminal interface for chatting.

---
# 👨‍💻 Author

Developed with ❤️ by [Samar Dash](https://github.com/samardash)
