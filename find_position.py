def findPosition(n):
    # Step 1: check only one set bit
    if n == 0 or (n & (n - 1)) != 0:
        return -1
    
    # Step 2: find position
    position = 1
    
    while n > 0:
        if n & 1:   # if last bit is 1
            return position
        n = n >> 1
        position += 1


# ----------- MAIN PROGRAM -----------

n = int(input("Enter number: "))
print("Position:", findPosition(n))