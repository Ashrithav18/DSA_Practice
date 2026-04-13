def isPowerOfTwo(n):
    return n > 0 and (n & (n - 1)) == 0


# ----------- MAIN PROGRAM -----------

n = int(input("Enter number: "))

if isPowerOfTwo(n):
    print("True")
else:
    print("False")