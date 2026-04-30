def characterReplacement(s, k):
    count = {}          # frequency of characters
    left = 0
    max_freq = 0        # max frequency in current window
    max_length = 0

    for right in range(len(s)):
        # count current char
        count[s[right]] = count.get(s[right], 0) + 1
        
        # update max frequency
        max_freq = max(max_freq, count[s[right]])
        
        # check if window is valid
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1
        
        # update answer
        max_length = max(max_length, right - left + 1)

    return max_length


# Test
print(characterReplacement("ABAB", 2))      # 4
print(characterReplacement("AABABBA", 1))   # 4