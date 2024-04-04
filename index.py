from fastapi import FastAPI
import uvicorn
from routes.books import router_books
from routes.schedule import router_schedule

app = FastAPI()
@app.get("/")
def index_read():
    return "서버 가동중입니다."

app.include_router(router_books)
app.include_router(router_schedule)


if __name__ == "__main__":
    uvicorn.run(app, port=8001)