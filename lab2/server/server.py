from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn
import matplotlib.pyplot as plt

from data.PgDbWordsProvider import PgDbWordsProvider
from words.GangstaTemplateFactory import GangstaTemplateFactory
from words.PhilosophicalTemplateFactory import RomanticTemplateFactory
from words.RomanticTemplateFactory import PhilosophicalTemplateFactory

from data.PgDbWordsProvider import ActivityLogger

port = 8001

app = FastAPI()

app.mount("/static", StaticFiles(directory="server/resources/static"), name="static")

templates = Jinja2Templates(directory="server/resources/templates")
activity_logger = ActivityLogger()

words_provider = PgDbWordsProvider(
    host='localhost',
    port='5430',
    dbname='cytaty',
    user='postgres',
    password='admin',
    activity_logger=activity_logger
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

@app.get("/activity-graph")
async def get_activity_graph():
    if not activity_logger.add_word_times:
        raise HTTPException(status_code=404, detail="Нет данных для построения графика активности")

    plt.plot(range(1, len(activity_logger.add_word_times) + 1), activity_logger.add_word_times, marker='o')
    plt.title('Время выполнения добавления слов')
    plt.xlabel('Номер операции добавления')
    plt.ylabel('Время выполнения (секунды)')
    plt.grid(True)

    graph_path = "activity_graph.png"
    plt.savefig(graph_path)
    plt.close()

    return FileResponse(graph_path, media_type='image/png')

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=port)
