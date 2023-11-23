import uvicorn
import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    "*"
]
    # settings.CLIENT_ORIGIN,

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "hello world"}

@app.get("/images")
def images():
    out = []
    for filename in os.listdir("static/images"):
        out.append({
            "name": filename,
            # "name": filename.split(".")[0],
            "path": "/static/images/" + filename
        })
    return out

@app.get("/documents")
def images():
    out = []
    for filename in os.listdir("static/documents"):
        out.append({
            "name": filename,
            # "name": filename.split(".")[0],
            "path": "/static/documents/" + filename
        })
    return out

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5000, workers=2) #, reload=True)