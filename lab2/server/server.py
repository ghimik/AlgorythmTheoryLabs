from fastapi import FastAPI
from fastapi.responses import HTMLResponse

import uvicorn

from lab2.data.PgDbWordsProvider import PgDbWordsProvider
from lab2.phase.templates.factory.GangstaTemplateFactory import GangstaTemplateFactory
from lab2.phase.templates.factory.PhilosophicalTemplateFactory import RomanticTemplateFactory
from lab2.phase.templates.factory.RomanticTemplateFactory import PhilosophicalTemplateFactory

port = 8001

app = FastAPI()

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

@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_content = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Генератор Цитат</title>
        <style>
            body { background-color: #2E2E2E; color: white; font-family: Arial, sans-serif; text-align: center; }
            button { margin: 10px; padding: 10px 20px; font-size: 16px; }
            #quote { font-size: 24px; font-style: italic; margin-top: 20px; }
        </style>
    </head>
    <body>
        <h1>Генератор Цитат</h1>
        <button onclick="fetchQuote('gangsta')">Пацанская Цитата</button>
        <button onclick="fetchQuote('romantic')">Романтическая Цитата</button>
        <button onclick="fetchQuote('philosophical')">Философская Цитата</button>
        <div id="quote">Нажмите кнопку, чтобы сгенерировать цитату!</div>

        <script>
            async function fetchQuote(type) {
                const response = await fetch(`/${type}`);
                const data = await response.json();
                document.getElementById('quote').innerText = data.quote;
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

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
