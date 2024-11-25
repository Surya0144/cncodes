import socket

def udp_client():
    host = '127.0.0.1'  # Server's address
    port = 12345        # Server's port

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        print("Connected to the UDP server...")
        while True:
            message = input("Enter message to send (or 'exit' to quit): ")
            if message.lower() == 'exit':
                break
            client_socket.sendto(message.encode(), (host, port))
            data, _ = client_socket.recvfrom(1024)
            print(f"Received from server: {data.decode()}")

udp_client()
