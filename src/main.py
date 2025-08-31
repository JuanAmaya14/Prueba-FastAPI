#.venv\Scripts\Activate.ps1
#fastapi dev main.py

from typing import Union

from fastapi import FastAPI, status, Request

from fastapi.responses import HTMLResponse

app = FastAPI()

# HTML Response
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return __respuesta_html()

# Json Response
@app.get("/json", status_code=status.HTTP_200_OK)
async def read_root():
    return {"Hola": "mundo"}

# Rquest Parameters
@app.get("/suma/{numero1}/{numero2}")
async def read_root(numero1: int, numero2: int, request: Request):
    print(numero1, numero2)
    if numero1 != 0 and numero2 != 0:
        return {"Primer numero": numero1, "Segundo numero": numero2, "Resultado suma": __suma(numero1, numero2)}
    else:
        return __respuesta_html_badRequest()
    
# POST
@app.post("/post/")
async def create_item(item):
    return item


# ------ FUNCIONES PRIVADAS ------
def __suma(numero1 , numero2):
    return numero1 + numero2

def __respuesta_html():
    html_content = """
    <html>
        <head>
            <title>FastAPI</title>
        </head>
        <body>
            <h1>Ola de mar</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

def __respuesta_html_badRequest():
    html_content = """
    <html>
        <head>
            <title>FastAPI</title>
        </head>
        <body>
            <h1>Error 400: Ningun numero debe ser 0</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=400)

