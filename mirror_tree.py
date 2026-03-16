class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def mirrorTree(root):

    if root is None:
        return None

    newNode = Node(root.data)

    # swap children
    newNode.left = mirrorTree(root.right)
    newNode.right = mirrorTree(root.left)

    return newNode


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Function Call
root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(4)

print("Inorder of original tree:")
inorder(root)

mirror = mirrorTree(root)

print("\nInorder of mirror tree:")
inorder(mirror)