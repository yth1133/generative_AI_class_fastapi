from fastapi import FastAPI, File, UploadFile, HTTPException
import cv2
from io import BytesIO
import numpy as np
import base64
from pydantic import BaseModel

app = FastAPI()

class ImageData(BaseModel):
    username: str
    image_base64: str

# 파일 업로드 형식의 엔드포인트
@app.post("/upload_imgfile/")
async def create_upload_file(file: UploadFile = File(...)):

    # 이미지 데이터를 읽고 PIL 이미지 객체로 변환
    image_data = await file.read()
    print(file.filename)
    nparr = np.fromstring(image_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # OpenCV를 사용한 이미지 증강: 여기서는 이미지를 반전시킵니다.
    img_flipped = cv2.flip(img, 0)

    # 변경된 이미지를 저장해보기
    save_path = "image_processing_"+file.filename
    cv2.imwrite(save_path, img_flipped)
   
    # 변환된 이미지 데이터를 반환 (실제 애플리케이션에서는 파일로 저장하거나 다른 처리를 수행할 수 있음)
    return {"save_path": save_path, "content_type": file.content_type}

# base64 업로드 형식의 엔드포인트
@app.post("/upload_base64/")
async def upload_image(data: ImageData):
    # 사용자 이름 확인
    username = data.username
    # Base64 인코딩된 이미지 데이터를 디코딩하여 바이너리 데이터로 변환
    try:
        image_data = base64.b64decode(data.image_base64)
        # 여기에서 이미지 데이터를 파일로 저장하거나 처리합니다.
        # 파일로 저장해보기
        save_path = f"image_processing_{username}_base64.jpg"
        with open(save_path, "wb") as file:
            file.write(image_data)
        return {"save_path": save_path}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"이미지 처리 중 오류가 발생했습니다: {str(e)}")