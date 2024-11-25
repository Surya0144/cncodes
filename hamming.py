import math

# Function to calculate parity bits for the encoded data
def calculate_parity_bits(encoded_data, data_length, redundant_bits):
    for i in range(redundant_bits):
        parity_bit_position = 2 ** i
        for j in range(1, data_length + redundant_bits + 1):
            if ((j >> i) & 1) == 1:
                encoded_data[parity_bit_position] ^= encoded_data[j]

# Function to find the position of the erroneous bit in the received data
def find_error_position(received_data, data_length, redundant_bits):
    error_position = 0
    for i in range(redundant_bits):
        parity_bit_position = 2 ** i
        parity = 0
        for j in range(1, data_length + redundant_bits + 1):
            if ((j >> i) & 1) == 1:
                parity ^= received_data[j]
        if parity != 0:
            error_position += parity_bit_position
    return error_position

def main():
    data_length = int(input("Enter the length of data bits: "))

    # Calculate the number of redundant bits required
    redundant_bits = 0
    while (2 ** redundant_bits) < (data_length + redundant_bits + 1):
        redundant_bits += 1

    # Input the data bits
    print("Enter the data bits: ")
    data_bits = [0] + [int(input()) for _ in range(data_length)]

    # Initialize the encoded data with parity bits set to 0
    encoded_data = [0] * (data_length + redundant_bits + 1)

    # Fill the encoded data with data bits, skipping parity bit positions
    data_index = 1
    for i in range(1, data_length + redundant_bits + 1):
        if (i & (i - 1)) == 0:  # Check if the position is a power of 2
            continue
        encoded_data[i] = data_bits[data_index]
        data_index += 1

    # Calculate and set the parity bits
    calculate_parity_bits(encoded_data, data_length, redundant_bits)

    # Output the encoded data
    print("Encoded data: ", *encoded_data[1:])

    # Input the received data
    print("Enter the received data bits: ")
    received_data = [0] + [int(input()) for _ in range(data_length + redundant_bits)]

    # Find the position of the error in the received data
    error_position = find_error_position(received_data, data_length, redundant_bits)

    # Check if there is an error in the received data
    if error_position == 0:
        print("No error in the data bits.")
    else:
        print(f"Error found in the data bit. The position of the error bit is: {error_position}")
        # Correct the error by flipping the bit at the error position
        received_data[error_position] ^= 1

        # Output the corrected data
        print("The data after error detection and correction is: ", *received_data[1:])

if __name__ == "__main__":
    main()
