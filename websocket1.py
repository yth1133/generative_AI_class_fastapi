from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()  # 클라이언트의 연결 요청을 수락
    cnt = 1
    while True:
        data = await websocket.receive_text()  # 클라이언트로부터 메시지를 받음
        message = f"{cnt}.  받은 메시지: {data}"
        await websocket.send_text(message)  # 받은 메시지를 클라이언트에게 다시 전송
        print(message)
        cnt +=1