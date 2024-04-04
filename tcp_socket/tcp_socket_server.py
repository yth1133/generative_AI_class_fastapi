import socket

# TCP 서버를 시작하는 함수입니다.
def start_server(host='127.0.0.1', port=65432):
    # socket 객체를 생성합니다. AF_INET은 IPv4를 사용하겠다는 의미이고, SOCK_STREAM은 TCP를 사용하겠다는 의미입니다.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_server:

        # 생성한 소켓을 주어진 호스트와 포트에 바인드(연결)합니다. 이는 서버가 해당 주소에서 클라이언트의 연결을 기다리게 합니다.
        socket_server.bind((host, port))

        # 소켓이 클라이언트의 연결을 기다리도록 설정합니다. 이 메서드는 소켓을 "리스닝" 상태로 만듭니다.
        socket_server.listen()
        print(f"서버가 연결되었습니다. {host}:{port}")

        # 클라이언트로부터 연결이 수립되면, accept 메서드는 연결된 클라이언트의 소켓 객체와 주소를 반환합니다.
        conn, addr = socket_server.accept()

        # 클라이언트와 연결된 소켓을 관리하는 코드 블록입니다. 이 블록을 벗어나면 연결은 자동으로 닫힙니다.
        with conn:
            print(f"연결된 소켓은 {addr}")

            # 무한 루프를 돌면서 클라이언트로부터 데이터를 받고, 받은 데이터를 그대로 클라이언트에게 다시 보냅니다(echo).
            while True:

                # 클라이언트로부터 데이터를 받습니다. 한 번에 최대 1024바이트를 읽을 수 있습니다.
                data = conn.recv(1024)

                # 받은 데이터가 없으면 연결이 종료된 것으로 간주하고 루프를 종료합니다. 이 부분은 상황에 맞춰 작성
                if not data:
                    break

                # 받은 데이터를 클라이언트에게 다시 보냅니다. 변형해서 보내도록 수정합니다
                conn.sendall(data)

# 이 스크립트가 직접 실행되었을 때만 start_server 함수를 호출합니다.
if __name__ == "__main__":
    start_server()
