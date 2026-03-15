from collections import deque

def reverseFirstK(q, k):

    n = len(q)

    if k > n:
        return q

    stack = []

    # Step 1: Push first k elements into stack
    for _ in range(k):
        stack.append(q.popleft())

    # Step 2: Push back into queue
    while stack:
        q.append(stack.pop())

    # Step 3: Move remaining elements
    for _ in range(n - k):
        q.append(q.popleft())

    return q


# Function Call
q = deque([1,2,3,4,5])
k = 3

print(list(reverseFirstK(q, k)))