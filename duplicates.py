def printDuplicates(s):
    freq = {}
    
    # Count frequency
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    
    # Print duplicates in order of first occurrence
    result = []
    for ch in freq:
        if freq[ch] > 1:
            result.append([ch, freq[ch]])
    
    return result


# Example usage
print(printDuplicates("geeksforgeeks"))
print(printDuplicates("programming"))
print(printDuplicates("mississippi"))