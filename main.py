from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root_index():
    return "Hello World"