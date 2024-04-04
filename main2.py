from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root_index():
    return "두번째 파일 실행중입니다"