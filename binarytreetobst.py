class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def binaryTreeToBST(root):

    # Step 1: Store inorder values
    values = []

    def inorder_store(root):
        if root is None:
            return
        inorder_store(root.left)
        values.append(root.data)
        inorder_store(root.right)

    inorder_store(root)

    # Step 2: Sort values
    values.sort()

    # Step 3: Put back values
    index = [0]   # using list to pass by reference

    def inorder_fill(root):
        if root is None:
            return
        inorder_fill(root.left)
        root.data = values[index[0]]
        index[0] += 1
        inorder_fill(root.right)

    inorder_fill(root)

    return root


# Helper: inorder print
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# ----------- MAIN PROGRAM -----------

# Create Binary Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)

# Convert to BST
binaryTreeToBST(root)

# Print inorder of BST
inorder(root)