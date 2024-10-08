from typing import Union

from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles
import schema
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return {"Name": "Yvan"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}