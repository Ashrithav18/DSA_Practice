import collections

def minOperations(s1, s2):

    # Step 1: Length check
    if len(s1) != len(s2):
        return -1

    # Step 2: Frequency check
    if collections.Counter(s1) != collections.Counter(s2):
        return -1

    n = len(s1)

    i = n - 1   # pointer for s1
    j = n - 1   # pointer for s2

    operations = 0

    # Step 3: Compare from end
    while i >= 0:

        # If characters match
        if s1[i] == s2[j]:
            i -= 1
            j -= 1

        else:
            # Move only i
            operations += 1
            i -= 1

    return operations


# -------- TEST CASES --------

print(minOperations("abd", "bad"))                 # 1
print(minOperations("GeeksForGeeks", "ForGeeksGeeks"))   # 3
print(minOperations("abc", "bca"))                 # 2
print(minOperations("abc", "def"))                 # -1