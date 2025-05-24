from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

from text_summarisation.api import router as summarizer_router
from my_chat_bot.api import router as chatbot_router
from sentiment_analysis.api import router as sentiment_router

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, "templates"),
    os.path.join(BASE_DIR, "text_summarisation", "templates"),
    os.path.join(BASE_DIR, "my_chat_bot", "templates"),
    os.path.join(BASE_DIR, "sentiment_analysis", "templates"),
]

# Custom Jinja2Templates to support multiple template dirs
from jinja2 import ChoiceLoader, FileSystemLoader
from starlette.templating import Jinja2Templates as StarletteJinja2Templates

class MultiDirJinja2Templates(StarletteJinja2Templates):
    def __init__(self, directory_list):
        loader = ChoiceLoader([FileSystemLoader(d) for d in directory_list])
        from jinja2 import Environment
        env = Environment(loader=loader, autoescape=True)
        super().__init__(env=env)

app.templates = MultiDirJinja2Templates(TEMPLATE_DIRS)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return app.templates.TemplateResponse("home.html", {"request": request})

# Mount routers for each AI tool
app.include_router(summarizer_router)
app.include_router(chatbot_router)
app.include_router(sentiment_router)
