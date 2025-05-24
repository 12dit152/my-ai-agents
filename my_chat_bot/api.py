from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
import subprocess
import yaml
import os

router = APIRouter()

TEMPLATE_NAME = "chatbot.html"
MODEL_NAME = "mistral"
INFO_PATH = os.path.join(os.path.dirname(__file__), 'data', 'info.yaml')

@router.get("/chatbot", response_class=HTMLResponse)
def chatbot_page(request: Request):
    return request.app.templates.TemplateResponse(TEMPLATE_NAME, {"request": request, "answer": None, "question": ""})

@router.post("/chatbot", response_class=HTMLResponse)
def chatbot_submit(request: Request, question: str = Form(...)):
    with open(INFO_PATH, 'r', encoding='utf-8') as f:
        info = yaml.safe_load(f)
    info_yaml = yaml.dump(info, allow_unicode=True)
    prompt = (
        "You are a helpful assistant. Answer the user's question using ONLY the YAML information below. "
        "If the answer is not in the info, say you don't know.\n\n"
        f"Personal Info (YAML):\n{info_yaml}\n\nQuestion: {question}\nAnswer:"
    )
    result = subprocess.run(
        ["ollama", "run", MODEL_NAME],
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
    )
    answer = result.stdout.decode("utf-8").strip()
    return request.app.templates.TemplateResponse(TEMPLATE_NAME, {"request": request, "answer": answer, "question": question})
