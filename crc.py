def binary_division(dividend, divisor, n):
    """Perform binary division using CRC and return the remainder."""
    # Copy initial bits of the dividend to the remainder
    remainder = dividend[:9]

    # Perform division bit by bit
    for i in range(n):
        # If the first bit of the remainder is 1, perform XOR with the divisor
        if remainder[0] == 1:
            for j in range(9):
                remainder[j] ^= divisor[j]

        # Shift the remainder left and bring down the next bit of the dividend
        if i + 9 < n + 8:  # Ensure we don't access out of bounds
            remainder = remainder[1:] + [dividend[i + 9]]

    return remainder


def main():
    n = int(input("Enter the size of the data bits: "))
    # Dividend array with room for the appended remainder
    dividend = [0] * (n + 8)

    print("Enter the data bits: ")
    for i in range(n):
        dividend[i] = int(input())

    # Divisor for binary division (hardcoded for this example: CRC-8 polynomial)
    divisor = [1, 0, 0, 0, 0, 0, 1, 1, 1]  # Polynomial x^8 + x^7 + x^4 + x^3 + x^2 + 1

    # Perform binary division
    remainder = binary_division(dividend, divisor, n)

    # Append remainder to the end of the original data
    for i in range(8):
        dividend[n + i] = remainder[i + 1]

    # Output the encoded data
    print("Encoded data bits are: ", *dividend)

    # Input received data bits for error checking
    print("Enter data bits received at receiver's end: ")
    received = [int(input()) for _ in range(n + 8)]

    # Perform binary division on received data
    received_remainder = binary_division(received, divisor, n)

    # Check the remainder to detect errors
    if all(bit == 0 for bit in received_remainder[:8]):
        print("NO ERROR DETECTED....")
    else:
        print("ERROR DETECTED!!!!")


if __name__ == "__main__":
    main()
