# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to find minimum in BST
def findMin(root):

    # If tree is empty
    if root is None:
        return None

    # Go to leftmost node
    while root.left is not None:
        root = root.left

    return root.data


# ----------- MAIN PROGRAM -----------

# Create BST
root = Node(5)
root.left = Node(4)
root.right = Node(6)
root.left.left = Node(3)
root.left.left.left = Node(1)
root.right.right = Node(7)

# Call function
min_value = findMin(root)

# Print result
print("Minimum value in BST is:", min_value)