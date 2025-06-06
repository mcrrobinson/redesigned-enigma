from typing import List
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from uvicorn import run
from env import FILE_DIR, TEMPLATES_DIR, STATIC_DIR
import os


class Metadata(BaseModel):
    delimiter: str
    ignored_rows: List[int]
    column_types: List[str]


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/api/files", response_class=JSONResponse)
async def files(request: Request):
    files = os.listdir(FILE_DIR)
    return files


# This will be a UUID later.
@app.post("/api/{file}/metadata/")
async def metadata(request: Request, file: str, metadata: Metadata) -> dict:
    print(file, metadata.column_types, metadata.delimiter, metadata.ignored_rows)
    return {"message": "success"}


@app.get("/api/{file}/content/{buffer}")
async def metadata(request: Request, file: str, buffer: int) -> str:
    absolute_path = os.path.join(FILE_DIR, file)
    if not os.path.isfile(absolute_path):
        return {"message": "file doens't exist"}

    remote_file = open(absolute_path, "r")
    remote_file.seek(buffer)
    content = remote_file.read(10000)
    remote_file.close()

    return content


@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/{file}/", response_class=HTMLResponse)
async def file(request: Request, file: str) -> HTMLResponse:
    return templates.TemplateResponse("file.html", {"request": request, "file": file})


if __name__ == "__main__":
    if not os.path.isdir(FILE_DIR):
        os.mkdir(FILE_DIR)

    if not os.path.isdir(TEMPLATES_DIR):
        print("Templates folder doesn't exist.")
        exit()

    if not os.path.isdir(STATIC_DIR):
        print("The static folder doesn't exist.")
        exit()

    run("main:app", host="127.0.0.1", port=8000, reload=True, log_level="info")
