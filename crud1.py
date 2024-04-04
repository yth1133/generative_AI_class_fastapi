from fastapi import FastAPI, HTTPException

app = FastAPI()

# 사용자 정보를 저장할 딕셔너리
user_dict = {}

# 사용자 정보 조회
@app.get("/users")
def read_users():
    return user_dict

# 사용자 생성
@app.post("/users/{user_id}")
def create_user(user_id: int, username: str, email: str):
    if user_id in user_dict:
        raise HTTPException(status_code=400, detail="이미 유저가 존재합니다.")
    # 사용자 정보 저장
    user_dict[user_id] = {"username": username, "email": email}
    return {f"{user_dict[user_id]}": "유저 정보가 생성되었습니다. "}

# 사용자 정보 업데이트
@app.put("/users/{user_id}")
def update_user(user_id: int, username: str, email: str):
    if user_id not in user_dict:
        raise HTTPException(status_code=404, detail="유저가 없습니다. ")
    # 사용자 정보 업데이트
    user_dict[user_id] = {"username": username, "email": email}
    return {f"{user_dict[user_id]}": "유저 정보를 업데이트하였습니다. "}

# 사용자 삭제
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in user_dict:
        raise HTTPException(status_code=404, detail="유저가 없습니다. ")
    # 사용자 정보 삭제
    del user_dict[user_id]
    return {f"{user_dict[user_id]}": "유저 정보를 삭제하였습니다. "}