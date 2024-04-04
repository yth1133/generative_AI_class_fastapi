# 수업을 위한 구조. 실제에서는 배치를 바꾸세요 
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
# 1. 데이터 베이스 모델 스키마 정의
class User(Base):
    __tablename__ = 'users'  # 이 클래스에 해당하는 테이블 이름을 'users'로 지정합니다.
    id = Column(Integer, primary_key=True)  # 사용자의 ID. 주 키로 설정하여 고유한 값이 되게 합니다.
    name = Column(String)  # 사용자의 이름을 저장하는 필드.
    email = Column(String)  # 사용자의 이메일을 저장하는 필드.

# 2. 데이터베이스 엔진 및 세션 생성
SQLALCHEMY_DATABASE_URL = "sqlite:///./fastapi_database.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. 데이터 베이스 테이블 생성
Base.metadata.create_all(bind=engine)

########## -------------------------------------------------------------- ##########

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

app = FastAPI()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db  # 요청 처리 동안 데이터베이스 세션
    finally:
        db.close()  # 요청 처리가 끝나면 데이터베이스 세션을 닫기

# 1. 회원가입 구현
@app.post("/users/")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    return {"name": name, "email": email}

# 2. 전체 회원 조회 구현
@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

# 3. 회원 데이터 수정
@app.put("/users/{user_id}")
def update_user(user_id: int, name: str, email: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.name = name
    db_user.email = email
    db.commit()
    db.refresh(db_user)
    return {"id": user_id, "name": name, "email": email}

# 4. 회원 데이터 삭제
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}
