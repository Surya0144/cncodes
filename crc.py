def binary_division(dividend, divisor, n):
    remainder = dividend[:9]
    for i in range(n):
        if remainder[0] == 1:
            for j in range(9):
                remainder[j] ^= divisor[j]
        if i + 9 < n + 8:
            remainder = remainder[1:] + [dividend[i + 9]]
    return remainder


def main():
    n = int(input("Enter the size of the data bits: "))
    dividend = [0] * (n + 8)
    print("Enter the data bits: ")
    for i in range(n):
        dividend[i] = int(input())
    divisor = [1, 0, 0, 0, 0, 0, 1, 1, 1]
    remainder = binary_division(dividend, divisor, n)
    for i in range(8):
        dividend[n + i] = remainder[i + 1]
    print("Encoded data bits are: ", *dividend)
    print("Enter data bits received at receiver's end: ")
    received = [int(input()) for _ in range(n + 8)]
    received_remainder = binary_division(received, divisor, n)
    if all(bit == 0 for bit in received_remainder[:8]):
        print("NO ERROR DETECTED....")
    else:
        print("ERROR DETECTED!!!!")


if __name__ == "__main__":
    main()
