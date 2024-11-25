import time
import random

TIMEOUT_DURATION = 2
FRAME_COUNT = 5
FRAME_CORRUPTION_PROBABILITY = 0.1

def sender():
    frame_number = 0
    sent_frames = 0
    
    while sent_frames < FRAME_COUNT:
        print(f"Sender: Sending frame {frame_number}")
        time.sleep(random.uniform(0.5, 1.5))
        
        if random.random() < FRAME_CORRUPTION_PROBABILITY:
            print(f"Sender: Frame {frame_number} got corrupted in transmission!")
            continue
        
        start_time = time.time()
        ack_received = False
        
        while not ack_received:
            if receiver_simulator(frame_number):
                print(f"Sender: Received ACK for frame {frame_number}")
                frame_number = 1 - frame_number
                sent_frames += 1
                ack_received = True
            else:
                if time.time() - start_time > TIMEOUT_DURATION:
                    print(f"Sender: Timeout occurred, resending frame {frame_number}")
                    break

    print("Sender: All frames transmitted successfully.")

def receiver_simulator(expected_frame):
    if random.random() < 0.1:
        print(f"Receiver: Frame {expected_frame} lost in transmission.")
        return False
    
    if random.random() < 0.1:
        print(f"Receiver: Received corrupted frame {expected_frame}. Discarding.")
        return False
    
    print(f"Receiver: Received frame {expected_frame} successfully.")
    time.sleep(random.uniform(0.5, 1.0))
    
    if random.random() < 0.1:
        print(f"Receiver: ACK for frame {expected_frame} lost in transmission.")
        return False
    
    print(f"Receiver: Sending ACK for frame {expected_frame}")
    return True

if __name__ == "__main__":
    sender()