# csv파일 불러와서 일정을 출력하는 API라우터
from fastapi import APIRouter, HTTPException
import pandas as pd

router_schedule = APIRouter(prefix="/schedule")

# CSV 파일에서 데이터를 읽어오는 함수
def read_csv_file(file_name: str):
    df = pd.read_csv(file_name)
    return df.to_dict(orient="records")  # 데이터프레임을 리스트 형태로 변환

# CSV 파일에서 일정 데이터를 가져오는 API 라우터
@router_schedule.get("/events")
async def get_events():
    events_data = read_csv_file("csv_example1.csv")
    return events_data