import socket

def udp_server():
    host = '127.0.0.1'  # localhost
    port = 12345        # Port to listen on

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"UDP Server listening on {host}:{port}...")
        while True:
            data, addr = server_socket.recvfrom(1024)
            print(f"Received from {addr}: {data.decode()}")
            server_socket.sendto(data, addr)  # Echo back the received data

udp_server()
