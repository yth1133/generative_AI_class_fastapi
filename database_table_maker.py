from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

# email 을 기준으로 캐릭터 정보 테이블 만들기

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)  # 이메일은 고유해야 합니다.
    characters = relationship("Character", back_populates="user")  # User와 Character는 1:N 관계입니다.

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))  # User 테이블의 id를 외래 키로 사용합니다.
    user = relationship("User", back_populates="characters")
    stage_clears = relationship("StageClear", back_populates="character")  # Character와 StageClear는 1:N 관계입니다.

class StageClear(Base):
    __tablename__ = 'stage_clears'
    id = Column(Integer, primary_key=True)
    stage_name = Column(String)
    cleared = Column(String)  # 클리어 여부, 예를 들어 "Yes", "No" 또는 클리어 날짜를 저장하기
    character_id = Column(Integer, ForeignKey('characters.id'))  # Character 테이블의 id를 외래 키로 사용합니다.
    character = relationship("Character", back_populates="stage_clears")

# 데이터베이스 엔진 및 세션 생성
SQLALCHEMY_DATABASE_URL = "sqlite:///./game_database.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 데이터 베이스 테이블 생성
Base.metadata.create_all(bind=engine)