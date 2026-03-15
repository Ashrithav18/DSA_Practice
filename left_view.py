from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def leftView(root):

    if not root:
        return []

    q = deque([root])
    result = []

    while q:

        level_size = len(q)

        for i in range(level_size):

            node = q.popleft()

            # first node of level
            if i == 0:
                result.append(node.data)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

    return result


# Function Call
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(leftView(root))