import random
import time

PACKET_LOSS_PROBABILITY = 0.1
FRAME_CORRUPTION_PROBABILITY = 0.1
ACK_LOSS_PROBABILITY = 0.1

def receiver(expected_frame):
    if random.random() < PACKET_LOSS_PROBABILITY:
        print(f"Receiver: Frame {expected_frame} lost in transmission.")
        return False
    
    if random.random() < FRAME_CORRUPTION_PROBABILITY:
        print(f"Receiver: Received corrupted frame {expected_frame}. Discarding.")
        return False
    
    print(f"Receiver: Received frame {expected_frame} successfully.")
    time.sleep(random.uniform(0.5, 1.0))
    
    if random.random() < ACK_LOSS_PROBABILITY:
        print(f"Receiver: ACK for frame {expected_frame} lost in transmission.")
        return False
    
    print(f"Receiver: Sending ACK for frame {expected_frame}")
    return True