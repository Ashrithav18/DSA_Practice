class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBalanced(root):

    def check(node):

        if node is None:
            return 0   # height = 0

        left = check(node.left)
        if left == -1:
            return -1

        right = check(node.right)
        if right == -1:
            return -1

        # check balance condition
        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)

    return check(root) != -1


# Function Call
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(60)

print(isBalanced(root))