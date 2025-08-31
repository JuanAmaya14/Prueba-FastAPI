from fastapi import APIRouter, status, Request
from Models.Usuario import Usuario
from .Funciones.Funciones import Funciones as f
from fastapi.responses import HTMLResponse
 
router = APIRouter()

class Routes:
    # HTML Response
    @router.get("/", response_class=HTMLResponse)
    async def Inicio():
        return f.respuesta_html()

    # Json Response
    @router.get("/json", status_code=status.HTTP_200_OK)
    async def RespuestaJson():
        return {"Hola": "mundo"}

    # Rquest Parameters
    @router.get("/suma/{numero1}/{numero2}")
    async def SumaRespuestaJson(numero1: int, numero2: int, request: Request):
        print(numero1, numero2)
        if numero1 != 0 and numero2 != 0:
            return {"Primer numero": numero1, "Segundo numero": numero2, "Resultado suma": f.suma(numero1, numero2)}
        else:
            return f.respuesta_html_badRequest()
    
    # POST
    @router.post("/post")
    async def PostUsuario(usuario: Usuario):
        print(usuario.ToString())
        return usuario