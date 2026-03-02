def isPermutationPossible(a, b, k):
    # Step 1: Sort a ascending
    a.sort()
    
    # Step 2: Sort b descending
    b.sort(reverse=True)
    
    # Step 3: Check condition
    for i in range(len(a)):
        if a[i] + b[i] < k:
            return False
    
    return True


# Example usage
print(isPermutationPossible([2,1,3], [7,8,9], 10))  # True
print(isPermutationPossible([1,2,2,1], [3,3,3,4], 5))  # False