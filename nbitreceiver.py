import socket

host = 'localhost'
port = 12345

class Receiver:
    def __init__(self, conn):
        self.expected_frame = 0
        self.conn = conn

    def receive_frame(self):
        frame = self.conn.recv(1024).decode().strip()

        if not frame:
            print("Receiver: Connection closed by the sender.")
            return False

        try:
            frame = int(frame)
            if frame == self.expected_frame:
                print(f"Receiver: Received expected frame {frame}, sending ACK")
                self.conn.sendall(str(frame).encode())
                self.expected_frame += 1
            else:
                print(f"Receiver: Frame {frame} out of order, expected {self.expected_frame}. Ignoring.")
                self.conn.sendall(str(self.expected_frame - 1).encode())
        except ValueError:
            print(f"Receiver: Received invalid frame data '{frame}', ignoring.")
        
        return True

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        sock.listen(1)
        print(f"Receiver: Listening on {host}:{port}")

        conn, addr = sock.accept()
        with conn:
            print(f"Receiver: Connected by {addr}")
            receiver = Receiver(conn)

            while receiver.receive_frame():
                pass

if __name__ == "__main__":
    main()