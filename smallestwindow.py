from collections import Counter

def smallestWindow(s, p):
    if len(p) > len(s):
        return ""

    need = Counter(p)   # required characters
    window = {}
    
    have = 0
    need_count = len(need)

    left = 0
    min_len = float('inf')
    start = 0

    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char, 0) + 1

        # Check if current char meets requirement
        if char in need and window[char] == need[char]:
            have += 1

        # Try shrinking window
        while have == need_count:
            
            # Update answer
            if (right - left + 1) < min_len:
                min_len = right - left + 1
                start = left

            # Remove from left
            window[s[left]] -= 1
            if s[left] in need and window[s[left]] < need[s[left]]:
                have -= 1

            left += 1

    return "" if min_len == float('inf') else s[start:start + min_len]


# Test
print(smallestWindow("timetopractice", "toc"))   # "toprac"
print(smallestWindow("zoomlazapzo", "oza"))      # "apzo"
print(smallestWindow("zoom", "zooe"))            # ""