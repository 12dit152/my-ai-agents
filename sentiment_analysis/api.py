from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
import subprocess
import os

router = APIRouter()

TEMPLATE_NAME = "sentiment.html"
MODEL_NAME = "mistral"
INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input', 'sample.txt')

@router.get("/sentiment", response_class=HTMLResponse)
def sentiment_page(request: Request):
    return request.app.templates.TemplateResponse(TEMPLATE_NAME, {"request": request, "sentiment": None, "input_text": ""})

@router.post("/sentiment", response_class=HTMLResponse)
def sentiment_submit(request: Request, input_text: str = Form(...)):
    prompt = (
        "You are a sentiment analysis expert. "
        "Analyze the following text and respond with only one word: Positive, Negative, or Neutral. "
        "Text:\n" + input_text + "\nSentiment:"
    )
    result = subprocess.run(
        ["ollama", "run", MODEL_NAME],
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
    )
    sentiment = result.stdout.decode("utf-8").strip()
    return request.app.templates.TemplateResponse(TEMPLATE_NAME, {"request": request, "sentiment": sentiment, "input_text": input_text})

