def isValid(s):
    stack = []
    
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        else:
            if not stack:
                return False
            
            top = stack.pop()
            
            if pairs[ch] != top:
                return False
    
    return len(stack) == 0


# 🔹 Function Calls
print(isValid("()"))        # True
print(isValid("()[]{}"))    # True
print(isValid("(]"))        # False
print(isValid("([])"))      # True
print(isValid("([)]"))      # False

print(isValid("()"))