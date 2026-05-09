def rabinKarp(text, pattern):
    d = 256          # number of characters
    q = 101          # prime number

    n = len(text)
    m = len(pattern)

    p_hash = 0       # hash value for pattern
    t_hash = 0       # hash value for text window
    h = 1

    result = []

    # h = pow(d, m-1) % q
    for i in range(m - 1):
        h = (h * d) % q

    # Calculate initial hash values
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    # Slide pattern over text
    for i in range(n - m + 1):

        # If hash values match
        if p_hash == t_hash:

            # Check characters one by one
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break

            if match:
                result.append(i)

        # Calculate next window hash
        if i < n - m:
            t_hash = (
                d * (t_hash - ord(text[i]) * h)
                + ord(text[i + m])
            ) % q

            # Handle negative hash
            if t_hash < 0:
                t_hash += q

    return result


# -------- TEST CASES --------

print(rabinKarp("geeksforgeeks", "geeks"))     
# [0, 8]

print(rabinKarp("aabaacaadaabaaba", "aaba"))  
# [0, 9, 12]