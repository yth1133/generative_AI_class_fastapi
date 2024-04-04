# main.py
from fastapi import FastAPI, APIRouter

app = FastAPI()

# 한페이지에 라우터 설정 같이 넣어보기

# 사용자 관련 라우터
router_users = APIRouter(prefix="/users")

@router_users.get("/")
def read_users():
    return {"message": "사용자 목록"}

@router_users.post("/")
def create_user():
    return {"message": "사용자 생성"}

# 책 관련 라우터
router_books = APIRouter(prefix="/books", tags=["books"])

@router_books.get("/")
def read_books():
    return {"message": "책 목록"}

@router_books.post("/")
def create_book():
    return {"message": "책 생성"}

# 이벤트 관련 라우터
router_events = APIRouter(prefix="/events", tags=["events"])

@router_events.get("/")
def read_events():
    return {"message": "이벤트 목록"}

@router_events.post("/")
def create_event():
    return {"message": "이벤트 생성"}

# 앱에 라우터 연결
app.include_router(router_users)
app.include_router(router_books)
app.include_router(router_events)
