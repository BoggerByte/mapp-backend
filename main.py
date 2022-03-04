__all__ = []

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from fastapi.responses import FileResponse

from app.routers import oauth, users, servers, server, xbox
from app.settings import DATABASE_URL, MODELS_FILE


app = FastAPI()

app.include_router(oauth.router, prefix="/oauth", tags=["auth"])
app.include_router(xbox.router, prefix="/xbox", tags=["xbox"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(server.router, prefix="/server", tags=["server"])
app.include_router(servers.router, prefix="/servers", tags=["servers"])

# app.mount('/app', StaticFiles(directory="C:/dev/2021/app_MAPP/dist/app"), name='app')
# app.mount("/static", StaticFiles(directory="C:/dev/2021/app_MAPP/dist"), name="static")

register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": [MODELS_FILE]},
    generate_schemas=True
)


@app.get("", response_class=FileResponse)
async def index():
    return FileResponse("C:/dev/2021/app_MAPP/dist/index.html")