from fastapi.responses import HTMLResponse

class Funciones:
    
    @staticmethod
    def suma(numero1 , numero2):
        return numero1 + numero2

    @staticmethod
    def respuesta_html():
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

    @staticmethod
    def respuesta_html_badRequest():
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