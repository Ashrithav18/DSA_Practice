from collections import deque

def reverseQueue(q):
    stack = []

    # Step 1: Push all elements into stack
    while q:
        stack.append(q.popleft())

    # Step 2: Push back into queue
    while stack:
        q.append(stack.pop())

    return q


# Function Call
q = deque([5, 10, 15, 20, 25])

print("Original Queue:", list(q))

reverseQueue(q)

print("Reversed Queue:", list(q))