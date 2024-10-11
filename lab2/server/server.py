from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn

from lab2.data.PgDbWordsProvider import PgDbWordsProvider
from lab2.words.templates.factory.GangstaTemplateFactory import GangstaTemplateFactory
from lab2.words.templates.factory.PhilosophicalTemplateFactory import RomanticTemplateFactory
from lab2.words.templates.factory.RomanticTemplateFactory import PhilosophicalTemplateFactory

port = 8001

app = FastAPI()

app.mount("/static", StaticFiles(directory="resources/static"), name="static")

templates = Jinja2Templates(directory="resources/templates")

words_provider = PgDbWordsProvider(
    host='localhost',
    port='5432',
    dbname='lab3',
    user='postgres',
    password='admin'
)

gangsta_factory = GangstaTemplateFactory()
romantic_factory = RomanticTemplateFactory()
philosophical_factory = PhilosophicalTemplateFactory()

def to_json(quote):
    return {"quote": quote}

class WordInput(BaseModel):
    word: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/gangsta")
async def get_gangsta_quote():
    word_set = words_provider.generate_word_set()
    quote = gangsta_factory.create_template()(word_set)
    return to_json(quote)

@app.get("/romantic")
async def get_romantic_quote():
    word_set = words_provider.generate_word_set()
    quote = romantic_factory.create_template()(word_set)
    return to_json(quote)

@app.get("/philosophical")
async def get_philosophical_quote():
    word_set = words_provider.generate_word_set()
    quote = philosophical_factory.create_template()(word_set)
    return to_json(quote)

@app.post("/add/noun")
async def add_noun(word_input: WordInput):
    try:
        words_provider.add_noun(word_input.word)
        return {"status": "success", "message": f"Существительное '{word_input.word}' добавлено."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/add/verb")
async def add_verb(word_input: WordInput):
    try:
        words_provider.add_verb(word_input.word)
        return {"status": "success", "message": f"Глагол '{word_input.word}' добавлен."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/add/adjective")
async def add_adjective(word_input: WordInput):
    try:
        words_provider.add_adjective(word_input.word)
        return {"status": "success", "message": f"Прилагательное '{word_input.word}' добавлено."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=port)
