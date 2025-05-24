from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
import subprocess

router = APIRouter()

TEMPLATE_NAME = "summarizer.html"
MODEL_NAME = "mistral"

@router.get("/summarizer", response_class=HTMLResponse)
def summarizer_page(request: Request):
    return request.app.templates.TemplateResponse(TEMPLATE_NAME, {"request": request, "summary": None, "input_text": ""})

@router.post("/summarizer", response_class=HTMLResponse)
def summarizer_submit(request: Request, input_text: str = Form(...)):
    prompt = (
        "You are an expert text summarizer. "
        "Write a concise summary (3-5 sentences) of the following text, focusing only on the most important points. "
        "Do NOT repeat the original text.\n\n"
        f"Text:\n{input_text}\n\nSummary:"
    )
    result = subprocess.run(
        ["ollama", "run", MODEL_NAME],
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
    )
    summary = result.stdout.decode("utf-8").strip()
    return request.app.templates.TemplateResponse(TEMPLATE_NAME, {"request": request, "summary": summary, "input_text": input_text})
