from fastapi import FastAPI
import uvicorn

from lab2.data.InMemoryWordsProvider import InMemoryWordsProvider
from lab2.phase.templates.factory.GangstaTemplateFactory import GangstaTemplateFactory
from lab2.phase.templates.factory.PhilosophicalTemplateFactory import RomanticTemplateFactory
from lab2.phase.templates.factory.RomanticTemplateFactory import PhilosophicalTemplateFactory

port = 8001

app = FastAPI()

words_provider = InMemoryWordsProvider()
gangsta_factory = GangstaTemplateFactory()
romantic_factory = RomanticTemplateFactory()
philosophical_factory = PhilosophicalTemplateFactory()

def to_json(quote):
    return {"quote": quote}

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

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=port)
