def countSetBits(n):
    return bin(n).count('1')


# Function Call
n = int(input("Enter number: "))
print("Set bits:", countSetBits(n))