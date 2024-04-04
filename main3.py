from fastapi import FastAPI
import uvicorn

app = FastAPI()

# 루트 엔드포인트
@app.get("/")
def root_index():
    return "세번째 파일 실행중입니다"

# 날씨 정보 엔드포인트
@app.get("/weather")
def get_weather(city: str = "서울"):
    return {"도시": city, "온도": "25°C", "날씨": "맑음"}

# 책 정보 엔드포인트
@app.get("/books")
def get_books():
    return {"책 목록": ["인생 언리얼 교과서", "Hey, 파이썬! 생성형 AI 활용 앱 만들어 줘"]}

# 사용자 정보 엔드포인트
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": "홍길동", "age": 30}


if __name__ == "__main__":
    uvicorn.run(app, port=8002)
