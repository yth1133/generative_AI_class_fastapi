## 이 코드는 두개의 클라이언트가 연결되었을 경우, 각각의 클라이언트에 다른 정볼을 보내주는 소켓 코드입니다.
import select
import socket

host = "0.0.0.0" 
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen()
    print("서버가 연결을 기다립니다.")

    server_socket.setblocking(False)
    inputs = [server_socket]
    outputs = []

    while inputs:
        readable, writable, exceptional = select.select(inputs, outputs, inputs)

        for socket_s in readable:
            if socket_s is server_socket:
                connection, client_address = socket_s.accept()
                print(f"연결된 클라이언트: {client_address}")
                connection.setblocking(0)
                inputs.append(connection)
            else:
                # 여기서는 데이터를 받지 않으므로, 바로 pass 처리
                pass

        for socket_s in writable:
            # 클라이언트를 구분하는 로직
            if client_address:  # 클라이언트 주소가 있는 경우
                ip, port = client_address
                try:
                    # 특정 클라이언트 식별 로직 - IP 주소로 판별하기
                    if ip == "여기 클라이언트 IP 주소 넣기":
                        data = "1".encode()  # 여기 데이터 수정
                    else:
                        data = "2".encode()  # 여기는 다른 클라이언트에 보낼 데이터
                    socket_s.sendall(data)
                except Exception as e:
                    print(f"클라이언트 {client_address} 연결이 종료되었습니다. 오류: {e}")
                    inputs.remove(socket_s)
                    if socket_s in outputs:
                        outputs.remove(socket_s)
                    socket_s.close()

        for socket_s in exceptional:
            inputs.remove(socket_s)
            if socket_s in outputs:
                outputs.remove(socket_s)
            socket_s.close()

        outputs = list(inputs)
        outputs.remove(server_socket)