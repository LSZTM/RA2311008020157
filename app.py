from fastapi import FastAPI
from logging_middleware.logger import log
app = FastAPI()
@app.get("/")
async def home():
    await log("backend", "info", "route", "home endpoint hit")
    return {"message": "ok"}
@app.get("/error")
async def error():
    try:
        x = int("abc")  # force error
    except Exception:
        await log("backend", "error", "handler", "invalid integer conversion")
        return {"error": "something went wrong"}
