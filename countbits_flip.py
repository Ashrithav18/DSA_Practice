def countBitsFlip(a, b):
    # Step 1: XOR
    xor = a ^ b
    
    # Step 2: Count set bits
    count = 0
    while xor:
        count += xor & 1   # check last bit
        xor = xor >> 1     # shift right
    
    return count


# Function Call
a = 10
b = 20
print(countBitsFlip(a, b))   # Output: 4