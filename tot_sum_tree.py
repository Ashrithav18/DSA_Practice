class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def toSumTree(root):

    if root is None:
        return 0

    # store old value
    old_val = root.data

    # get sums of left and right
    left_sum = toSumTree(root.left)
    right_sum = toSumTree(root.right)

    # update node value
    root.data = left_sum + right_sum

    # return total sum including old value
    return root.data + old_val


# Helper to print inorder
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Function Call
root = Node(10)
root.left = Node(-2)
root.right = Node(6)
root.left.left = Node(8)
root.left.right = Node(-4)
root.right.left = Node(7)
root.right.right = Node(5)

toSumTree(root)

inorder(root)