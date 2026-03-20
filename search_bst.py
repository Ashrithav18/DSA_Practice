class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def searchBST(root, key):

    while root:

        if key == root.val:
            return True

        elif key < root.val:
            root = root.left

        else:
            root = root.right

    return False

# Build BST
root = Node(6)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.right = Node(9)

print(searchBST(root, 4))  # True
print(searchBST(root, 7))  # False