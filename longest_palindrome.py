def longestPalindrome(s):
    
    def expand(left, right):
        # Expand while valid palindrome
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    longest = ""

    for i in range(len(s)):
        # Odd length
        p1 = expand(i, i)
        
        # Even length
        p2 = expand(i, i+1)
        
        # Take longer one
        if len(p1) > len(longest):
            longest = p1
        if len(p2) > len(longest):
            longest = p2

    return longest


# Test
print(longestPalindrome("babad"))  # "bab" or "aba"
print(longestPalindrome("cbbd"))   # "bb"