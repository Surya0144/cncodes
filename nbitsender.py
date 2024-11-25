import socket
import time
import random

N = 4
window_size = 2**N
total_frames = 10
host = 'localhost'
port = 12345

class Sender:
    def __init__(self, sock):
        self.window_start = 0
        self.window_end = window_size - 1
        self.next_frame_to_send = 0
        self.sock = sock

    def send_frame(self):
        if self.next_frame_to_send <= self.window_end:
            print(f"Sender: Sending frame {self.next_frame_to_send}")
            self.sock.sendall(str(self.next_frame_to_send).encode())
            return self.next_frame_to_send
        else:
            print("Sender: Window full, waiting for ACK...")
            return None

    def receive_ack(self):
        ack = self.sock.recv(1024).decode()
        print(f"Sender: Received ACK for frame {ack}")
        ack = int(ack)
        if self.window_start <= ack <= self.window_end:
            self.window_start = ack + 1
            self.window_end = self.window_start + window_size - 1
            self.next_frame_to_send = self.window_start
        else:
            print(f"Sender: ACK {ack} is out of window bounds")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sender = Sender(sock)

        while sender.next_frame_to_send < total_frames:
            frame = sender.send_frame()
            if frame is not None:
                time.sleep(1)

                if random.random() < 0.8:
                    sender.receive_ack()
                else:
                    print(f"Sender: Frame {frame} lost during transmission.")

            sender.next_frame_to_send += 1
            time.sleep(1)

if __name__ == "__main__":
    main()
