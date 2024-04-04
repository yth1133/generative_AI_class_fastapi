from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

# 학생 테이블 모델
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    subjects = relationship("Subject", back_populates="student")

# 과목 테이블 모델
class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    name = Column(String)
    score = Column(Integer)
    student = relationship("Student", back_populates="subjects")


SQLALCHEMY_DATABASE_URL = "sqlite:///./example_database.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


# 앞서 정의한 모델과 세션 설정 코드 이후에 이어서 작성합니다.

# 새 세션 생성
session = SessionLocal()

# 학생 데이터 추가
student1 = Student(name="김철수", email="chulsoo@email.com")
session.add(student1)

student2 = Student(name="박영희", email="younghee@email.com")
session.add(student2)

# 데이터베이스에 커밋하여 학생 데이터 저장
session.commit()

# 과목 데이터 추가
# 학생 ID는 앞서 추가한 학생 객체의 id 속성을 참조하여 설정합니다.
subject1 = Subject(name="수학", score=95, student_id=student1.id)
session.add(subject1)

subject2 = Subject(name="영어", score=90, student_id=student1.id)
session.add(subject2)

subject3 = Subject(name="수학", score=85, student_id=student2.id)
session.add(subject3)

subject4 = Subject(name="과학", score=80, student_id=student2.id)
session.add(subject4)

# 데이터베이스에 커밋하여 과목 데이터 저장
session.commit()

# 세션 닫기
session.close()
