class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isDeadEnd(root):
    nodes = set()
    leaves = set()

    # inorder traversal
    def inorder(root):
        if root is None:
            return

        inorder(root.left)

        # store node
        nodes.add(root.data)

        # check leaf
        if root.left is None and root.right is None:
            leaves.add(root.data)

        inorder(root.right)

    inorder(root)

    # Add 0 (important trick)
    nodes.add(0)

    # Check dead end
    for leaf in leaves:
        if (leaf - 1) in nodes and (leaf + 1) in nodes:
            return True

    return False


# ----------- MAIN PROGRAM -----------

# Create BST
root = Node(8)
root.left = Node(5)
root.right = Node(9)
root.left.left = Node(2)
root.left.right = Node(7)
root.left.left.left = Node(1)

# Function call