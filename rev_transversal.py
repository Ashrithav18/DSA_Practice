from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def reverseLevelOrder(root):

    if root is None:
        return []

    q = deque()
    stack = []

    q.append(root)

    while q:

        node = q.popleft()
        stack.append(node.data)

        # push right first
        if node.right:
            q.append(node.right)

        if node.left:
            q.append(node.left)

    # reverse order
    result = []

    while stack:
        result.append(stack.pop())

    return result


# Function Call
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(60)

print(reverseLevelOrder(root))