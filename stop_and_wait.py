import time
import random

# Constants
TIMEOUT_DURATION = 2  # Timeout duration for waiting ACK (in seconds)
FRAME_COUNT = 5  # Number of frames to send

# Simulate packet loss, corruption, and ACK loss probabilities
PACKET_LOSS_PROBABILITY = 0.1
ACK_LOSS_PROBABILITY = 0.1
FRAME_CORRUPTION_PROBABILITY = 0.1

# Sender function that implements Stop-and-Wait Protocol with timeout handling
def sender():
    frame_number = 0  # Initial frame number
    sent_frames = 0   # Track how many frames have been successfully sent
    
    while sent_frames < FRAME_COUNT:
        print(f"Sender: Sending frame {frame_number}")
        
        # Simulate transmission delay
        time.sleep(random.uniform(0.5, 1.5))
        
        # Simulate frame corruption
        if random.random() < FRAME_CORRUPTION_PROBABILITY:
            print(f"Sender: Frame {frame_number} got corrupted in transmission!")
            continue
        
        # Start the timer and wait for the ACK
        start_time = time.time()
        ack_received = False
        
        while not ack_received:
            if receiver(frame_number):
                print(f"Sender: Received ACK for frame {frame_number}")
                frame_number = 1 - frame_number  # Flip the frame bit for the next frame
                sent_frames += 1  # Successfully sent and acknowledged the frame
                ack_received = True
            else:
                # Check if timeout has occurred
                if time.time() - start_time > TIMEOUT_DURATION:
                    print(f"Sender: Timeout occurred, resending frame {frame_number}")
                    break  # Resend the frame after timeout

    print("Sender: All frames transmitted successfully.")

# Receiver function
def receiver(expected_frame):
    # Simulate random packet loss
    if random.random() < PACKET_LOSS_PROBABILITY:
        print(f"Receiver: Frame {expected_frame} lost in transmission.")
        return False
    
    # Simulate frame corruption
    if random.random() < FRAME_CORRUPTION_PROBABILITY:
        print(f"Receiver: Received corrupted frame {expected_frame}. Discarding.")
        return False
    
    print(f"Receiver: Received frame {expected_frame} successfully.")
    
    # Simulate transmission delay for ACK
    time.sleep(random.uniform(0.5, 1.0))
    
    # Simulate ACK loss
    if random.random() < ACK_LOSS_PROBABILITY:
        print(f"Receiver: ACK for frame {expected_frame} lost in transmission.")
        return False
    
    print(f"Receiver: Sending ACK for frame {expected_frame}")
    return True

if __name__ == "__main__":
    sender()
