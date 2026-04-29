def markMultiples(a, b):
    size = b - a + 1

    # Bit array (each int holds 32 bits)
    bit_array = [0] * ((size + 31) // 32)

    # Mark multiples of 2 and 5
    for num in range(a, b + 1):
        if num % 2 == 0 or num % 5 == 0:
            idx = (num - a) // 32
            bit = (num - a) % 32
            bit_array[idx] |= (1 << bit)

    # Print results
    result = []
    for num in range(a, b + 1):
        idx = (num - a) // 32
        bit = (num - a) % 32

        if bit_array[idx] & (1 << bit):
            result.append(num)

    return result


# Test
print(markMultiples(2, 10))
print(markMultiples(60, 95))