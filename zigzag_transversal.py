from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def zigzagTraversal(root):

    if not root:
        return []

    q = deque([root])
    result = []
    left_to_right = True

    while q:

        level_size = len(q)
        level = []

        for _ in range(level_size):

            node = q.popleft()
            level.append(node.data)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        if not left_to_right:
            level.reverse()

        result.extend(level)

        left_to_right = not left_to_right

    return result


# Function Call
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(zigzagTraversal(root))