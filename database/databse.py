# 수업을 위한 구조. 실제에서는 배치를 바꾸세요 
from sqlalchemy import Column, Integer, String, create_engine, inspect
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
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. 데이터 베이스 테이블 생성
Base.metadata.create_all(bind=engine)
