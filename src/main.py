from fastapi import FastAPI

from Routes.Routes import router

app = FastAPI()

app.include_router(router)



