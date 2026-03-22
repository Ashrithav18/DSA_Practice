class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def kthLargest(root, k):
    count = [0]   # to track count
    result = [-1] # to store answer

    def reverse_inorder(node):
        if node is None or count[0] >= k:
            return

        # Step 1: Right
        reverse_inorder(node.right)

        # Step 2: Root
        count[0] += 1
        if count[0] == k:
            result[0] = node.data
            return

        # Step 3: Left
        reverse_inorder(node.left)

    reverse_inorder(root)
    return result[0]


# ----------- MAIN PROGRAM -----------

# Create BST
root = Node(4)
root.left = Node(2)
root.right = Node(9)

k = 2

print("Kth Largest:", kthLargest(root, k))