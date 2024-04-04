from fastapi import FastAPI, WebSocket
import cv2
import numpy as np
import base64
from io import BytesIO

app = FastAPI()

@app.websocket("/ws/image")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        # 클라이언트로부터 바이너리 데이터(이미지) 수신
        image_data = await websocket.receive_bytes()
        if image_data:
            # 바이너리 데이터를 numpy 배열로 변환
            nparr = np.frombuffer(image_data, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            # 이미지를 세로로 플립(수직 반전)
            flipped_img = cv2.flip(img, 0)
            # 플립된 이미지를 Base64 인코딩하여 전송
            _, buffer = cv2.imencode('.jpg', flipped_img)
            jpg_as_text = base64.b64encode(buffer).decode()
            await websocket.send_text(jpg_as_text)
        else:
            break
