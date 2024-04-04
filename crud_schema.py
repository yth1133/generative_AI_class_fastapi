from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional

app = FastAPI()

# 사용자 정보를 저장할 딕셔너리 - 타입 형태를 명시해서 가독성 높이기
# 
user_dict: Dict[int, Dict[str, Optional[str]]] = {}

# Pydantic 모델 정의
class User(BaseModel):
    username: str
    email: str

# 사용자 정보 조회
@app.get("/users")
def read_users():
    return user_dict

# 사용자 생성
@app.post("/users/{user_id}")
def create_user(user_id: int, user: User):
    if user_id in user_dict:
        raise HTTPException(status_code=400, detail="이미 유저가 존재합니다.")
    # 사용자 정보 저장
    user_dict[user_id] = user.dict()
    return f"유저 정보가 생성되었습니다. 유저 ID: {user_id}"

# 사용자 정보 업데이트
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id not in user_dict:
        raise HTTPException(status_code=404, detail="유저가 없습니다.")
    # 사용자 정보 업데이트
    user_dict[user_id] = user.dict()
    return f"유저 정보를 업데이트하였습니다. 유저 ID: {user_id}"

# 사용자 삭제
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in user_dict:
        raise HTTPException(status_code=404, detail="유저가 없습니다.")
    # 사용자 정보 삭제
    del user_dict[user_id]
    return f"유저 정보를 삭제하였습니다. 유저 ID: {user_id}"
