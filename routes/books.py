from fastapi import APIRouter
router_books = APIRouter(prefix="/books")

@router_books.get("/")
async def read_books():
    return "책 목록"

@router_books.post("/")
async def create_book():
    return "책 생성"