def countSubstrings(s):
    
    def expand(left, right):
        count = 0
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
            
        return count

    total = 0

    for i in range(len(s)):
        # Odd length
        total += expand(i, i)
        
        # Even length
        total += expand(i, i+1)

    return total


# Test
print(countSubstrings("abc"))  # 3
print(countSubstrings("aaa"))  # 6